import os
import sys
##This must be the path to your python site-packages folder
##Easy gui is necessary to select a file from a folder, however this could be bypassed by just
##specifying the system path to the folder with Powerpoint images in
sys.path.append("C:\Users\matt's laptop\AppData\Local\Programs\Python\Python37\Lib\site-packages")
from os import listdir
from os import path
from os.path import isfile, join
import easygui

assetTools = unreal.AssetToolsHelpers.get_asset_tools()
materialEditor = unreal.MaterialEditingLibrary
assetEditor = unreal.EditorAssetLibrary
levelEditor = unreal.EditorLevelLibrary

##Functions to import IMG files, create textures and materials using the images, ready to be applied to
##a static mesh
    
def createTexture(imageFile, imageFolder):
    file = join(imageFolder, f)
    assetImportProperties = []
    assetImportTask = unreal.AssetImportTask()
    assetImportTask.set_editor_property('filename', file)
    assetImportTask.set_editor_property('destination_path', '/Game/Slides/Textures')
    assetImportTask.set_editor_property('save', True)
    assetImportTask.set_editor_property('replace_existing', True)
    assetImportTask.set_editor_property('replace_existing_settings', True)
    assetImportTask.set_editor_property('automated', True)
    assetImportProperties.append(assetImportTask)
    return str(assetTools.import_asset_tasks(assetImportProperties))
    

def createMaterial(f):
    materialName = f[:-4] + "_Mat"
    path = "/Game/Slides/Materials"
    existPath = path + "/" + materialName
    if assetEditor.does_asset_exist(existPath) != True:
        new_material = assetTools.create_asset(materialName, path, unreal.Material, unreal.MaterialFactoryNew())
        return new_material
    else:
        new_material = assetEditor.load_asset(path + "/" + materialName)
        return new_material

def applyTexture(file, material):
    textureNode = materialEditor.create_material_expression(material, unreal.MaterialExpressionTextureSample, -400, -100)
    path = "/Game/Slides/Textures/" + file[:-4] + "." + file[:-4]
    texture = unreal.load_asset(path)
    textureNode.set_editor_property("texture", texture)
    materialEditor.connect_material_property(textureNode, "RGBA", unreal.MaterialProperty.MP_BASE_COLOR)

    roughnessNode = materialEditor.create_material_expression(material, unreal.MaterialExpressionConstant, -400, -300)
    roughnessNode.set_editor_property("R", 0.25)
    materialEditor.connect_material_property(roughnessNode, "", unreal.MaterialProperty.MP_ROUGHNESS)

##def createCube():
##    actor = levelEditor.spawn_actor_from_class(unreal.StaticMeshActor.static_class(), unreal.Vector(0, 0, 100), unreal.Rotator(0, 0, 0))
##    actor.set_actor_label(actor)
##    component = actor.get_component_by_class(unreal.StaticMeshComponent.static_class())
##    component.set_static_mesh(assetEditor.load_asset("/Engine/BasicShapes/Cube.Cube"))
##    component.set_editor_property("relative_scale3d", unreal.Vector(0.1, 1.28, 0.

imageFolder = easygui.diropenbox(title = "Select image folder")
filesAndFolders = listdir(imageFolder)
for f in filesAndFolders:
    if os.path.splitext(f)[1] == ".png":
        imageTexture = createTexture(f, imageFolder)
        material = createMaterial(f)
        applyTexture(f, material)

