import bpy
import bmesh
import sys
import subprocess

# This is a counter to help make unique files
fileIteration = 0


def read_dimensions():
    dimensions = []
    file = open('dimensions.txt', 'r')
    for line in file:
        dimensions += line.strip().split('=')[1:]

    global fileIteration
    fileIteration = dimensions[3]

    draw_simple_cube(dimensions)


def calculate_thickness(x, y, z):
    # return ((x * 0.025) + (y * 0.025) + (z * 0.025)) / 3
    return 0.07


def draw_simple_cube(dimensions):

    # Select the default Blender Cube
    bpy.data.objects['Cube'].select = True
    bpy.ops.object.mode_set(mode='OBJECT')
    # Delete the selected objects (default blender Cube)
    bpy.ops.object.delete()

    thickness = calculate_thickness(float(dimensions[0]), float(dimensions[1]), float(dimensions[2]))

    # Define vertices, faces, edges
    verts = [(-(float(dimensions[0]) / 2) + (thickness / 2), -float(dimensions[1]) / 2, -thickness / 2),  # 0
             (-(float(dimensions[0]) / 2) + (thickness / 2),  float(dimensions[1]) / 2, -thickness / 2),  # 1
             ( (float(dimensions[0]) / 2) - (thickness / 2),  float(dimensions[1]) / 2, -thickness / 2),  # 2
             ( (float(dimensions[0]) / 2) - (thickness / 2), -float(dimensions[1]) / 2, -thickness / 2),  # 3
             # (-float(dimensions[0]) / 2, -float(dimensions[1]) / 2,  thickness / 2),  # 4
             # (-float(dimensions[0]) / 2,  float(dimensions[1]) / 2,  thickness / 2),  # 5
             # ( float(dimensions[0]) / 2,  float(dimensions[1]) / 2,  thickness / 2),  # 6
             # ( float(dimensions[0]) / 2, -float(dimensions[1]) / 2,  thickness / 2)
            ]  # 7
    faces = [(0, 1, 2, 3)]

    # Define mesh and object
    mesh = bpy.data.meshes.new("Cube")
    object = bpy.data.objects.new("Cube", mesh)

    # Set location and scene of object
    object.location = bpy.context.scene.cursor_location
    bpy.context.scene.objects.link(object)

    # Create mesh
    mesh.from_pydata(verts, [], faces)
    mesh.update(calc_edges=True)

    bpy.data.objects["Cube"].select = True
    # Select the default Blender Cube
    bpy.context.scene.objects.active = bpy.context.scene.objects["Cube"]

    # thickness = calculate_thickness(float(dimensions[0]), float(dimensions[1]), float(dimensions[2]))

    bpy.ops.object.modifier_add(type="SOLIDIFY")
    bpy.data.objects["Cube"].modifiers["Solidify"].thickness = thickness
    bpy.data.objects["Cube"].modifiers["Solidify"].use_even_offset = True
    bpy.data.objects["Cube"].modifiers["Solidify"].offset = 0
    bpy.ops.object.mode_set(mode="OBJECT")
    bpy.ops.object.modifier_apply(apply_as="DATA", modifier="Solidify")


def save_object_creation():
    bpy.ops.wm.save_as_mainfile(filepath="C:\\Users\\Jayson\\Documents\\Quarters7-9\\9Capstone\\BlendFiles\\BoxLid" + str(fileIteration) + ".blend")


def generate_stl():
    bpy.ops.export_mesh.stl(filepath='C:\\Users\\Jayson\\Documents\\Quarters7-9\\9Capstone\\STLFiles\\BoxLid' + str(fileIteration) + '.stl')


def scratch_cube_creation():
    read_dimensions()


def register():
    scratch_cube_creation()
    save_object_creation()
    generate_stl()


if __name__ == "__main__":
    register()