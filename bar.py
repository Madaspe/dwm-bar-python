import os
import importlib


def get_modules(path_to_modules):
    all_module = os.listdir(path_to_modules)

    try:
        all_module.remove('__init__.py')
        all_module.remove("__pycache__")
    except:
        pass

    return [f'{path_to_modules.replace("/", ".")}.{module.replace(".py", "")}' for module in all_module]


def import_module(name):
    return importlib.import_module(name)


module_path = 'modules'
all_module = get_modules(module_path)
imported_modules = []

bar_sep = " | "
bar_string = ""

for module in all_module:
    module_text = import_module(module).get_module_text()
    if module_text:
        bar_string += bar_sep + module_text + bar_sep

print(bar_string)