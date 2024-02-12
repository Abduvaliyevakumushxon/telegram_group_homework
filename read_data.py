import json

def read_data(file_path: str)->dict:
    """
    Get the total number of messages.

    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        int: Total number of messages.
    
    """
    f=open(file_path , encoding='utf-8').read()
    return json.loads(f)['messages']
