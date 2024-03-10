#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objcts = storage.all()
print("-- Reloaded objects --")
for objct_id in all_objcts.keys():
    objct = all_objcts[objct_id]
    print(objct)

print("-- a new object created --")
my_model = BaseModel()
my_model.name = "My_First_Base_Model"
my_model.my_number = 79
my_model.save()
print(my_model)
