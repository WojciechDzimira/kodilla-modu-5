def dicts_to_object(library_list):
    """Konwertuje listę obiektów Film/Serial na listę słowników"""
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