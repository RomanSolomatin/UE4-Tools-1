import bpy

class ExportScene(bpy.types.Operator):
    """Export all stadium element"""
    bl_idname = "object.export_stadium"
    bl_label = "Export all object present in layer actif"

    # All Variable


    def execute(self, context):
        visible_object = bpy.context.visible_objects

        for obj in visible_object:
            obj.name = obj.name.lower()
            name = obj.name
            scn = context.scene

            bpy.ops.object.select_all(action='DESELECT')

            if obj.type == 'MESH':
                obj.select = True

                # Generate a path
                self.path_export = scn.conf_path
                path = self.path_export + name + ".fbx"

                bpy.ops.export_scene.fbx(filepath=path,
                                         version='BIN7400',
                                         use_selection=True,
                                         object_types={'MESH'},
                                         use_mesh_modifiers=True,
                                         )

        return {'FINISHED'}


def register():
    bpy.utils.register_class(ExportScene)


def unregister():
    bpy.utils.unregister_class(ExportScene)


if __name__ == "__main__":
    register()
