import bpy

from bpy.props import StringProperty

# ----------------------------------------------------------------------------
# Model to define all path and settings :
#  -> Substance Software Path
#  -> Temporary Folder
# ----------------------------------------------------------------------------
class PathExport(bpy.types.PropertyGroup):
    path_export = StringProperty(
        name="Path Export",
        default="",
        description = "Choose where you want export your file",
        subtype="DIR_PATH",
            )


# def register():
    # bpy.utils.register_class(PathExport)
    # bpy.types.Scene.ue4_export = bpy.props.StringProperty(type='PathExport')


# def unregister():
    # bpy.utils.unregister_class(PathExport)
    # del bpy.types.Scene.ue4_export
