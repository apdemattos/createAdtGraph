
import sys
import logging
import json
import logging
from revtiTypesToLabels import revitFamiliesToDtDlModel
from neo4jFunctions import App
import asyncio
import argparse
from httpRequests import getModelHigharchy, getModelProperties

logging.basicConfig(filename='std.log', format='%(asctime)s %(message)s', filemode='w')
logger=logging.getLogger() 
logger.setLevel(logging.DEBUG) 

parser = argparse.ArgumentParser()
parser.add_argument('--buildingId', default=None, help='Unique Building Id code')
parser.add_argument('--buildingName', default=None, help='Building Name')
parser.add_argument('--roomsPath', default=None, help='Path to Room and Level mapping file')
parser.add_argument('--archUrn', default=None, help='Architectural URN')
parser.add_argument('--mechUrn', default=None, help='Mechanical URN')
parser.add_argument('--elecUrn', default=None, help='Electrical URN')
parser.add_argument('--plumbUrn', default=None, help='Plumbing URN')

args = parser.parse_args()

#Dunbar
# ArchitecturalUrn = 'dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6ZHVuYmFycmV2aXRfMTEyNi9BcmNoaXRlY3R1cmFsX1VwZGF0ZWQucnZ0'
# MechanicalUrn = 'dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6ZHVuYmFycmV2aXRfMTEyNi9NZWNoYW5pY2FsLnJ2dA'
# ElectricalUrn = 'dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6ZHVuYmFycmV2aXRfMTEyNi9FbGVjdHJpY2FsLnJ2dA'
# PlumbingUrn = 'dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6ZHVuYmFycmV2aXRfMTEyNi9QbHVtYmluZy5ydnQ'

#Havtech 
# ArchitecturalUrn = 'dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6aGF2dGVjaHJldml0bW9kZWxfMTEyNy9BcmNoaXRlY3R1cmUucnZ0'
# MechanicalUrn = 'dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6aGF2dGVjaHJldml0bW9kZWxfMTEyNy9NZWNoYW5pY2FsLnJ2dA'
# ElectricalUrn = 'dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6aGF2dGVjaHJldml0bW9kZWxfMTEyNy9FbGVjdHJpY2FsLnJ2dA'
# PlumbingUrn =  'dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6aGF2dGVjaHJldml0bW9kZWxfMTEyNy9QbHVtYmluZy5ydnQ'

async def loadData(): 
    if(args.archUrn == None or args.mechUrn == None or args.elecUrn == None or args.plumbUrn == None or args.roomsPath == None):
        print('Please provide a urn for all model (A,M,E,P')
        sys.exit()
    # Architectural
    archInstanceTree = await getModelHigharchy(args.archUrn)
    archProperties = await getModelProperties(args.archUrn)
    # archCoords = json.load(open('./Havtech/Architectural/Havtech_Architectural_Coordinates.json'))
    archRoomLevelMap = json.load(open(args.roomsPath))
    Architectural = {'Name': 'Architectural', 'urn': args.archUrn, 'Instance Tree': archInstanceTree, 'Properties': archProperties, 'Rooms': archRoomLevelMap, 'Coords': ''}

    # Mechanical
    mechInstanceTree = await getModelHigharchy(args.mechUrn)
    mechProperties = await getModelProperties(args.mechUrn)
    # mechCoords = json.load(open('./Havtech/Mechanical/Havtech_Mechanical_Coordinates.json'))
    Mechanical = {'Name': 'Mechanical', 'urn': args.mechUrn, 'Instance Tree': mechInstanceTree, 'Properties': mechProperties, 'Coords': ''}

    # Plumbing
    plumbInstanceTree = await getModelHigharchy(args.plumbUrn)
    plumbProperties = await getModelProperties(args.plumbUrn)
    # plumbCoords = json.load(open('./Havtech/Plumbing/Havtech_Plumbing_Coordinates.json'))
    Plumbing = {'Name': 'Plumbing', 'urn': PlumbingUrn,'Instance Tree': plumbInstanceTree, 'Properties': plumbProperties, 'Coords': ''}

    # Electrical 
    elecInstanceTree = await getModelHigharchy(args.elecUrn)
    elecProperties = await getModelProperties(args.elecUrn)
    # elecCoords = json.load(open('./Havtech/Electrical/Havtech_Electrical_Coordinates.json'))
    Electrical = {'Name': 'Electrical', 'urn': args.elecUrn, 'Instance Tree': elecInstanceTree, 'Properties': elecProperties, 'Coords': ''}

    return Architectural, Mechanical, Electrical, Plumbing


