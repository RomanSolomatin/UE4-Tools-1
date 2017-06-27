import bpy


class LightmapGenerate(bpy.types.Operator):
    """Generate a news UV map and rename it Lightmap"""
    bl_idname = "uv.lightmap_generate"
    bl_label = "Make a lightmap channel"

    def execute(self, context):
        bpy.ops.mesh.uv_texture_add()
        bpy.context.object.data.uv_textures["UVMap.001"].name = "UV Lightmap"

        return {'FINISHED'}


def register():
    bpy.utils.register_class(LightmapGenerate)


def unregister():
    bpy.utils.unregister_class(LightmapGenerate)


if __name__ == "__main__":
    register()
