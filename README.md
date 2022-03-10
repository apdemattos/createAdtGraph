# Revit to Neo4j Translator 

## How to run 

1. Start the Syyclops Api locally. In httpRequests.py enter username and password for syyclops in the oathLogin function
2. In createBuildingGraph.py find the __main__ function at the bottom and insert the neo4j url, user, and password
3. Get all model urn's for a building 
4. Run with: 

```
python3 createBuildingGraph.py --buildingId "DunbarDC2022" --buildingName "Dunbar HS" --roomsPath ./Dunbar/Architectural/Dunbar_Architectural_RoomLevelMap.json 
        --archUrn dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6ZHVuYmFycmV2aXRfMTEyNi9BcmNoaXRlY3R1cmFsX1VwZGF0ZWQucnZ0 
        --mechUrn dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6ZHVuYmFycmV2aXRfMTEyNi9NZWNoYW5pY2FsLnJ2dA 
        --elecUrn dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6ZHVuYmFycmV2aXRfMTEyNi9FbGVjdHJpY2FsLnJ2dA 
        --plumbUrn dXJuOmFkc2sub2JqZWN0czpvcy5vYmplY3Q6ZHVuYmFycmV2aXRfMTEyNi9QbHVtYmluZy5ydnQ
```