createdTwins= []

# Labels
facilityModelId = 'Space:Building'
floorModelId = 'BuildingComponent:Architectural:Floor'
spaceModelId = 'Space:Room'
systemModelId = 'Collection:AssetCollection:Equipment:System'

componentsLocation = {}

# Get Level - Function to return what level a asset is located on
#       Parameters: 
#           propreties - a instances properties
#       Returns: 
#           None if the level is not found, else returns the level the asset is located on
def getLevel(properties):
    level = None
    if 'Constraints' in properties:
        if('Reference Level' in properties['Constraints']):
            level = properties['Constraints']['Reference Level']
        elif('Level' in properties['Constraints']):
            level = properties['Constraints']['Level']
        elif('Schedule Level' in properties['Constraints']):
            level = properties['Constraints']['Schedule Level']
        elif('Base Level' in properties['Constraints']):
            level = properties['Constraints']['Base Level']
        elif('Base Constraint' in properties['Constraints']):
            level = properties['Constraints']['Base Constraint']

    return level

# Get Room - Function to use X,Y,Z Coordinate data to find the room location of a asset
#       Paramters: 
#           coordinates - data for all coordinates of everything in given revit model
#           externalId - the externalId of the asset 
#       Returns: 
#           array of locations
def getRoom(coordinates, externalId, roomLevelMap):
    coords = [coord for coord in coordinates if coord['ExtIdentifier'] == externalId]
    componentCenterPoint = coords[0]['center']
    componentMinPoint = coords[0]['minCoordinates']
    componentMaxPoint = coords[0]['maxCoordinates']
    # print(componentCenterPoint)
    # print(componentMinPoint)
    # print(componentMaxPoint)

    locations = []
    for floor in roomLevelMap:
        for room in roomLevelMap[floor]:
            # print(room['_bounds'])
            roomBox = room['_bounds']
            if roomBox['min']['x'] + 5 < componentMinPoint['x'] and roomBox['min']['y'] + 5 < componentMinPoint['y'] and roomBox['min']['z'] + 5 < (componentMinPoint['z'] + 1):
                if roomBox['max']['x'] + 5 > componentMaxPoint['x'] and roomBox['max']['y'] + 5 > componentMaxPoint['y'] and roomBox['max']['z'] + 5 > componentMaxPoint['z']:
                    # print('component in ' + room['_name'])
                    locations.append(room['_name'])

    return locations


# Function to iterate over a models instance tree and its properties
def createAssets(app, instanceTree, propreties, coordinates, roomLevelMap, facilityId, modelCode, modelName, modelUrn):
    for Category in instanceTree['data']['objects'][0]['objects']:
        if Category['name'] == 'Rooms' or Category['name'] == 'Spaces':
            for room in Category['objects']:
                # print(room['name'])
                pass
        else:
            for Family in Category['objects']:
                labels = ''
                if Family['name'] in revitFamiliesToDtDlModel:
                    labels = revitFamiliesToDtDlModel[Family['name']]  
                else:
                    labels = 'Asset'
            
                for Type in Family['objects']:
                    for Instance in Type['objects']:
                        instanceProperties = [prop for prop in propreties['data']['collection'] if prop['objectid'] == Instance['objectid']]
                        instanceProperties = instanceProperties[0]
                        externalId = instanceProperties['externalId']

                        # Get Room
                        # roomLocations = getRoom(coordinates, externalId, roomLevelMap)
                        # if roomLocations == []:
                        #     logger.warning('Room not found for instance: {} externalId: {}'.format(instanceProperties['name'], externalId))
                        # else: 
                        #     logger.info('Instance {} externalId: {} located in {}'.format(instanceProperties['name'], externalId, roomLocations))

                        # Get the Level
                        # instanceLevel = getLevel(instanceProperties['properties'])
                        # if instanceLevel == None:
                        #     logger.error('Level not found: {} Constraints: {}'.format(instanceProperties['name'], instanceProperties['properties']['Constraints']))

                        # Create asset
                        assetId = facilityId + '-' + modelCode + '-' + externalId
                        # instanceProperties['properties']['Identity Data']['Type Name'] if 'Type Name' in instanceProperties['properties']['Identity Data'] else 
                        app.merge_asset(assetId, instanceProperties['name'], labels, externalId)

                        # Asset is in Building
                        app.merge_asset_part_of_building(assetId, facilityId)

                        # Assign asset to the revit model it came from
                        app.merge_asset_from_revit_model(facilityId, assetId, modelName, modelUrn)

                        # Asset is located on level
                        # if instanceLevel is not None:
                        #     floorId = facilityId + '-A-' + instanceLevel.replace(" ", "")
                        #     app.merge_asset_located_on_floor(assetId, floorId, floorId)
                        
                        # Create Systems
                        if 'Mechanical' in instanceProperties['properties']:
                            if 'System Name' in instanceProperties['properties']['Mechanical']:
                                systems = instanceProperties['properties']['Mechanical']['System Name'].split(",")
                                for system in systems:
                                    if(system != ""):
                                        systemId = facilityId + '-' + modelCode + '-' + system.replace(" ", "")
                                        # System
                                        if(not systemId in createdTwins):
                                            systemLabel = systemModelId
                                            if modelCode == 'M':
                                                systemLabel += ':HVAC'
                                            elif modelCode == 'P':
                                                systemLabel += ":Plumbing"
                                            app.merge_system(systemId, system, systemLabel)
                                            app.merge_system_of_building(systemId, facilityId, modelUrn)
                                            createdTwins.append(systemId)
                                            logger.info('Created System: {}'.format(system))
                            
                                        # Asset is included in System
                                        app.merge_asset_includedIn_system_rel(assetId, systemId)

