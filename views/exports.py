import bpy


# -----------------------------------------------------------------------------
# Export Panel
# -----------------------------------------------------------------------------
class ClassPanel(bpy.types.Panel):
    bl_label = "Exports Batch"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "GA Tools"

    def draw(self, context):
        layout = self.layout

        layout.prop(context.scene, 'conf_path')
        text = "Exports all Visible"
        icon = "FILE_TICK"
        layout.operator("object.export_stadium", text=text, icon=icon)
        text = "Copy Data Buffer"
        icon = "COPYDOWN"
        layout.operator("object.data_buffer", text=text, icon=icon)
        text = "Assets Elements"
        icon = "MATCUBE"
        layout.operator("object.manage_assets", text=text, icon=icon)
        icon = 'CURVE_DATA'
        text = "Export Curve Data"
        layout.operator("object.spline_csv", text=text, icon=icon)


def register():
    bpy.utils.register_class(ClassPanel)
    bpy.types.Scene.conf_path = bpy.props.StringProperty \
        (
            name = "Root Path",
            default = "",
            subtype = 'DIR_PATH'
        )


def unregister():
    bpy.utils.unregister_class(ClassPanel)
    del bpy.types.Scene.conf_path


