import arcpy
arcpy.env.workspace = r"C:\Users\HP MICAH\Desktop\kenyadata"

KRBRoads = r"C:\Users\HP MICAH\Desktop\kenyadata\KRBRoads.shp"
# mycount = arcpy.GetCount_management("parks.shp")

roadDictionary = {}
totalLength = 0
total = 0

with arcpy.da.SearchCursor(KRBRoads, ["SurfType", "Length"]) as cursor:
    for row in cursor:
        # row =>  ('surface dressing','0.987666')
        road_type = row[0]
        length = row[1]

        if road_type not in roadDictionary.keys():
            roadDictionary[road_type] = length

        totalLength += length
        total += 1
    print "Total_Length of Roads in KM: ", totalLength, "Total Roads in Kenya: ", total
    # print total_length, " KM"
    print "Total Length per Road: ", roadDictionary
    #
    total_value = 0
    for key, value in roadDictionary.items():
        total_value += value
        print key, value
    print "Total Sum: ", total_value



