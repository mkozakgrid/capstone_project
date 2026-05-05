from typing import Dict

def set_to_dict(dict_to_update: Dict[str, int], **items_to_set) -> Dict:
    for key, value in items_to_set.items():
        if value > dict_to_update[key]:
            dict_to_update[key] = value
    
    return dict_to_update