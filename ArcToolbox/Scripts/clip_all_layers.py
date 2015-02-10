'''Clip all layers in the map to the specified polygon.
Adapted from Alex Tereshenkov, http://gis.stackexchange.com/a/111712/108
'''
import arcpy
arcpy.env.overwriteOutput = True

mxd = arcpy.GetParameterAsText(0)
clip_layer = arcpy.GetParameterAsText(1)
out_gdb = arcpy.GetParameterAsText(2)


if not mxd:
    mxd = arcpy.mapping.MapDocument("CURRENT")

for lyr in arcpy.mapping.ListLayers(mxd):
    arcpy.AddMessage(lyr)
    out_layer = os.path.join(out_gdb,lyr.name)
    arcpy.Clip_analysis(lyr,clip_layer,out_layer)

print arcpy.GetMessages()