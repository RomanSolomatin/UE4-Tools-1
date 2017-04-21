import bpy
import os

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
                folder = self.path_export
                file_extension = ".fbx"
                path = folder + name + file_extension

                # Add a new rule, assets objects (need to be center)
                if obj.parent.name == 'assets_element':
                    folder = self.path_export + "\\assets\\"
                    if not os.path.exists(folder):
                        os.makedirs(folder)

                    path = os.path.join(folder + name + file_extension)
                    # folder = dir(self.path_export + "assets")
                    # path = str(folder) + name + ".fbx"

                    print("This element as an assets :")
                    print(obj.name)
                    print("The path export as :")
                    print(path)

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
