def load(class_type, path_to_file, splitter):
    list = []
    with open(path_to_file, mode="r", encoding="utf-8") as file:
        for line in file:
            attrs = line.split(splitter)
            attrs[-1] = attrs[-1].replace("\n", "")
            new_obj = class_type()
            new_obj.load_from_file(attrs)    
            list.append(new_obj)
    return list

def append(obj, path_to_file):
    with open(path_to_file, mode="a", encoding="utf-8") as file:
        file.write(obj.to_save() + "\n")

def rewrite(list, path_to_file):
    with open(path_to_file, mode="w", encoding="utf-8") as file:
        for obj in list:
            file.write(obj.to_save() + "\n")