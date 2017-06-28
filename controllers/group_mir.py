import bpy


class MirorGroup(bpy.types.Operator):
    """Generate a new object with a miror"""
    bl_idname = "object.group_miror"
    bl_label = "Make a duplicate object with a miror"

    def execute(self, context):
        obj = context.object

        suffix = 'MIR '
        self.group_name = suffix + obj.name
        # Check the group already exist
        for value in bpy.data.groups.data.groups.values():
            name = value.name
            print(name)

            if self.group_name == value.name:
                print("This group already exist")
                bpy.ops.group.objects_add_active(group=value)
            else:
                print("Create a new group and add the oject selected")
                bpy.ops.group.create(name=self.group_name)
                bpy.ops.object.group_add(self.group_name)

        # bpy.ops.group.create(name=group_name)
        # bpy.ops.group.objects_add_active(group=group_name)
        # bpy.data.groups["Group"].name = group_name

        return {'FINISHED'}


def register():
    bpy.utils.register_class(MirorGroup)


def unregister():
    bpy.utils.unregister_class(MirorGroup)


if __name__ == "__main__":
    register()
