#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User

all_objcts = storage.all()
print("-- Reloaded objects --")
for objct_id in all_objcts.keys():
    objct = all_objcts[objct_id]
    print(objct)

print("-- Create User --")
my_user = User()
my_user.first_name = "Betty"
my_user.last_name = "Badr"
my_user.email = "badrbnb@mail.com"
my_user.password = "AZsqqsnice"
my_user.save()
print(my_user)

print("-- Create User 2 --")
my_user2 = User()
my_user2.first_name = "John"
my_user2.email = "mohamed3bnb@mail.com"
my_user2.password = "simo4333DDdz"
my_user2.save()
print(my_user2)

print("-- Create User 3 --")
my_user2 = User()
my_user2.first_name = "sofia"
my_user2.email = "sofia233bnb@mail.com"
my_user2.password = "sofia123tt"
my_user2.save()
print(my_user3)

