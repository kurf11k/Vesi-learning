import inspect
import storage
from tabulate import tabulate


class Service:
    def __init__(self, class_type, path_to_file):
        self.class_type = class_type
        self.path_to_file = path_to_file
        self.list = storage.load(class_type, path_to_file)
    
    def show_menu(self):
        while True:
            print("---------------")
            print(f"MENU - {self.class_type.__name__}")
            print("1 - Show")
            print("2 - Add" )
            print("3 - Delete")
            #print("4 - Update") - tohle až bude implementace na update
            print("0 - End")
            choice = input("Type choice: ")
            
            if choice == "1":
                self.show_list()
            
            elif choice == "2":
                self.add()
                
            elif choice == "3":
                self.delete()
                
            else:
                break
            
            input("Press any key to continue to menu...")
            
    def show_list(self):
        list_to_show = []
        for obj in self.list:
            line = self.__convert_obj_to_list(obj)
            list_to_show.append(line)
            
        headers = self.__get_class_attrs()
        for i, header in enumerate(headers):
            header = header.capitalize()
            header = header.replace("_", " ")
            headers[i] = header
        
        print(tabulate(list_to_show, headers=headers))
    
    def get(self):
        return self.list
            
    def add(self):
        print("\n------------")
        print(f"{self.class_type.__name__} - creation")
        attrs = {}
        for attr in self.__get_class_attrs():
            attr_name = attr.replace("_", " ")
            attrs[attr] = input(f"Type {attr_name}: ")
                
        new_obj = self.class_type(**attrs)
        self.list.append(new_obj)
        storage.append(new_obj, self.path_to_file)
        print(f"{self.class_type.__name__} was succesfully created.")
        
    def update(self):
        print("\n------------")
        print(f"{self.class_type.__name__} - update")
        # to do


    def delete(self):
        self.show()
        id = input("Type id of object you want delete: ")
        for obj in self.list:
            if id == obj.id:
                self.list.remove(obj)
                break
        storage.rewrite(self.list, self.path_to_file)
        print(f"{self.class_type.__name__} was succesfully deleted.")

    def __str__(self):
        return self.list
    
    def __get_class_attrs(self):
        constructor = inspect.signature(self.class_type.__init__)
        attrs = list(constructor.parameters)
        attrs.pop(0)
        return attrs
    
    def __convert_obj_to_list(self, obj):
        obj = obj.__dict__
        obj_to_print = []
        for i, p in enumerate(self.__get_class_attrs()):
            obj_to_print.append(obj[p])
                
        return obj_to_print