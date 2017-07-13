import bpy
import csv

def dataspline(obj_select):
    data = [
        ['', 'XPos', 'YPos', 'ZPos', 'XInTangent', 'YInTangent', 'ZInTangent',
         'XOutTangent', 'YOutTangent', 'ZOutTangent'],
    ]

    outputfile = r'E:\Users\Desktop\Splines\blender_spline.csv'
    csvfile = csv.writer(open(outputfile, 'w'),
                         delimiter=',')

    # All point spline
    spline = obj_select.data.splines.active.bezier_points
    scale = 100


    for key in range(len(spline)):
        print('index', key) # Point Coordinate
        print('Name > ', 'vert' + str(key),
              'XPos > ', round(spline[key].co[0], 4),
              'YPos > ', round(spline[key].co[1], 4),
              'ZPos > ', round(spline[key].co[2], 4),
              'XInTangent > ', round(spline[key].handle_left[0], 4),
              'YInTangent > ', round(spline[key].handle_left[1], 4),
              'ZInTangent > ', round(spline[key].handle_left[2], 4),
              'XOutTangent > ', round(spline[key].handle_right[0], 4),
              'YOutTangent > ', round(spline[key].handle_left[1], 4),
              'ZOutTangent > ', round(spline[key].handle_left[2], 4))

        data.append(['vert' + str(key),
                     round(spline[key].co[0], 4) * scale,
                     round(spline[key].co[1], 4) * scale,
                     round(spline[key].co[2], 4) * scale,
                     round(spline[key].handle_left[0], 4) * scale,
                     round(spline[key].handle_left[1], 4) * scale * -1,
                     round(spline[key].handle_left[2], 4) * scale,
                     round(spline[key].handle_right[0], 4) * scale,
                     round(spline[key].handle_right[1], 4) * scale * -1,
                     round(spline[key].handle_right[2], 4) * scale
                    ])

    for value in data:
        csvfile.writerow(value)

class SplineCSV(bpy.types.Operator):
    """Create a database for a spline object"""
    bl_idname = "object.spline_csv"
    bl_label = "Database Spline CSV"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and \
               context.active_object.type == 'CURVE'

    def execute(self, context):
        ob = context.object

        dataspline(ob)

        return {'FINISHED'}


def register():
    bpy.utils.register_class(SplineCSV)


def unregister():
    bpy.utils.unregister_class(SplineCSV)


if __name__ == "__main__":
    register()