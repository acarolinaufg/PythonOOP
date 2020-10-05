class Item():
    def __init__(self,name_obj, description_obj):
        self.name = name_obj
        self.description = description_obj
    
    def set_name(self,name_obj):
        self.name = name_obj
    
    def get_name(self):
        return self.name
    
    def set_description(self, description_obj):
        self.description = description_obj

    def get_description(self):
        return self.description