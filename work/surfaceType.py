import os
import time

import arcpy

# arcpy.env.workspace = r"C:\Users\HP MICAH\Desktop\kenyadata"
arcpy.env.overwriteOutput = True
folder = r"C:\Users\HP MICAH\Desktop\kenyadata\mainFolder"

output_DIR = r"C:\Users\HP MICAH\Desktop\kenyadata\mainFolder\surfaceTypeOutputs"
working_roads = "projected_roads_embu.shp"


caseSurfaceDressing = "SurfType IN('Surface Dressing')"
caseSurfacePremix = "SurfType IN('Premix')"
caseSurfaceNatural = "SurfType IN('Natural')"
caseSurfaceSetstone = "SurfType IN('Set Stone')"
caseSurfaceSand = "SurfType IN('Sand')"
caseSurfaceEarth = "SurfType IN('Earth')"
caseSurfaceBrick = "SurfType IN('Brick')"
caseSurfaceGravel = "SurfType IN('Gravel')"

cases = {
     "Dressing":caseSurfaceDressing,
     "Premix":caseSurfacePremix,
     "Natural": caseSurfaceNatural,
     "SetStone":caseSurfaceSetstone,
     "Sand":caseSurfaceSand,
     "Earth":caseSurfaceEarth,
     "Brick":caseSurfaceBrick,
     "Gravel":caseSurfaceGravel
}

if os.path.exists(folder):
    # initialize output folder
    outFolder = output_DIR
    # set workspace folder
    arcpy.env.workspace = folder
    # loop through available shapefiles
    shapefiles = arcpy.ListFeatureClasses("*.shp")
    list_1 = []
    for shape in shapefiles:
        for key, value in cases.iteritems():
            name = key
            print "Selecting and exporting "+name+" roads..."
            arcpy.MakeFeatureLayer_management(shape,"layer")
            arcpy.SelectLayerByAttribute_management("layer","NEW_Selection",value)
            arcpy.FeatureClassToFeatureClass_conversion("layer",outFolder, name)
            print "Successfully exported "+name+ " roads.."
            print "#########################################################"

else:
    print "You should connect to the main folder!"

# sleep for five seconds then calculate the total lengths
print "Sleeping for 5 secs"
time.sleep(5)
print "Finished sleeping, now proceeding..."

# Calculating total lengths for each

if os.path.exists(output_DIR):
    arcpy.env.workspace = output_DIR
    shapefiles = arcpy.ListFeatureClasses("*.shp")
    print "Printing Total length for Road Surface Type!"
    for shape in shapefiles:
        try:
            ln_list = []
            rows = arcpy.SearchCursor(shape)
            for row in rows:
                LENGTH = row.getValue("length")
                ln_list.append(LENGTH)

            print shape + " Roads: \n Total Length is {0} KM".format(sum(ln_list))

        except Exception as e:
            print "Error: ",e
else:
    print "No such folder, please generate the shapefiles first!"





