import os
import sys
##This must be the path to your python site-packages folder
##Easy gui is necessary to select a folder, however this could be bypassed by just
##specifying the system path to the folder with speeches in
sys.path.append("C:\Users\matt's laptop\AppData\Local\Programs\Python\Python37\Lib\site-packages")
from os import listdir
from os import path
from os.path import isfile, join
import easygui

assetTools = unreal.AssetToolsHelpers.get_asset_tools()
materialEditor = unreal.MaterialEditingLibrary
assetEditor = unreal.EditorAssetLibrary
levelEditor = unreal.EditorLevelLibrary

def ImportSpeeches(SpeechFile, SpeechFolder):
    assetImportProperties = []
    assetImportTask = unreal.AssetImportTask()
    assetImportTask.set_editor_property('filename', file)
    assetImportTask.set_editor_property('destination_path', '/Game/Slides/Sounds')
    assetImportTask.set_editor_property('save', True)
    assetImportTask.set_editor_property('replace_existing', True)
    assetImportTask.set_editor_property('replace_existing_settings', True)
    assetImportTask.set_editor_property('automated', True)
    assetImportProperties.append(assetImportTask)
    (assetTools.import_asset_tasks(assetImportProperties))


speechFolder = (title = "Select Speech Folder")
filesAndFolders = listdir(speechFolder)
for f in filesAndFolders:
    if os.path.splitext(f)[1] == ".wav":
        ImportSpeeches(f, speechFolder)
