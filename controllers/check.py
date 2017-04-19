import bpy


class CheckLightmap(bpy.types.Operator):
    """Check if the selected object as a Lightmap"""
    bl_idname = "object.check_lightmap"
    bl_label = "This Operator check if the selected object have a lightmap " \
               "channel"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        slt_obj = context.selected_objects

        for obj in slt_obj:
            if obj.type == 'MESH':
                mesh = obj.data.name
                uvs = bpy.data.meshes[mesh].uv_layers

                if uvs:
                    if uvs[2]:
                        print('UV 2 exist')
                    elif uvs[1]:
                        print('UV 1 en fait')
                else:
                    print("pas de uv lol")

        return {'FINISHED'}


def register():
    bpy.utils.register_class(CheckLightmap)


def unregister():
    bpy.utils.unregister_class(CheckLightmap)


if __name__ == "__main__":
    register()
