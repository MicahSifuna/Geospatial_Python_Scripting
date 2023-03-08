import os
import arcpy
import time
# arcpy.env.workspace = r"C:\Users\LOUIS\ASSIGNMENT_CODES\ke\kenyadata\kenyadata"
arcpy.env.overwriteOutput = True

folder = r"C:\Users\HP MICAH\Desktop\kenyadata\mainFolder"

output_DIR = r"C:\Users\HP MICAH\Desktop\kenyadata\mainFolder\roadclass"
working_roads = "projected_roads_embu.shp"

case_B = "ROADCLASS IN('B')"
case_J = "ROADCLASS IN('J')"
case_E = "ROADCLASS IN('E')"
case_D = "ROADCLASS IN('D')"
case_A = "ROADCLASS IN('A')"
case_K = "ROADCLASS IN('K')"
case_C = "ROADCLASS IN('C')"
case_P = "ROADCLASS IN('P')"
case_M = "ROADCLASS IN('M')"
case_G = "ROADCLASS IN('G')"
case_L = "ROADCLASS IN('L')"
case_F = "ROADCLASS IN('F')"

cases = {
         "ROAD_CLASS_B":case_B,
         "ROAD_CLASS_J":case_J,
         "ROAD_CLASS_E": case_E,
         "ROAD_CLASS_D":case_D,
         "ROAD_CLASS_A":case_A,
         "ROAD_CLASS_K":case_K,
         "ROAD_CLASS_C":case_C,
         "ROAD_CLASS_P":case_P,
         "ROAD_CLASS_M":case_M,
         "ROAD_CLASS_G":case_G,
         "ROAD_CLASS_L":case_L,
         "ROAD_CLASS_F":case_F,
}

if os.path.exists(folder):
    # init output folder
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
    print "Please Connect to your main folder!"

# sleep for five seconds then calculate the total lengths
print "Sleeping for 5 secs"
time.sleep(5)
print "Finished sleeping, now proceeding..."
# Calculating total lengths for each

if os.path.exists(output_DIR):
    arcpy.env.workspace = output_DIR
    shapefiles = arcpy.ListFeatureClasses("*.shp")
    print "Printing Total length for Road Class Roads!"
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