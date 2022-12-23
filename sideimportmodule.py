import sys
from pathlib import Path
import importlib 


def special_import(module_to_import):
""" Imports a python package same as doing "import x" 
    makes it possible to import names from a list or making the package names dynamically

    Args:
      module_to_import(str): name of the python module in pypi
"""
    # for some reason the file path needs to be in sys.path for this to work 
    base_path = Path(__file__).parent
    sys.path.append(base_path)

    # import the module
    globals()[f'{module_to_import}'] = importlib.import_module(module_to_import)
    globals()[f'{module_to_import}'].main()
