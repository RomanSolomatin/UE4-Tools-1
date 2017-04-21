import bpy
import clipboard


class DataBuffer(bpy.types.Operator):
    """Insert a simple description"""
    bl_idname = "object.data_buffer"
    bl_label = "Paste information buffer"

    def execute(self, context):
        obj = context.active_object

        if obj is not None:
            string_data = \
'Begin Map \n' \
'   Begin Level \n'\
'       Begin Actor '\
        'Class=StaticMeshActor '\
        'Name=' + obj.name + ' ' \
        'Archetype=StaticMeshActor'\
        '\'/Script/Engine.Default__StaticMeshActor\'\n'\
'           Begin Object Class=StaticMeshComponent '\
            'Name=StaticMeshComponent0 '\
            'ObjName=StaticMeshComponent0 ' \
            'Archetype = StaticMeshComponent'\
            '\'/Script/Engine.Default__StaticMeshActor:StaticMeshComponent0' \
                             '\'\n'\
'           End Object\n'\
'           Begin Object '\
            'Name=StaticMeshComponent0 '\
            'StaticMesh=StaticMesh\'/Engine/EditorMeshes/EditorCube' \
                             '.EditorCube\' '\
            'RelativeLocation=(X=' + str(round(obj.location.x, 2)) + ',Y=' + \
str(round(obj.location.y, 2)) + ',Z=' + str(round(obj.location.z, 2)) + ')\n'\
            'RelativeScale3D=(X=1.0,Y=1.0,Z=1.0) '\
            'RelativeRotation=(Pitch=0.0,Yaw=0.0,Roll=0.0) '\
            'CustomProperties\n' \
'           End Object\n' \
'           StaticMeshComponent=StaticMeshComponent0\n' \
'           Components(0)=StaticMeshComponent0\n' \
'           RootComponent=StaticMeshComponent0\n' \
'           ActorLabel=' + obj.name + '\n' \
'       End Actor\n' \
'   End Level\n' \
'Begin Surface\n' \
'End Surface\n' \
'End Map'
            clipboard.copy(string_data)

        else:
            self.report({'WARNING'}, "Select an object(s).")

            return {'CANCELLED'}

        return {'FINISHED'}


def register():
    bpy.utils.register_class(DataBuffer)


def unregister():
    bpy.utils.unregister_class(DataBuffer)


if __name__ == "__main__":
    register()

#          Begin Object Name=StaticMeshComponent0
#             StaticMesh=StaticMesh'/Engine/EditorMeshes/EditorCube.EditorCube'
#             RelativeLocation=(X=44.1928,Y=20.0976,Z=0.0)
#             RelativeScale3D=(X=1.0,Y=1.0,Z=1.0)
#             RelativeRotation=(Pitch=0.0,Yaw=0.0,Roll=0.0)
#             CustomProperties
#          End Object
#          StaticMeshComponent=StaticMeshComponent0
#          Components(0)=StaticMeshComponent0
#          RootComponent=StaticMeshComponent0
#          ActorLabel="Box001"
#       End Actor
#    End Level
# Begin Surface
# End Surface
# End Map
