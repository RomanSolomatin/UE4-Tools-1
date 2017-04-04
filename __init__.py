import bpy
import mathutils

bl_info = {
    "name": "UE4 Tools",
    "description": "Various tools to make more easy the Game Art",
    # "description": "Creates a bounding cube object for each selected object from your Bouding Box, based on code from Jonatan Bijl",
    "author": "stilobique",
    "version": (0, 1, 0),
    "blender": (2, 7, 8),
    "location": "context menu",
    "category": "Object"}

def main(context, prefix):
    #make a list of the selected objects of type 'mesh'
    import bpy

    objs = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']
    generated_objs = []
    
    bpy.ops.object.select_all(action='DESELECT')
    
    for obj in objs:
        scale = obj.scale
        
        minx = obj.bound_box[0][0] * scale.x
        maxx = obj.bound_box[4][0] * scale.x
        miny = obj.bound_box[0][1] * scale.y
        maxy = obj.bound_box[2][1] * scale.y
        minz = obj.bound_box[0][2] * scale.z
        maxz = obj.bound_box[1][2] * scale.z
        dx = maxx - minx
        dy = maxy - miny
        dz = maxz - minz
    
        new_name = '{0}{1}'.format(prefix, obj.name)
        
        loc =  mathutils.Vector(((minx + 0.5* dx), (miny + 0.5* dy), (minz + 0.5* dz)))
        loc.rotate(obj.rotation_euler)
        loc = loc + obj.location
        
        bpy.ops.mesh.primitive_cube_add(location=loc, rotation=obj.rotation_euler)
        new_obj = bpy.context.object
        
        new_obj.name = new_name
        new_obj.dimensions = mathutils.Vector((dx, dy, dz))
        
        generated_objs.append(new_obj)
        
        new_obj.data.show_double_sided = False
    
    for obj in generated_objs:
        obj.select=True
        obj.draw_type = 'WIRE'


from bpy.props import StringProperty

class GenerateBoundingBoxesOperator(bpy.types.Operator):
    """Create a joined copy of selected meshes, with modifiers applied if needed"""
    bl_idname = "object.generate_bounding_boxes"
    bl_label = "Generate bounding box shapes for all selected objects"
    bl_options = {'REGISTER', 'UNDO'}

    name_prefix = StringProperty(name='name_prefix', description='The name prefix for the new objects', default='UCX_')
    @classmethod
    def poll(cls, context):
        return len(context.selected_objects) > 0

    def execute(self, context):
        main(context, self.name_prefix)
        return {'FINISHED'}

class UCXPanel(bpy.types.Panel): 
    bl_label = "GA Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "GA Tools"

    def draw(self, context):
        layout = self.layout

        layout.label(text="UCX")
        layout.operator("object.generate_bounding_boxes")


def register():
    bpy.utils.register_class(GenerateBoundingBoxesOperator)
    bpy.utils.register_class(UCXPanel)


def unregister():
    bpy.utils.unregister_class(GenerateBoundingBoxesOperator)
    bpy.utils.unregister_class(UCXPanel)


if __name__ == "__main__":
    register()