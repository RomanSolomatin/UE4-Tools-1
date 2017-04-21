import bpy


class ManageAssets(bpy.types.Operator):
    """Insert a simple description"""
    bl_idname = "object.manage_assets"
    bl_label = "Make the selected object as an Assets"


    def execute(self, context):
        slt_obj = context.active_object
        obj_name = slt_obj.name
        obj_data = bpy.data.objects
        parentname =  'assets_element'

        if bpy.data.objects.get(parentname) is None:
            bpy.ops.object.add(type='EMPTY')
            ob = context.active_object
            ob.name = parentname

            bpy.ops.object.select_all(action='DESELECT')

        # Make the empty as parent
        context.scene.objects.active = obj_data[obj_name]
        obj_data[obj_name].parent = obj_data[parentname]

        return {'FINISHED'}


def register():
    bpy.utils.register_class(ManageAssets)


def unregister():
    bpy.utils.unregister_class(ManageAssets)


if __name__ == "__main__":
    register()
