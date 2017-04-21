import bpy
import clipboard


class DataBuffer(bpy.types.Operator):
    """Insert a simple description"""
    bl_idname = "object.data_buffer"
    bl_label = "Paste information buffer"

    def execute(self, context):
        complete_command = """Begin Map
   Begin Level
      Begin Actor Class=StaticMeshActor Name=Box001 Archetype=StaticMeshActor'/Script/Engine.Default__StaticMeshActor'
         Begin Object Class=StaticMeshComponent Name=StaticMeshComponent0 ObjName=StaticMeshComponent0 Archetype=StaticMeshComponent'/Script/Engine.Default__StaticMeshActor:StaticMeshComponent0'
         End Object
         Begin Object Name=StaticMeshComponent0
            StaticMesh=StaticMesh'/Engine/EditorMeshes/EditorCube.EditorCube'
            RelativeLocation=(X=44.1928,Y=20.0976,Z=0.0)
            RelativeScale3D=(X=1.0,Y=1.0,Z=1.0)
            RelativeRotation=(Pitch=0.0,Yaw=0.0,Roll=0.0)
            CustomProperties
         End Object
         StaticMeshComponent=StaticMeshComponent0
         Components(0)=StaticMeshComponent0
         RootComponent=StaticMeshComponent0
         ActorLabel="Box001"
      End Actor
   End Level
Begin Surface
End Surface
End Map"""

        clipboard.copy(complete_command)

        return {'FINISHED'}


def register():
    bpy.utils.register_class(DataBuffer)


def unregister():
    bpy.utils.unregister_class(DataBuffer)


if __name__ == "__main__":
    register()



