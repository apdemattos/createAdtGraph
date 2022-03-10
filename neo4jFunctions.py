from distutils.command.build import build
from neo4j import GraphDatabase

class App:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        # Don't forget to close the driver connection when you are finished with it
        self.driver.close()

    def create_building(self, buildingId, modelId):
        with self.driver.session() as session: 
            result = session.write_transaction(self._create_and_return_building, buildingId, modelId)

            for row in result:
                print("Create Building: {}".format(row))

    @staticmethod
    def _create_and_return_building(tx, buildingId, modelId):
        query = (
            "CREATE (b1:" + modelId + " {name: $buildingId, id: $buildingId })"
            "RETURN b1 as name"
        )
        result = tx.run(query, buildingId=buildingId)
        return [row["name"] for row in result]

    def merge_building(self, buildingId, modelId, buildingName):
        with self.driver.session() as session: 
            result = session.write_transaction(self._merge_and_return_building, buildingId, modelId, buildingName)

            for row in result:
                print("Merge Building: {}".format(row))

    @staticmethod
    def _merge_and_return_building(tx, buildingId, modelId, buildingName):
        query = (
            "MERGE (building:" + modelId + " {id: $buildingId })"
            "ON CREATE set building.name = $buildingName "
            "RETURN building.name as name"
        )
        result = tx.run(query, buildingId=buildingId, buildingName = buildingName)
        return [row["name"] for row in result]

    def create_floor(self, floorId, floorName, modelId):
        with self.driver.session() as session: 
            result = session.write_transaction(self._create_and_return_floor, floorId, floorName, modelId)

            for row in result:
                print("Create Room: {}".format(row))

    @staticmethod
    def _create_and_return_floor(tx, floorId, floorName, modelId):
        query = (
            "CREATE (r:" + modelId + " {id: $floorId, name: $floorName })"
            "RETURN r.name as name"
        )
        result = tx.run(query, floorId=floorId, floorName=floorName)
        return [row["name"] for row in result]
    
    def merge_floor(self, floorId, floorName, modelId):
        with self.driver.session() as session: 
            result = session.write_transaction(self._merge_and_return_floor, floorId, floorName, modelId)

            for row in result:
                print("Merge Room: {}".format(row))

    @staticmethod
    def _merge_and_return_floor(tx, floorId, floorName, modelId):
        query = (
            "MERGE (r:" + modelId + " {id: $floorId})"
            "ON CREATE set r.name = $floorName "
            "RETURN r.name as name"
        )
        result = tx.run(query, floorId=floorId, floorName=floorName)
        return [row["name"] for row in result]

    def create_room(self, roomId, roomName, modelId, externalId):
        with self.driver.session() as session: 
            result = session.write_transaction(self._create_and_return_room, roomId, roomName, modelId, externalId)

            for row in result:
                print("Create Room: {}".format(row))

    @staticmethod
    def _create_and_return_room(tx, roomId, roomName, modelId, externalId):
        query = (
            "CREATE (r:" + modelId + " {id: $roomId, name: $roomName, externalId: $externalId })"
            "RETURN r.name as name"
        )
        result = tx.run(query, roomId=roomId, roomName=roomName, externalId=externalId)
        return [row["name"] for row in result]
    
    def merge_room(self, roomId, roomName, modelId, externalId):
        with self.driver.session() as session: 
            result = session.write_transaction(self._merge_and_return_room, roomId, roomName, modelId, externalId)

            for row in result:
                print("Merge Room: {}".format(row))

    @staticmethod
    def _merge_and_return_room(tx, roomId, roomName, modelId, externalId):
        query = (
            "Merge (r:" + modelId + " {externalId: $externalId})"
            "ON CREATE set r.id = $roomId, r.name = $roomName "
            "RETURN r.name as name"
        )
        result = tx.run(query, roomId=roomId, roomName=roomName, externalId=externalId)
        return [row["name"] for row in result]

    def create_room_isLocationOf_floor_rel(self, sourceId, targetId):
        with self.driver.session() as session: 
            result = session.write_transaction(self._create_and_return_room_isLocationOf_floor_rel, sourceId, targetId)

            for row in result:
                print("Created room is part of floor: {}".format(row))

    @staticmethod
    def _create_and_return_room_isLocationOf_floor_rel(tx, sourceId, targetId):
        query = (
            "Match (sR:Room {id: $sourceId})"
            "Match (tF:Floor {id: $targetId})"
            "Create (sR)-[r:isLocationOf]->(tF)"
            "RETURN sR, tF"
        )
        result = tx.run(query, sourceId=sourceId, targetId=targetId)
        return [row for row in result]
    
    def merge_room_isLocationOf_floor_rel(self, sourceId, targetId):
        with self.driver.session() as session: 
            result = session.write_transaction(self._merge_and_return_room_isLocationOf_floor_rel, sourceId, targetId)

            for row in result:
                print("Merge room is part of floor: {}".format(row))

    @staticmethod
    def _merge_and_return_room_isLocationOf_floor_rel(tx, sourceId, targetId):
        query = (
            "Match (sR:Room {id: $sourceId})"
            "Match (tF:Floor {id: $targetId})"
            "Merge (sR)-[r:isLocationOf]->(tF)"
            "RETURN sR, tF"
        )
        result = tx.run(query, sourceId=sourceId, targetId=targetId)
        return [row for row in result]

    def create_floor_locatedIn_building_rel(self, sourceId, targetId):
        with self.driver.session() as session: 
            result = session.write_transaction(self._create_and_return_floor_locatedIn_building_rel, sourceId, targetId)

            for row in result:
                print("Created Floor is located in of building: {}".format(row))

    @staticmethod
    def _create_and_return_floor_locatedIn_building_rel(tx, sourceId, targetId):
        query = (
            "Match (tF:Floor {id: $sourceId})"
            "Match (b:Building {id: $targetId})"
            "Create (tF)-[r:locatedIn]->(b)"
            "RETURN tF, b"
        )
        result = tx.run(query, sourceId=sourceId, targetId=targetId)
        return [row for row in result]
    
    def merge_floor_locatedIn_building_rel(self, sourceId, targetId):
        with self.driver.session() as session: 
            result = session.write_transaction(self._merge_and_return_floor_locatedIn_building_rel, sourceId, targetId)

            for row in result:
                print("Merged Floor is located in of building: {}".format(row))

    @staticmethod
    def _merge_and_return_floor_locatedIn_building_rel(tx, sourceId, targetId):
        query = (
            "Match (tF:Floor {id: $sourceId})"
            "Match (b:Building {id: $targetId})"
            "Merge (tF)-[r:locatedIn]->(b)"
            "RETURN tF, b"
        )
        result = tx.run(query, sourceId=sourceId, targetId=targetId)
        return [row for row in result]
    
    def create_asset(self, assetId, assetName, assetLabel, externalId):
        with self.driver.session() as session: 
            result = session.write_transaction(self._create_and_return_asset, assetId, assetName, assetLabel, externalId)

            for row in result:
                print("Create Asset: {}".format(row))

    @staticmethod
    def _create_and_return_asset(tx, assetId, assetName, assetLabel, externalId):
        query = (
            "CREATE (r:" + assetLabel + " {id: $assetId, name: $assetName, externalId: $externalId })"
            "RETURN r.name as name"
        )
        result = tx.run(query, assetId=assetId, assetName=assetName, externalId=externalId)
        return [row["name"] for row in result]
    
    def merge_asset(self, assetId, assetName, assetLabel, externalId):
        with self.driver.session() as session: 
            result = session.write_transaction(self._merge_and_return_asset, assetId, assetName, assetLabel, externalId)

            for row in result:
                print("Create Asset: {}".format(row))

    @staticmethod
    def _merge_and_return_asset(tx, assetId, assetName, assetLabel, externalId):
        query = (
            "MERGE (a:" + assetLabel + " {id: $assetId }) "
            "ON CREATE set a.externalId = $externalId, a.name = $assetName "
            "RETURN a.name as name"
        )
        result = tx.run(query, assetId=assetId, assetName=assetName, externalId=externalId)
        return [row["name"] for row in result]
    

    def create_system(self, systemId, systemName, modelId):
        with self.driver.session() as session: 
            result = session.write_transaction(self._create_and_return_system, systemId, systemName, modelId)

            for row in result:
                print("Create System: {}".format(row))

    @staticmethod
    def _create_and_return_system(tx, systemId, systemName, modelId):
        query = (
            "CREATE (r: " + modelId + "{id: $systemId, name: $systemName })"
            "RETURN r.name as name"
        )
        result = tx.run(query, systemId=systemId, systemName=systemName)
        return [row["name"] for row in result]
    
    def merge_system(self, systemId, systemName, modelId):
        with self.driver.session() as session: 
            result = session.write_transaction(self._merge_and_return_system, systemId, systemName, modelId)

            for row in result:
                print("Merge System: {}".format(row))

    @staticmethod
    def _merge_and_return_system(tx, systemId, systemName, modelId):
        query = (
            "MERGE (s: " + modelId + "{id: $systemId}) "
            "On create set s.name = $systemName "
            "RETURN s.name as name"
        )
        result = tx.run(query, systemId=systemId, systemName=systemName)
        return [row["name"] for row in result]

    def create_asset_includedIn_system_rel(self, sourceId, targetId):
        with self.driver.session() as session: 
            result = session.write_transaction(self._create_and_return_asset_includedIn_system_rel, sourceId, targetId)

            for row in result:
                print("Created Asset included in system: {}".format(row))

    @staticmethod
    def _create_and_return_asset_includedIn_system_rel(tx, sourceId, targetId):
        query = (
            "Match (a:Asset {id: $sourceId})"
            "Match (s:System {id: $targetId})"
            "Create (a)-[r:includedIn]->(s)"
            "RETURN a, s"
        )
        result = tx.run(query, sourceId=sourceId, targetId=targetId)
        return [row for row in result]

    def merge_asset_includedIn_system_rel(self, sourceId, targetId):
        with self.driver.session() as session: 
            result = session.write_transaction(self._merge_and_return_asset_includedIn_system_rel, sourceId, targetId)

            for row in result:
                print("Merge Asset included in system: {}".format(row))

    @staticmethod
    def _merge_and_return_asset_includedIn_system_rel(tx, sourceId, targetId):
        query = (
            "Match (a:Asset {id: $sourceId})"
            "Match (s:System {id: $targetId})"
            "Merge (a)-[r:includedIn]->(s)"
            "RETURN a, s"
        )
        result = tx.run(query, sourceId=sourceId, targetId=targetId)
        return [row for row in result]

    def merge_asset_located_on_floor(self, assetId, floorId, floorName):
        with self.driver.session() as session: 
            result = session.write_transaction(self._merge_and_return_asset_located_on_floor, assetId, floorId, floorName)

            for row in result:
                print("Merge Asset located on Floor: {}".format(row))

    @staticmethod
    def _merge_and_return_asset_located_on_floor(tx, assetId, floorId, floorName):
        query = (
            "Match (a:Asset {id: $assetId}) "
            "Merge (f:Floor {id: $floorId}) "
            "On create set f.name = $floorName "
            "Merge (a)-[r:locatedOn]->(f) "
            "RETURN a, f"
        )
        result = tx.run(query, assetId=assetId, floorId=floorId, floorName=floorName)
        return [row for row in result]

    def merge_asset_part_of_building(self, assetId, buildingId):
        with self.driver.session() as session: 
            result = session.write_transaction(self._merge_and_return_asset_part_of_building, assetId, buildingId)

            for row in result:
                print("Merge Asset is part of building : {}".format(row))

    @staticmethod
    def _merge_and_return_asset_part_of_building(tx, assetId, buildingId):
        query = (
            "Match (a:Asset {id: $assetId}) "
            "Match (b:Building {id: $buildingId}) "
            "Merge (a)-[r:partOfBuilding]->(b) "
            "RETURN a, b"
        )
        result = tx.run(query, assetId=assetId, buildingId=buildingId)
        return [row for row in result]

    def merge_asset_from_revit_model(self, buildingId, assetId, modelName, modelUrn):
        with self.driver.session() as session: 
            result = session.write_transaction(self._merge_and_return_asset_from_revit_model, buildingId, assetId, modelName, modelUrn)

            for row in result:
                print("Merge Asset from revit model: {}".format(row))

    @staticmethod
    def _merge_and_return_asset_from_revit_model(tx, buildingId, assetId, modelName, modelUrn):
        query = (
            "Match (b:Building {id: $buildingId}) "
            "Match (a:Asset {id: $assetId}) "
            "Merge (m:RevitModel {id: $modelUrn, name: $modelName}) "
            "Merge (a)-[r:fromRevitModel]->(m) "
            "Merge (m)-[:revitModelOfBuilding]->(b)"
            "RETURN a, m"
        )
        result = tx.run(query, assetId=assetId, modelName=modelName, modelUrn=modelUrn, buildingId=buildingId)
        return [row for row in result]

    def merge_system_of_building(self, systemId, buildingId, modelUrn):
        with self.driver.session() as session: 
            result = session.write_transaction(self._merge_and_return_system_of_building, systemId, buildingId, modelUrn)

            for row in result:
                print("Merge System of Building: {}".format(row))

    @staticmethod
    def _merge_and_return_system_of_building(tx, systemId, buildingId, modelUrn):
        query = (
            "Match (b:Building {id: $buildingId}) "
            "Match (s:System {id: $systemId})"
            "Match (m:RevitModel {id: $modelUrn})"
            "Merge (s)-[:systemOfBuilding]->(b)"
            "Merge (s)-[:fromRevitModel]->(m)"
            "Return b, s"
            
        )
        result = tx.run(query, systemId=systemId, buildingId=buildingId, modelUrn=modelUrn)
        return [row for row in result]