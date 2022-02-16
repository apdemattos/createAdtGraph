import json
import sys
import xlsxwriter

# Model Tree Higharchy
instanceTree = open('./Revit_InstanceTree_Dunbar.json')
instanceTreeData = json.load(instanceTree)

# Mechanical Properties 
modelProperties = open('./Revit_Mechanical_Properties_Dunbar.json')
modelPropertiesData = json.load(modelProperties)

# Mechanical Coorindates
mechanicalModelCoordinates = open('./Revit_Mechanical_Coordinates_Dunbar.json')
mechanicalModelCoordinatesData = json.load(mechanicalModelCoordinates)

# Architectural Floors and Rooms
floorAndRooms = open('./Revit_Rooms_Dunbar.json')
floorAndRoomsData = json.load(floorAndRooms)

# ADT Model IDs
facilityModelId = 'dtmi:com:willowinc:Building;1'
floorModelId = 'dtmi:com:willowinc:Floor;1'
spaceModelId = 'dtmi:com:willowinc:Room;1'
mechanicalEquipmentModelId = 'dtmi:com:syyclops:MechanicalEquipment;1'
systemModelId = 'dtmi:com:willowinc:System;1'

# Map Revit Families to their corresponding DTDL Model
revitFamiliesToDtDlModel = {
    'Rectangular Duct': 'dtmi:com:willowinc:HVACRectangularDuct;1', 
    'Round Duct': 'dtmi:com:willowinc:HVACRoundDuct;1',
    'Pipe Types': 'dtmi:com:willowinc:Pipe;1',
    'Transition - Generic': 'dtmi:com:willowinc:PipeFitting;1',
    'Elbow - Generic': 'dtmi:com:willowinc:PipeFittingElbow;1',
    'Tee - Generic': 'dtmi:com:willowinc:PipeFittingTee;1',
    'Pipe Spud': 'dtmi:com:willowinc:PipeFitting;1',
    'Coupling - Generic': 'dtmi:com:willowinc:PipeFittingCoupling;1',
    'Climate Master - TS Series': 'dtmi:com:willowinc:AirHandlingUnit;1',
    'Krueger LMHS-HWC': 'dtmi:com:willowinc:VAVBoxReheat;1',
    'Krueger LMHS': 'dtmi:com:willowinc:VAVBox;1',
    'Cabinet Fan-BCF': 'dtmi:com:willowinc:HVACFan;1',
    'Unit Heater - Cabinet': 'dtmi:com:willowinc:UnitHeater;1',
    'Pool Unit': 'dtmi:com:willowinc:AirHandlingUnit;1',
    'AHU 1,3,7': 'dtmi:com:willowinc:AirHandlingUnit;1',
    'AHU': 'dtmi:com:willowinc:AirHandlingUnit;1',
    'BG Base Mounted Centrifugal Pump Series 1510-5': 'dtmi:com:willowinc:HVACPump;1',
    'Expansion Tank - Freestanding - Vertical': 'dtmi:com:willowinc:HVACTank;1',
    'BAC - Cooling Tower': 'dtmi:com:willowinc:CoolingTower;1',
    'Greenheck Sidewall Exhaust': 'dtmi:com:willowinc:ExhaustFan;1',
    'DOAS 1,2,8': 'dtmi:com:willowinc:DedicatedOutdoorAirSystem;1',
    'DOAS': 'dtmi:com:willowinc:DedicatedOutdoorAirSystem;1',
    'AHU 2,5': 'dtmi:com:willowinc:AirHandlingUnit;1',
    'Greenheck Rooftop Ventilator': 'dtmi:com:willowinc:ExhaustFan;1',
    'CaptiveAire Rooftop Ventilator': 'dtmi:com:willowinc:ExhaustFan;1',
    'RooftopVentilator 10,25': 'dtmi:com:willowinc:ExhaustFan;1',
    'RooftopVentilator': 'dtmi:com:willowinc:ExhaustFan;1',
    'MAU': 'dtmi:com:willowinc:MakeupAirUnit;1',
    'Horizontal FCU': 'dtmi:com:willowinc:FanCoilUnit;1',
    'Unit Heater': 'dtmi:com:willowinc:UnitHeater;1',
    'Refrigeration Unit': 'dtmi:com:willowinc:RefrigerationEquipment;1',
    'FCU Stair': 'dtmi:com:willowinc:FanCoilUnit;1',
    'Cabinet Fan-BDF': 'dtmi:com:willowinc:ReturnFan;1',
    'InlineTubeFan-Horiz': 'dtmi:com:willowinc:ReturnFan;1',
    'Chiller': 'dtmi:com:willowinc:Chiller;1',
    'Heat Exchanger': 'dtmi:com:willowinc:HeatExchanger;1',
    'WWHP': 'dtmi:com:willowinc:HVACPump;1',
    'FCU IT': 'dtmi:com:willowinc:FanCoilUnit;1',
    'BG Base Mounted Centrifugal Pump Series 1510-4': 'dtmi:com:willowinc:HVACPump;1',
    'Bio Tank': 'dtmi:com:willowinc:HVACTank;1',
    'BG_In-Line Mounted Pump_Series 80-1.5x1.5xX': 'dtmi:com:willowinc:HVACTank;1',
    'CeilingFan': 'dtmi:com:willowinc:CeilingFan;1',
    'BAS Panel': 'dtmi:com:willowinc:AccessControlPanel;1',
    'Bypass Feeder': 'dtmi:com:willowinc:Asset;1',
    'ACC': 'dtmi:com:willowinc:Asset;1'
}

