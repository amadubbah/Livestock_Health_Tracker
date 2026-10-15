"""
animal.py
Livestock Health & Tracking System - Animal class
"""

class Animal:
    # Class attributes 
    ALLOWED_SPECIES = ("Cow", "Goat", "Sheep", "Pig", "Chicken")
    HEALTH_STATUSES = ("Healthy", "Sick", "Under Treatment", "Recovered")

    
    total_animals = 0

    def __init__(self, tag_id, species, age, weight_kg, health_status="Healthy"):
        # Instance attributes
        self.tag_id = tag_id.strip().upper()
        self.species = species.strip().title()
        self.age = age                      
        self.weight_kg = weight_kg          
        self.health_status = health_status
        self.vaccinations = []              

        
        Animal.total_animals += 1

    # INSTANCE MTHODS 

    def display_info(self):
        """Print the full record of this animal."""
        print(f"\n--- Animal Record: {self.tag_id} ---")
        print(f"Tag ID        : {self.tag_id}")
        print(f"Species       : {self.species}")
        print(f"Age           : {self.age} year(s)")
        print(f"Weight        : {self.weight_kg} kg")
        print(f"Health Status : {self.health_status}")

        if len(self.vaccinations) == 0:
            print("Vaccinations  : None recorded")
        else:
            print("Vaccinations  :")
            for vaccine_name, date_given in self.vaccinations:
                print(f"   - {vaccine_name} (given on {date_given})")

    def get_summary(self):
        """Return a one-line summary of this animal (used in lists)."""
        return (f"{self.tag_id} | {self.species} | {self.age} yr(s) | "
                f"{self.weight_kg} kg | {self.health_status}")

    def update_health(self, new_status):
        """Change the health status if the new status is a valid option."""
        if new_status not in Animal.HEALTH_STATUSES:
            print(f"'{new_status}' is not a valid health status.")
            return False

        old_status = self.health_status
        self.health_status = new_status
        print(f"{self.tag_id} health status updated: {old_status} -> {new_status}")
        return True

    def add_vaccination(self, vaccine_name, date_given):
        """Store a vaccination as a tuple so the record cannot be altered later."""
        vaccine_record = (vaccine_name.strip(), date_given.strip())
        self.vaccinations.append(vaccine_record)
        print(f"Vaccination '{vaccine_record[0]}' recorded for {self.tag_id}.")

    def needs_attention(self):
        """Return True if the animal is sick or still under treatment."""
        return self.health_status in ("Sick", "Under Treatment")

  #   CLASS METHODS 

    @classmethod
    def get_total_animals(cls):
        """Return how many Animal objects have been created."""
        return cls.total_animals

    @classmethod
    def from_record(cls, record):
        """
        Create an Animal from a tuple record, e.g. a line copied from a
        farmer's paper register: ("LV001", "Cow", 4, 320, "Healthy")
        """
        tag_id, species, age, weight_kg, health_status = record   
        return cls(tag_id=tag_id, species=species, age=age,
                   weight_kg=weight_kg, health_status=health_status)

    # STATIC METHOD

    @staticmethod
    def is_valid_tag_id(tag_id):
        """
        Check that a tag ID follows the farm's format:
        'LV' followed by exactly 3 digits, e.g. LV001.
        """
        tag_id = tag_id.strip().upper()
        return len(tag_id) == 5 and tag_id.startswith("LV") and tag_id[2:].isdigit()
