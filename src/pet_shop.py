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
def remove_pet_by_name(pet_shop, name_to_delete):
    number_in_list = -1
    for pets in pet_shop["pets"]:
        if pets["name"] != name_to_delete:
            number_in_list + 1
        pet_shop["pets"].pop(int(number_in_list))
# 9
def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

# 10
def get_customer_cash(customer):
    return customer["cash"]

# 11
def remove_customer_cash(customer, num1):
    customer["cash"] -= int(num1)
    
def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet["name"]) 

def customer_can_afford_pet(customer, new_pet):
    return bool(new_pet["price"] == customer["cash"])
        
def sell_pet_to_customer(pet_shop, pet, customer):
    for pets in pet_shop["pets"]:
        if pets["name"] == pet:
            customer["pets"].append(pet)
            pet_shop["admin"]["pets_sold"] += 1
            customer["cash"] -= int(pet["price"])
            pet_shop["admin"]["total_cash"] += int(pet["price"])
        else: break

            