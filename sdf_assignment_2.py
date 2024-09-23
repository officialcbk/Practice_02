"""
Description:Data Types In Python
Author:Emmanuel Eze
Date:22-9-2024
"""

#SIMPLE DATA TYPES
name = "Emmanuel"
print('name:' ,name)
print('type:' ,type(name))

current_driving_status = False
print('has driving license:' , current_driving_status)
print('type:', type(current_driving_status))

current_year = 2024
print('this year:' , current_year)
print('type :' , type(current_year))

current_year = 2024+1
print('this year:' , current_year)
print('type :' , type(current_year))


#CALCULATIONS
GST = 0.05
PST = 0.07
vehicle_price = 70000

print('pre-tax value :',vehicle_price) 
print('Provincial Tax:', PST * vehicle_price) 
print('Federal Tax:', GST * vehicle_price) 
print('Total :' , (PST * vehicle_price)+(GST * vehicle_price))


#LISTS

#TUPLES

#DICTIONARIES

#SETS

