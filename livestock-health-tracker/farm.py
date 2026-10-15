"""
farm.py
Livestock Health & Tracking System - Farm class
"""

from animal import Animal


class Farm:
    def __init__(self, farm_id, district):
        self.farm_id = farm_id.strip().upper()
        self.district = district.strip().title()
        self.animals = []          

    def add_animal(self, animal):
        """Add an Animal object to the farm's list (rejects duplicate tag IDs)."""
        if self.find_animal(animal.tag_id) is not None:
            print(f"Tag ID {animal.tag_id} is already registered on this farm.")
            return False

        self.animals.append(animal)
        print(f"{animal.species} {animal.tag_id} added to farm {self.farm_id} successfully.")
        return True

    def display_animals(self):
        """Loop through the list and display every animal on the farm."""
        print(f"\n--- Animals on Farm {self.farm_id} ({self.district} District) ---")

        # Check if there are any animals first
        if len(self.animals) == 0:
            print("No animals registered yet.")
        else:
            for index, animal in enumerate(self.animals):
                print(f"{index + 1}. {animal.get_summary()}")
            print(f"Total animals: {len(self.animals)}")

    def find_animal(self, tag_id):
        """Search the list for an animal by tag ID. Returns None if not found."""
        tag_id = tag_id.strip().upper()
        for animal in self.animals:
            if animal.tag_id == tag_id:
                return animal
        return None

    def remove_animal(self, tag_id):
        """Remove an animal from the list (e.g. sold or deceased)."""
        animal = self.find_animal(tag_id)
        if animal is None:
            print(f"No animal with tag ID {tag_id.strip().upper()} was found.")
            return False

        self.animals.remove(animal)
        print(f"{animal.species} {animal.tag_id} has been removed from the farm.")
        return True

    def display_health_report(self):
        """Show a summary of the farm: animals per species and those needing care."""
        print(f"\n--- Health Report: Farm {self.farm_id} ({self.district} District) ---")
        print(f"Animals currently on farm : {len(self.animals)}")
        print(f"Animal records created    : {Animal.get_total_animals()}")

        # Count animals of each species using the fixed species tuple
        print("\nAnimals by species:")
        for species in Animal.ALLOWED_SPECIES:
            count = 0
            for animal in self.animals:
                if animal.species == species:
                    count += 1
            if count > 0:
                print(f"   {species}: {count}")

        # List animals that are sick or under treatment
        print("\nAnimals needing attention:")
        attention_count = 0
        for animal in self.animals:
            if animal.needs_attention():
                print(f"   - {animal.get_summary()}")
                attention_count += 1

        if attention_count == 0:
            print("   None - all animals are healthy or recovered.")
