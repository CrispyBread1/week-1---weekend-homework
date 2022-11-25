# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, num1):
    total_money = pet_shop["admin"]["total_cash"]
    pet_shop["admin"]["total_cash"] = int(total_money) + int(num1)
    