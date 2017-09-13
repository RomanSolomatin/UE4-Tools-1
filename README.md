# UE4-Tools
Tools to work with Unreal Engine on Blender

# Information
This tool need a dependency : `pyperclip`. You can find it on [Github](https://github.com/asweigart/pyperclip/). Paste the folder pyperclip inside the blender 
folder scripts/modules (create it if don't exist).
This folder on :
- **Windows** : %APPDATA%\Roaming\Blender Foundation\Blender\2
.79\scripts\modules
- **Mac** : *I don't know this OS*
- **Linux** : *I don't know this OS*

# UI
WIP

![Panel](https://github.com/stilobique/UE4-Tools/wiki/Ressources/Pannel.jpg)

## GA Tools
Any operator to make more simple any task. Generate a simple UCX mesh, batch
 lightmap... and more incoming.
 
## Export Batch
- Choose your path export and click "Exports all visible". This operator 
export only the static mesh.
- *Copy Data Buffer* : copy all position, rotation and scale for all 
selected object. Paste inside Unreal and replace the basic cube with your 
Static mesh.
- *Assets Elements* : Need more work.
- *Export Curve Data* : Export a CSV file to write your Curve inside a file.
 You can import it inside UE4 and used a blueprint to generate your Curve.


# More
Documentation available on Wiki page, WIP.