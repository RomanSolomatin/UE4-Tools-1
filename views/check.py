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
        obj = context.active_object

        if context.active_object is not None:
            layout.label(obj.name)

            # Check any point :
            # - Lightmap
            # - Material
            if context.active_object.type == 'MESH':
                text = "No Lightmap UV"
                icon = "ERROR"
                uvs = context.active_object.data.uv_layers
                if len(uvs) >= 2:
                    text = "UV Bad name"
                    if uvs[1] and uvs[1].name == 'UV Lightmap':
                        text = "Lightmap"
                        icon = "FILE_TICK"

                layout.label(text=text, icon=icon)

                text = "No Material"
                icon = "ERROR"
                if len(context.active_object.material_slots) >= 1:
                    if context.active_object.material_slots[0]:
                        text = "Material(s)"
                        icon = "FILE_TICK"
                layout.label(text=text, icon=icon)

            else:
                layout.label("This object can't be export")

        else:
            layout.label("No object selected")




def register():
    bpy.utils.register_class(CheckerObjectsPanel)


def unregister():
    bpy.utils.unregister_class(CheckerObjectsPanel)
