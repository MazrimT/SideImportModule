import sys
from pathlib import Path
import importlib 

base_path = Path(__file__).parent

file = Path(__file__)



sys.path.append(f'{base_path}/subfolder')


task_id = "etl_set_variable"
#globals()[f'{task_id}'] = __import__('etl_set_variable')

globals()[f'{task_id}'] = importlib.import_module(task_id)

globals()[f'{task_id}'].main()
