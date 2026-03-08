def dicts_to_object():
    """Konwertuje listę słowników .json na listę obiektów Film/Serial"""
    result = []   
    for i, record in enumerate(library_list, start=1): 
        rekord_dict = {   
            "record_id" : i,            
            "type": "Film" if type(record) == Film else "Serial",  
            "title": record.title,
            "year": record.year,
            "genre": record.genre,
            "views": record.views_number,
        }
        if type(record) == Serial:
            rekord_dict["episode_number"] = record.episode_number
            rekord_dict["season_number"] = record.season_number
        
        result.append(rekord_dict) 
    
    return result  


 with open("biblioteka.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)