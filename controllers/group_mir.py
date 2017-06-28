import bpy
import math


class MirorGroup(bpy.types.Operator):
    """Generate a new object with a miror"""
    bl_idname = "object.group_miror"
    bl_label = "Make a duplicate object with a miror"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and \
               context.active_object.type == 'MESH'

    def execute(self, context):
        obj = context.object

        grp_name = 'MIR ' + obj.name
        dupli = bpy.data.groups.find(grp_name)

        if dupli == -1:
            print("Ce group n'est pas present, generate all data")
            print("Group Name >> ", grp_name)
            bpy.ops.group.create(name=grp_name)
            bpy.ops.group.objects_add_active(group=grp_name)
        else:
            print("Groupe deja present, asign it !")
            bpy.ops.group.objects_add_active(group=grp_name)

        # Generate all Duplication
        bpy.ops.object.group_instance_add(group=grp_name,
                                          rotation=(0, 0, 0))
        obj = bpy.context.object
        bpy.data.objects.get(obj.name).select = True
        bpy.ops.transform.resize(value=(-1, 1, 1))


        bpy.ops.object.group_instance_add(group=grp_name,
                                          rotation=(0, 0, math.radians(180)))
        obj = bpy.context.object
        bpy.data.objects.get(obj.name).select = True
        bpy.ops.object.group_instance_add(group=grp_name,
                                          rotation=(0, 0, 0))
        obj = bpy.context.object
        bpy.data.objects.get(obj.name).select = True
        bpy.ops.transform.resize(value=(1, -1, 1))
        return {'FINISHED'}


def register():
    bpy.utils.register_class(MirorGroup)


def unregister():
    bpy.utils.unregister_class(MirorGroup)


if __name__ == "__main__":
    register()
