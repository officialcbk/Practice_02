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
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_of_numbers)

list_of_numbers.insert(5,"Emmanuel")
print(list_of_numbers)

list_of_numbers.remove(9)
print(list_of_numbers)

alphabets = ['A','B','C']

combination_of_numbers_and_letters = list_of_numbers + alphabets
print(combination_of_numbers_and_letters)

#TUPLES
canadian_provinces = ('MB','OT','SK','AB')
print(canadian_provinces)  



#DICTIONARIES

canadian_currency = {
    'nickel': 5,
    'dime': 10,
    'quarter':25,
     'looney':100,
     'tooney':200

}

print(canadian_currency)


#SETS

even_number = {2,4,6,8,10,12,14,16,18,20}
print(even_number)

multiples_of_5 = {5,10,15,20}
print(multiples_of_5)

even_numbers_multiples_of_5 ={10,20}
print(even_numbers_multiples_of_5)

common_numbers =even_number.intersection(multiples_of_5)
print(common_numbers)

even_numbers_that_are_not_multiples_of_5 = even_number.difference(multiples_of_5)
print(even_numbers_that_are_not_multiples_of_5)

multiples_of_5_that_are_not_even_numbers = multiples_of_5.difference(even_number)
print(multiples_of_5_that_are_not_even_numbers)