componentsLocation = {}

adtGraph = { "digitalTwinsFileInfo": { "fileVersion": "1.0.0" },
  "digitalTwinsGraph": {"digitalTwins": [], "relationships": []}}

def createTypeComponentAndSystem():
    for Category in instanceTreeData['children']:
        if(Category['name'] == 'Mechanical Equipment' or Category['name'] == 'Ducts'):
            for Family in Category['children']: 
                # print(Family['name'])
                revitFamilyToDTDLModel = revitFamiliesToDtDlModel[Family['name']]                
                for Type in Family['children']:
                    for Component in Type['children']:

                        prop = [prop for prop in modelPropertiesData['data']['collection'] if prop['externalId'] == Component['externalId']]

                        # Get the location of the Component
                        coords = [coord for coord in mechanicalModelCoordinatesData if coord['ExtIdentifier'] == Component['externalId']]
                        # print(coords[0]['center'])
                        componentCenterPoint = coords[0]['center']
                        componentMinPoint = coords[0]['minCoordinates']
                        componentMaxPoint = coords[0]['maxCoordinates']

                        locations = []
                        for floor in floorAndRoomsData:
                            for room in floorAndRoomsData[floor]:
                                # print(room['_bounds'])
                                roomBox = room['_bounds']
                                if roomBox['min']['x'] < componentMinPoint['x'] and roomBox['min']['y'] < componentMinPoint['y'] and roomBox['min']['z'] < (componentMinPoint['z'] + 1):
                                    if roomBox['max']['x'] > componentMaxPoint['x'] and roomBox['max']['y'] > componentMaxPoint['y'] and roomBox['max']['z'] > componentMaxPoint['z']:
                                        # print('component in ' + room['_name'])
                                        locations.append(room['_name'])

                        componentsLocation[Component['name']] = locations
                        # print(componentsLocation)
                        

                        # type = Component['name']
                        # name = prop[0]['properties']['Identity Data']['Type Name']


                        # Type
                        # typeId = Family['name'].replace(" ", "")
                        # typeName = Family['name']

                        # adtGraph['digitalTwinsGraph']['digitalTwins'].append({"$dtId": typeId, "name": typeName, "$metadata": {"$model": typeModelId}})


                        # Component
                        componentDtId = Component['name'].replace(" ", "").replace("[", "-").replace("]", "").replace("/", "-")

                        adtGraph['digitalTwinsGraph']['digitalTwins'].append({"$dtId": componentDtId, "name": prop[0]['properties']['Identity Data']['Type Name'] if 'Type Name' in prop[0]['properties']['Identity Data'] else "TBD", "geometryViewerID": Component['externalId'], "$metadata": {"$model": revitFamilyToDTDLModel}})

                        # Systems
                        systems = prop[0]['properties']['Mechanical']['System Name'].split(",")

                        for system in systems:
                            if(system != ""):
                                systemId = system.replace(" ", "")
                                # System
                                adtGraph['digitalTwinsGraph']['digitalTwins'].append({"$dtId": systemId, "name": system, "$metadata": {"$model": systemModelId}})


                                # Component Is Part Of System
                                adtGraph['digitalTwinsGraph']['relationships'].append({"$relationshipId": "{}->isPartOf->{}".format(componentDtId, systemId), "$sourceId": componentDtId, "$targetId": systemId, "$relationshipName": "isPartOf"})
        

def createFloorsAndRooms(facilityDtId):
    for floor in floorAndRoomsData:
        # Create Floor
        floorId = floor.replace(" ", "")

        adtGraph['digitalTwinsGraph']['digitalTwins'].append({"$dtId": floorId, "name": floor, "$metadata": {"$model": floorModelId}})

        # Floor is Part Of Facility
        adtGraph['digitalTwinsGraph']['relationships'].append({"$relationshipId": "{}->isPartOf->{}".format(floorId, facilityDtId), "$sourceId": floorId, "$targetId": facilityDtId, "$relationshipName": "isPartOf"})


        for room in floorAndRoomsData[floor]:
            roomId = room["_name"].replace(" ", "").replace("[", "-").replace("]", "").replace('/', "-").replace('&', "-").replace("'", "")
            # Create Room
            adtGraph['digitalTwinsGraph']['digitalTwins'].append({"$dtId": roomId, "name": room["_name"].replace("'", "").split("[")[0], "geometryViewerID": room['_info']["externalId"], "$metadata": {"$model": spaceModelId}})

            # Room is part of floor
            adtGraph['digitalTwinsGraph']['relationships'].append({"$relationshipId": "{}->isPartOf->{}".format(roomId, floorId), "$sourceId": roomId, "$targetId": floorId, "$relationshipName": "isPartOf"})

    createTypeComponentAndSystem()
            

def main():
    facilityDtId = 'DunbarHS'

    # Create Facility Twin
    adtGraph['digitalTwinsGraph']['digitalTwins'].append({"$dtId": facilityDtId, "name": facilityDtId, "$metadata": {"$model": facilityModelId}})

    createFloorsAndRooms(facilityDtId)
    # createTypeComponentAndSystem()

    with open("adtGraph.json", "w") as outfile:
        json.dump(adtGraph, outfile)

if __name__ == "__main__":
    main()
