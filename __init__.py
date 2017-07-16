import sys
import importlib

modulesNames = [
    # Models
    # 'models.paths',
    # Views
    'views.pie',
    'views.check',
    'views.exports',
    'views.various',
    # Controllers
    'controllers.check',
    'controllers.collision',
    'controllers.data_buffer',
    'controllers.export_scene',
    'controllers.group_mir',
    'controllers.lightmap',
    'controllers.manage',
    'controllers.splinedata',
    ]

modulesFullNames = []
for currentModule in modulesNames:
    modulesFullNames.append('{}.{}'.format(__name__, currentModule))

for currentModule in modulesFullNames:
    if currentModule in sys.modules:
        importlib.reload(sys.modules[currentModule])
    else:
        globals()[currentModule] = importlib.import_module(currentModule)

bl_info = {
    "name": "UE4 Tools",
    "description": "Various tools to make more easy the Game Art",
    "author": "stilobique",
    "version": (0, 2, 0),
    "blender": (2, 7, 8),
    "location": "context menu",
    "category": "Object"}


def register():
    # Add all class present in this addon
    for module in modulesFullNames:
        if module in sys.modules:
            if hasattr(sys.modules[module], 'register'):
                sys.modules[module].register()


def unregister():
    for module in modulesFullNames:
        if module in sys.modules:
            if hasattr(sys.modules[module], 'unregister'):
                sys.modules[module].unregister()


if __name__ == "__main__":
    register()
