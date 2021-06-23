"""
Util File
Contains small and independent functions
"""

import os
import json

def load_json_file(path_file: str) -> dict:
    """
    Loads given json file as a dictionary.
    
    Args:
        path_file [str]: path and name of json file to load.
    
    Return:
        [dict] with json file data.
    """
    
    
    if os.path.isfile(path_file):
        with open(path_file, 'r') as file:
            json_file = json.load(file)
        
        return json_file
    
        
    else:
        return None
    

def queue_add(list_queue: list, item) -> None:
    """
    Appends item to list as queue of set length.
    
    Args:
        queue [list]: queue object.
        item: any objecto to add to queue.
        
    Return: None
    """
    
    list_queue.append(item)
    list_queue.pop(0)
    