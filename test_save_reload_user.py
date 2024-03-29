#!/usr/bin/python3

from models.base_model import BaseModel
from models import storage
from models .user import User

all_objs = storage.all()
print("--cReloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_user = User()
my_user.first_name = "Betty"
my_user.last_name = "Holberton"
my_user.email = "airbnb@holbertonshool.com"
my_user.password = "root"
my_user.save()
print(my_user)

print("-- Create a new user 2 --")
my_user2 = User()
my_user2.first_name = "John"
my_user2.email = "airbnb@holbertonshool.com"
my_user2.password = "root"
my_user2.save()
print(my_user2)
