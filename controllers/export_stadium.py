import bpy

class ExportStadium(bpy.types.Operator):
    """Export all stadium element"""
    bl_idname = "object.export_stadium"
    bl_label = "Export all object present in layer actif"

    # All Variable


    def execute(self, context):
        visible_object = bpy.context.visible_objects

        for obj in visible_object:
            name = obj.name
            scn = context.scene

            bpy.ops.object.select_all(action='DESELECT')
            obj.select = True

            # Generate a path
            self.path_export = scn.conf_path
            path = self.path_export + name + ".fbx"

            bpy.ops.export_scene.fbx(filepath=path,
                                     version='BIN7400',
                                     use_selection=True,
                                     # object_types={'MESH'},
                                     use_mesh_modifiers=True,
                                     )

            print(path)

        return {'FINISHED'}


def register():
    bpy.utils.register_class(ExportStadium)


def unregister():
    bpy.utils.unregister_class(ExportStadium)


if __name__ == "__main__":
    register()
