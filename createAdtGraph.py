import json
import sys
from tkinter import N
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
facilityModelId = 'dtmi:com:syyclops:Facility;1'
floorModelId = 'dtmi:com:syyclops:Floor;1'
spaceModelId = 'dtmi:com:syyclops:Space;1'
mechanicalEquipmentModelId = 'dtmi:com:syyclops:MechanicalEquipment;1'
ductModelId = 'dtmi:com:syyclops:Duct;1'
systemModelId = 'dtmi:com:syyclops:System;1'
typeModelId = 'dtmi:com:syyclops:Type;1'

componentsLocation = {}

adtGraph = { "digitalTwinsFileInfo": { "fileVersion": "1.0.0" },
  "digitalTwinsGraph": {"digitalTwins": [], "relationships": []}}

def createTypeComponentAndSystem():
    for Category in instanceTreeData['children']:
        if(Category['name'] == 'Mechanical Equipment'):
            for Family in Category['children']: 
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
                        

                        type = Component['name']
                        # name = prop[0]['properties']['Identity Data']['Type Name']
                        systems = prop[0]['properties']['Mechanical']['System Name'].split(",")


                        # Type
                        typeId = Family['name'].replace(" ", "")
                        typeName = Family['name']

                        adtGraph['digitalTwinsGraph']['digitalTwins'].append({"$dtId": typeId, "name": typeName, "$metadata": {"$model": typeModelId}})


                        # Component
                        componentDtId = Component['name'].replace(" ", "").replace("[", "-").replace("]", "").replace("/", "-")

                        adtGraph['digitalTwinsGraph']['digitalTwins'].append({"$dtId": componentDtId, "name": prop[0]['properties']['Identity Data']['Type Name'] if 'Type Name' in prop[0]['properties']['Identity Data'] else "TBD", "ExtIdentifier": Component['externalId'], "$metadata": {"$model": mechanicalEquipmentModelId}})


                        for system in systems:
                            if(system != ""):
                                systemId = system.replace(" ", "")
                                # System
                                adtGraph['digitalTwinsGraph']['digitalTwins'].append({"$dtId": systemId, "name": system, "$metadata": {"$model": systemModelId}})


                                # Component Is Part Of System
                                adtGraph['digitalTwinsGraph']['relationships'].append({"$relationshipId": "{}->isPartOf->{}".format(componentDtId, systemId), "$sourceId": componentDtId, "$targetId": systemId, "$relationshipName": "isPartOf"})


                        # Component Is Of Type
                        adtGraph['digitalTwinsGraph']['relationships'].append({"$relationshipId": "{}->isPartOf->{}".format(componentDtId, typeId), "$sourceId": componentDtId, "$targetId": typeId, "$relationshipName": "isOfType"})
        

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
            adtGraph['digitalTwinsGraph']['digitalTwins'].append({"$dtId": roomId, "name": room["_name"].replace("'", "").split("[")[0], "ExtIdentifier": room['_info']["externalId"], "$metadata": {"$model": spaceModelId}})

            # Room is part of floor
            adtGraph['digitalTwinsGraph']['relationships'].append({"$relationshipId": "{}->isPartOf->{}".format(roomId, floorId), "$sourceId": roomId, "$targetId": floorId, "$relationshipName": "isPartOf"})


    createTypeComponentAndSystem()
            

def main():
    facilityDtId = 'DunbarHS'

    # Create Facility Twin
    adtGraph['digitalTwinsGraph']['digitalTwins'].append({"$dtId": facilityDtId, "name": facilityDtId, "$metadata": {"$model": facilityModelId}})

    createFloorsAndRooms(facilityDtId)


    with open("adtGraph.json", "w") as outfile:
        json.dump(adtGraph, outfile)

if __name__ == "__main__":
    main()
