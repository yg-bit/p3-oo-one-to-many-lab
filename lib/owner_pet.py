class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Returns a list of all pets owned by this owner"""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Adds a pet to the owner, checking that it's a Pet instance"""
        if not isinstance(pet, Pet):
            raise Exception(f"Can only add Pet instances")
        pet.owner = self

    def get_sorted_pets(self):
        """Returns a sorted list of pets by their names"""
        return sorted(self.pets(), key=lambda pet: pet.name)