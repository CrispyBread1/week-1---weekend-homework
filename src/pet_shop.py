# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]
# 1
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]
# 2
def add_or_remove_cash(pet_shop, num1):
    total_money = pet_shop["admin"]["total_cash"]
    pet_shop["admin"]["total_cash"] = int(total_money) + int(num1)
# 3
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]
# 4
def increase_pets_sold(pet_shop, num1):
    pet_shop["admin"]["pets_sold"] = num1
    return pet_shop["admin"]["pets_sold"]
# 5
def get_stock_count(pet_shop):
    return len(pet_shop["pets"])
# 6
def get_pets_by_breed(pet_shop, pet_breed):
    pets_breed = []
    for pets in pet_shop["pets"]:
        if pets["breed"] == pet_breed:
            pets_breed.append('pets') 
    return pets_breed
# 7
def find_pet_by_name(pet_shop, pet_name):
    for pets in pet_shop["pets"]:
        if pets["name"] == pet_name:
            pet_name = pets
            return pet_name
# 8
def remove_pet_by_name(pet_shop, name):
    number_in_list = 0
    while pet_shop["pets"] != name:
        number_in_list += 1
        if pet_shop['pets'] == name:
            break
    pet_shop["pets"].pop(number_in_list)