def createFloorsAndRooms(app, facilityId, roomLevelMap):
    for floor in roomLevelMap:
        # Create Floor
        floorId = facilityId + '-A-' + floor.replace(" ", "")

        app.merge_floor(floorId, floor, floorModelId)

        # Floor Located In Facility
        app.merge_floor_locatedIn_building_rel(floorId, facilityId)

        for room in roomLevelMap[floor]:
            roomExternalId = room['_info']["externalId"]
            roomId = facilityId + '-A-' +  roomExternalId
            # Create Room
            roomName = room['_info']["name"].replace("'", "").split("[")[0]
            app.merge_room(roomId, roomName, spaceModelId, roomExternalId)

            # Room is location of floor
            app.merge_room_isLocationOf_floor_rel(roomId, floorId)

async def main(app):
    # Load Data
    ArchitecturalData, MechanicalData, ElectricalData, PlumbingData = await loadData()

    # Create Building
    if args.buildingId == None or args.buildingName == None:
        print('Please provide a building id and name')
        sys.exit()
    facilityId = args.buildingId
    facilityName = args.buildingName
    app.merge_building(facilityId, facilityModelId, facilityName)  

    # Create Levels and Rooms
    createFloorsAndRooms(app, facilityId, ArchitecturalData['Rooms'])

    # Loop through revit models - create nodes 
    # Create Asset & relate it to the building
    # Group Assets by system
    createAssets(app, ArchitecturalData['Instance Tree'], ArchitecturalData['Properties'], ArchitecturalData['Coords'], ArchitecturalData['Rooms'], facilityId, 'A', ArchitecturalData['Name'], ArchitecturalData['urn'])
    createAssets(app, MechanicalData['Instance Tree'], MechanicalData['Properties'], MechanicalData['Coords'], ArchitecturalData['Rooms'], facilityId, 'M', MechanicalData['Name'], MechanicalData['urn'])
    createAssets(app, ElectricalData['Instance Tree'], ElectricalData['Properties'], ElectricalData['Coords'], ArchitecturalData['Rooms'], facilityId, 'E', ElectricalData['Name'], ElectricalData['urn'])
    createAssets(app, PlumbingData['Instance Tree'], PlumbingData['Properties'], PlumbingData['Coords'], ArchitecturalData['Rooms'], facilityId, 'P', PlumbingData['Name'], PlumbingData['urn'])

if __name__ == "__main__":
    uri = 'bolt://localhost:7687' # uri = "neo4j+s://38658833.databases.neo4j.io"
    user = 'neo4j'
    password = 'syyclops'     # password = "Z5vVAh9mzrpWxPrB3JrhHOPuVjnJAlWyu8pcAxDWrZQ"
    app = App(uri, user, password)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(app))
    app.close()