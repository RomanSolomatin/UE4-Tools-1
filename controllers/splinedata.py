import bpy
import csv

def dataspline(obj_select):
    data = [
        ['', 'XPos', 'YPos', 'ZPos', 'XInTangent', 'YInTangent', 'ZInTangent',
         'XOutTangent', 'YOutTangent', 'ZOutTangent'],
    ]

    name = obj_select.name
    outputfile = 'E:\\Users\\Desktop\\Splines\\' + name + '.csv'
    csvfile = csv.writer(open(outputfile, 'w'),
                         delimiter=',')

    # All point spline
    spline = obj_select.data.splines.active.bezier_points
    scale = 100


    for key in range(len(spline)):
        x_value = round(spline[key].co[0], 2)
        y_value = round(spline[key].co[1], 2) * -1
        z_value = round(spline[key].co[2], 2)

        xt_in = round(spline[key].handle_left[0], 2)
        yt_in = round(spline[key].handle_left[1] * -1, 2)
        zt_in = round(spline[key].handle_left[2], 2)

        xt_out = round(spline[key].handle_right[0], 2)
        yt_out = round(spline[key].handle_right[1] * -1, 2)
        zt_out = round(spline[key].handle_right[2], 2)

        data.append(['vert' + str(key),
                     x_value * scale, y_value * scale, z_value * scale,
                     xt_in * scale, yt_in * scale, zt_in * scale,
                     xt_out * scale, yt_out * scale, zt_out * scale
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