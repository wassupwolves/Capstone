import bpy
import bmesh
import sys
import subprocess

# Representation of all inserts, index 0 will contain the box insert
allInserts = []
fileIteration = 0


def read_dimensions():
    dimensions = []
    file = open('dimensions.txt', 'r')
    for line in file:
        dimensions += line.strip().split('=')[1:]
    fileIteration = dimensions[3]
    draw_simple_cube(dimensions)


def calculate_thickness(x, y, z):
    return ((x * 0.05) + (y * 0.05) + (z * 0.05)) / 3


def draw_simple_cube(dimensions):

    position_camera(float(dimensions[0]), float(dimensions[1]), float(dimensions[2]))

    bpy.data.objects['Cube'].select = True  # Select the default Blender Cube
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.delete()  # Delete the selected objects (default blender Cube)

    # Define vertices, faces, edges
    verts = [(-float(dimensions[0])/2, -float(dimensions[1])/2, -float(dimensions[2])/2),
             (-float(dimensions[0])/2, float(dimensions[1])/2, -float(dimensions[2])/2),
             (float(dimensions[0])/2, float(dimensions[1])/2, -float(dimensions[2])/2),
             (float(dimensions[0])/2, -float(dimensions[1])/2, -float(dimensions[2])/2  ),
             (-float(dimensions[0])/2, -float(dimensions[1])/2, float(dimensions[2])/2),
             (-float(dimensions[0])/2, float(dimensions[1])/2, float(dimensions[2])/2),
             (float(dimensions[0])/2, float(dimensions[1])/2, float(dimensions[2])/2),
             (float(dimensions[0])/2, -float(dimensions[1])/2, float(dimensions[2])/2)]
    faces = [(0, 1, 2, 3), (4, 5, 6, 7), (0, 4, 5, 1), (1, 5, 6, 2), (2, 6, 7, 3), (3, 7, 4, 0)]

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

    # Enter edit mode to delete top face
    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.mesh.normals_make_consistent(inside=False)

    bm = bmesh.from_edit_mesh(mesh)
    for face in bm.faces:
        face.select = False
    bm.faces[1].select = True

    bpy.ops.mesh.delete(type="FACE")

    thickness = calculate_thickness(float(dimensions[0]), float(dimensions[1]), float(dimensions[2]))

    # Enter "modifier mode" to give the faces thickness
    for face in bm.faces:
        face.select = True
    bpy.ops.object.modifier_add(type="SOLIDIFY")
    bpy.data.objects["Cube"].modifiers["Solidify"].thickness = thickness
    bpy.data.objects["Cube"].modifiers["Solidify"].use_even_offset = True
    bpy.ops.object.mode_set(mode="OBJECT")
    bpy.ops.object.modifier_apply(apply_as="DATA", modifier="Solidify")

    allInserts.insert(0, bm)
    # print(allInserts)

    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            area.spaces[0].region_3d.view_perspective = 'CAMERA'
    # bpy.ops.view3d.viewnumpad(type='CAMERA')


def position_camera(x, y, z):
    biggestside = x
    if y > x:
        biggestside = y
    if z > y and z > x:
        biggestside = z
    tx = biggestside * 2
    ty = -biggestside * 2
    tz = biggestside * 2

    rx = 54.0
    ry = 0.0
    rz = 45.0

    fov = 40.0

    pi = 3.14159265

    scene = bpy.data.scenes["Scene"]

    # Set render resolution
    scene.render.resolution_x = 480
    scene.render.resolution_y = 359

    # Set camera fov in degrees
    scene.camera.data.angle = fov * (pi / 180.0)

    # Set camera rotation in euler angles
    scene.camera.rotation_mode = 'XYZ'
    scene.camera.rotation_euler[0] = rx * (pi / 180.0)
    scene.camera.rotation_euler[1] = ry * (pi / 180.0)
    scene.camera.rotation_euler[2] = rz * (pi / 180.0)

    # Set camera translation
    scene.camera.location.x = tx
    scene.camera.location.y = ty
    scene.camera.location.z = tz


def save_object_creation():
    bpy.ops.wm.save_as_mainfile(filepath='boxinsert' + str(fileIteration) + '.blend')
    # bpy.ops.image.save_as(save_as_render=True, copy=True, filepath="//untitled.png", relative_path=True,
    #                       show_multiview=False, use_multiview=False)
    bpy.ops.render.render()
    bpy.data.images['Render Result'].save_render(filepath="C:\\Users\\Jayson\\Documents\\Quarters7-9\\9Capstone\\Stor3d\\insert.png")


def save_stlfile():
    lines = []
    file = open('readytoprint.txt', 'r')
    for line in file:
        lines += line
    readytoprint = bool(lines[0])
    if(readytoprint):
        generate_stl()


def generate_stl():
    pass


def scratch_cube_creation():
    read_dimensions()


def register():
    # bpy.utils.register_class(LayoutDemoPanel)
    scratch_cube_creation()
    save_object_creation()
    save_stlfile()


# def unregister():
#     bpy.utils.unregister_class(LayoutDemoPanel)


if __name__ == "__main__":
    register()