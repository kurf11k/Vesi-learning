import inspect

def load(class_type, path_to_file, splitter=";"):
    list = []
    with open(path_to_file, mode="r", encoding="utf-8") as file:
        for line in file:
            attrs = line.split(splitter)
            attrs[-1] = attrs[-1].replace("\n", "")
            new_obj = class_type(*attrs)   
            list.append(new_obj)
    return list

def append(obj, path_to_file, splitter=";"):
    with open(path_to_file, mode="a", encoding="utf-8") as file:
        file.write(_convert_obj_to_str(obj, splitter))

def rewrite(list, path_to_file, splitter=";"):
    with open(path_to_file, mode="w", encoding="utf-8") as file:
        for obj in list:
            file.write(_convert_obj_to_str(obj, splitter))

def _convert_obj_to_str(obj, splitter):
    constructor = inspect.signature(type(obj).__init__)
    obj_to_save = ""
    obj = obj.__dict__
    
    for i, p in enumerate(constructor.parameters):
        if i == 1:
            obj_to_save += str(obj[p])
        elif i > 1:
            obj_to_save += f"{splitter}{obj[p]}"
        
    return obj_to_save + "\n"