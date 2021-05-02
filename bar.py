import os
import importlib
import config


def get_modules(path_to_modules):
    all_module = os.listdir(path_to_modules)

    try:
        all_module.remove('__init__.py')
        all_module.remove("__pycache__")
    except:
        pass

    return [f'modules.{module.replace(".py", "")}' for module in all_module]


def import_module(name):
    return importlib.import_module(name)


module_path = f'{os.path.realpath(__file__).replace("bar.py", "")}/modules'
all_module = get_modules(module_path)
modules_avalible = [module_avalible.split('.')[-1] for module_avalible in all_module]
imported_modules = []

bar_sep = " | "
bar_string = ""

for module in config.modules_use:
    if module in modules_avalible:
        module = f"{'.'.join(all_module[-1].split('.')[:-1])}.{module}"


    module_text = import_module(module).get_module_text()
    if module_text:
        bar_string += bar_sep + module_text + bar_sep


print(bar_string)
