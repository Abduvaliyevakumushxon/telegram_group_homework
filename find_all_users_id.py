from read_data import read_data

def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    s=[]
    for i in data:
        if i.get('actor_id')==None:
            if i['from_id'] not in s:
                s.append(i['from_id'])
        else:
            if i['actor_id'] not in s:
                s.append(i['actor_id'])
    return s
print(find_all_users_id(read_data('data/result.json')))