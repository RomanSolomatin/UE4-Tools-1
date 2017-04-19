import bpy


# -----------------------------------------------------------------------------
# Checker Object panel
# -----------------------------------------------------------------------------
class CheckerObjectsPanel(bpy.types.Panel):
    bl_label = "Checker Object"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "GA Tools"
    bl_context = "objectmode"


    def draw(self, context):
        layout = self.layout

        layout.label("Check all parameter for selected object")
        text = "Lightmap"
        icon = "FILE_TICK"
        layout.operator("object.check_lightmap", text=text, icon=icon)


def register():
    bpy.utils.register_class(CheckerObjectsPanel)


def unregister():
    bpy.utils.unregister_class(CheckerObjectsPanel)
