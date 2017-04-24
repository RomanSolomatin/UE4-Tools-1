import bpy
import clipboard
from math import degrees


class DataBuffer(bpy.types.Operator):
    """Export data Position, Rotation and Scale of all selected element"""
    bl_idname = "object.data_buffer"
    bl_label = "Paste information buffer"

    def execute(self, context):
        objs = context.selected_objects
        string_data_prefixe = 'Begin Map \n''   Begin Level \n'
        string_data_suffixe = '   End Level\n''Begin Surface\n''End ' \
                              'Surface\n''End Map'
        string_data = ""

        for element in objs:
            print(element.name)
            if element is not None:
                position_x = str(round(element.location.x * 100, 2))
                position_y = str(round(element.location.y * -100, 2))
                position_z = str(round(element.location.z * 100, 2))
                rotation_pitch = str(round(degrees(element.rotation_euler.x), 2))
                rotation_yaw = str(round(degrees(element.rotation_euler.y), 2))
                rotation_roll = str(round(degrees(element.rotation_euler.z), 2))
                string_data = string_data + \
    '      Begin Actor '\
            'Class=StaticMeshActor '\
            'Name=' + element.name + ' ' \
            'Archetype=StaticMeshActor'\
            '\'/Script/Engine.Default__StaticMeshActor\'\n'\
    '         Begin Object Class=StaticMeshComponent '\
                'Name=StaticMeshComponent0 '\
                'ObjName=StaticMeshComponent0 ' \
                'Archetype=StaticMeshComponent'\
                '\'/Script/Engine.Default__StaticMeshActor:StaticMeshComponent0' \
                                 '\'\n'\
    '         End Object\n'\
    '         Begin Object '\
                'Name=StaticMeshComponent0\n'\
    '            StaticMesh=StaticMesh\'/Engine/EditorMeshes/EditorCube' \
                                 '.EditorCube\' \n'\
    '            RelativeLocation=(X=' + position_x + ',Y=' + \
    position_y + ',Z=' + position_z + ')\n'\
    '            RelativeScale3D=(X=' + str(round(element.scale.x, 2)) + ',' \
                                                                     'Y=' + str(round(element.scale.y, 2)) + ',' \
                                                                      'Z=' + \
    str(round(element.scale.z, 2)) + ')\n'\
    '            RelativeRotation=(Pitch=' + rotation_pitch + ',Yaw=' + \
    rotation_yaw + ',' \
                                                              'Roll=' + \
    rotation_roll + ')\n'\
    '            CustomProperties\n' \
    '         End Object\n' \
    '         StaticMeshComponent=StaticMeshComponent0\n' \
    '         Components(0)=StaticMeshComponent0\n' \
    '         RootComponent=StaticMeshComponent0\n' \
    '         ActorLabel="' + element.name + '"\n' \
    '      End Actor\n' \

            else:
                self.report({'WARNING'}, "Select an object(s).")

                return {'CANCELLED'}

        string_complete = string_data_prefixe + string_data \
                          + string_data_suffixe
        clipboard.copy(string_complete)

        return {'FINISHED'}


def register():
    bpy.utils.register_class(DataBuffer)


def unregister():
    bpy.utils.unregister_class(DataBuffer)


if __name__ == "__main__":
    register()