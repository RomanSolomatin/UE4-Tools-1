import bpy


class UCXPanel(bpy.types.Panel):
    bl_label = "GA Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "GA Tools"

    def draw(self, context):
        layout = self.layout

        layout.label(text="UCX")
        layout.operator("object.generate_bounding_boxes")

        text = "Lightmap"
        layout.operator("uv.lightmap_generate", text=text)
        text = "Miror Group"
        layout.operator("object.group_miror", text=text)

def register():
    bpy.utils.register_class(UCXPanel)


def unregister():
    bpy.utils.unregister_class(UCXPanel)