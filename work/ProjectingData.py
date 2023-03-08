import arcpy
arcpy.env.workspace = r"C:\Users\HP MICAH\Desktop\kenyadata"

inputShapefile = "KRBRoads.shp"
outputShapefile = "Projected_KRBRoads.shp"
outputCrs = arcpy.SpatialReference(21037) #arc 1960 UTM 37S
outputCrsCounties = arcpy.SpatialReference(4326) #UTM wgs 84
projectedKrbShp = "Projected_KRBRoads.shp"
countiesShp = "counties.shp"
outputCounties = "prj_counties.shp"


# # check the crs of counties shapefile
# desc = arcpy.Describe(countiesShp)
# spatialRef = desc.spatialReference.Name
# print "Before Projection: ", spatialRef

# reproject counties to UTM
arcpy.Project_management(countiesShp, outputCounties,outputCrsCounties)
desc2 = arcpy.Describe(outputCounties)
spatialRef = desc2.spatialReference.Name
print "After Projection: ", spatialRef


# clip Analysis

# clip  roads in embu
print "clipping roads in embu"
arcpy.Clip_analysis("KRBRoads.shp","embu.shp","embu_roads.shp")
print "Finished Clipping, going to next task!"







# from tabulate import tabulate
#
# table = [['First Name', 'Last Name', 'Age'],
#          ['John', 'Smith', 39],
#          ['Mary', 'Jane', 25],
#          ['Jennifer', 'Doe', 28]]
#
# print(tabulate(table))

