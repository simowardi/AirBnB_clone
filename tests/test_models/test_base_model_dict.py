#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My_First_Base_Model"
my_model.my_number = 79
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key, value in my_model_json.keys():
    print(f"\t{key}: ({type(value).__name__}) - {value}")

print("--")
my_new_base_model = BaseModel(**my_model_json)
print(my_new_base_model.id)
print(my_new_base_model)
print(type(my_new_base_model.created_at))

print("--")
print(my_model is my_new_base_model)
