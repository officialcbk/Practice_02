"""
Description:Data Types In Python
Author:Emmanuel Eze
Date:22-9-2024
"""

#SIMPLE DATA TYPES
name = "Emmanuel"
print('name:' ,name)
print('type:' ,type(name))

has_driving_license = False
print('has driving license:' , has_driving_license)
print('type:', type(has_driving_license))

current_year = 2024
print('this year:' , current_year)
print('type :' , type(current_year))

current_year = 2024+1
print('this year:' , current_year)
print('type :' , type(current_year))


#CALCULATIONS
GST = 0.05
PST = 0.07
purchase_price = 70000

federal_tax = purchase_price * GST
provincial_tax = purchase_price * PST

final_cost = purchase_price + federal_tax + provincial_tax

print(f"Purchase Price: {purchase_price}, Federal Tax: {federal_tax}, Provincial Tax: {provincial_tax}, Final Cost: {final_cost}")

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
    'nickel': 0.05,
    'dime': 0.10,
    'quarter': 0.25
}

print(type(canadian_currency))

print(canadian_currency)

canadian_currency['nickel'] = 5      #Modified the values of nickel,dime,quarter
canadian_currency['dime'] = 10
canadian_currency['quarter'] = 25

print(canadian_currency)

canadian_currency['loonie'] = 100   #Added loonie and tooney to the dictionary
canadian_currency['toonie'] = 200

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

