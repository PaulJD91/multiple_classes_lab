class PetShop:

    def __init__(self, name, cash, pets):
        self.name = name
        self.cash = cash
        self.pets = pets
        self.pets_sold = 0

    def stock_count(self):
        return len(self.pets)
    
    def increase_total_cash(self, amount):
        self.cash += amount

    def remove_pet(self, pet):
        self.pets.remove(pet)

    def find_pet_by_name(self, name):
        for pet in self.pets:
            if pet.name == name:
                return pet
    def increase_pets_sold(self):
        self.pets_sold += 1

    def sell_pet(self, pet_name_to_sell):
        pet_to_sell = self.find_pet_by_name(pet_name_to_sell)
        self.increase_total_cash(pet_to_sell.price)
        self.remove_pet(pet_to_sell)
        self.increase_pets_sold()
        return pet_to_sell

        
