from typing import List, Any

def delete_from_list(list_to_clean: List, item_to_delete: Any) -> List:
    item_index = list_to_clean.index(item_to_delete)
    list_to_clean.pop(item_index)
    
    return list_to_clean