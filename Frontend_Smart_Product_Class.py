# Template for a new smart object
class smart_object():
    
    def __init__(self):
        
        self._smart_object_characteristics = []
        
    def get_smart_object_characteristic(self):

        return self._smart_object_characteristics
    
    def set_smart_object_characteristic(self, characteristic):
        
        self._smart_object_characteristics.append(characteristic)
