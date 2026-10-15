"""
main.py
Livestock Health & Tracking System - main program
"""

from animal import Animal
from farm import Farm


def get_whole_number(prompt, min_value, max_value):
    """Keep asking until the user enters a whole number in the allowed range."""
    while True:
        value = input(prompt).strip()
        if value.isdigit() and min_value <= int(value) <= max_value:
            return int(value)
        print(f"Please enter a whole number from {min_value} to {max_value}.")


def get_text(prompt):
    """Keep asking until the user types something (not left blank)."""
    while True:
        value = input(prompt).strip()
        if value != "":
            return value
        print("This field cannot be left blank.")


def choose_option(title, options):
    """Show numbered options from a tuple and return the one the user picks."""
    print(f"\n{title}")
    for index, option in enumerate(options):
        print(f"  {index + 1}. {option}")
    number = get_whole_number("Enter number: ", 1, len(options))
    return options[number - 1]


def ask_for_existing_animal(farm):
    """Ask for a tag ID and return the matching animal, or None if not found."""
    tag_id = get_text("Enter tag ID (e.g. LV001): ")
    animal = farm.find_animal(tag_id)
    if animal is None:
        print(f"No animal with tag ID {tag_id.upper()} was found.")
    return animal


# MENU ACTIONS 

def register_animal(farm):
    print("\n--- Register New Animal ---")
    tag_id = get_text("Enter tag ID (LV followed by 3 digits, e.g. LV005): ").upper()

    if not Animal.is_valid_tag_id(tag_id):
        print("Invalid tag ID. It must be LV followed by 3 digits, e.g. LV005.")
        return
    if farm.find_animal(tag_id) is not None:
        print(f"Tag ID {tag_id} is already in use. Please use a different tag.")
        return

    species = choose_option("Select species:", Animal.ALLOWED_SPECIES)
    age = get_whole_number("Enter age in years (0-30): ", 0, 30)
    weight_kg = get_whole_number("Enter weight in kg (1-2000): ", 1, 2000)
    health_status = choose_option("Select health status:", Animal.HEALTH_STATUSES)

    # Keyword arguments make sure every value goes to the right attribute
    new_animal = Animal(tag_id=tag_id, species=species, age=age,
                        weight_kg=weight_kg, health_status=health_status)
    farm.add_animal(new_animal)


def search_animal(farm):
    print("\n--- Search Animal ---")
    animal = ask_for_existing_animal(farm)
    if animal is not None:
        animal.display_info()


def update_animal_health(farm):
    print("\n--- Update Health Status ---")
    animal = ask_for_existing_animal(farm)
    if animal is not None:
        print(f"Current status of {animal.tag_id}: {animal.health_status}")
        new_status = choose_option("Select new health status:", Animal.HEALTH_STATUSES)
        animal.update_health(new_status)


def record_vaccination(farm):
    print("\n--- Record Vaccination ---")
    animal = ask_for_existing_animal(farm)
    if animal is not None:
        vaccine_name = get_text("Enter vaccine name: ")
        date_given = get_text("Enter date given (YYYY-MM-DD): ")
        animal.add_vaccination(vaccine_name, date_given)


def remove_animal(farm):
    print("\n--- Remove Animal (sold or deceased) ---")
    tag_id = get_text("Enter tag ID of the animal to remove: ")
    farm.remove_animal(tag_id)


def load_sample_data(farm):
    """Load a few example animals so the program can be demonstrated."""
    sample_records = [
        ("LV001", "Cow", 4, 320, "Healthy"),
        ("LV002", "Goat", 2, 35, "Sick"),
        ("LV003", "Sheep", 3, 48, "Healthy"),
        ("LV004", "Chicken", 1, 2, "Under Treatment"),
    ]
    for record in sample_records:
        animal = Animal.from_record(record)   
        farm.add_animal(animal)              

    
    farm.find_animal("LV001").add_vaccination("Anthrax Vaccine", "2026-08-14")
    farm.find_animal("LV003").add_vaccination("PPR Vaccine", "2026-09-02")


def show_menu():
    print("\n========== LIVESTOCK HEALTH & TRACKING SYSTEM ==========")
    print("1. Register a new animal")
    print("2. View all animals")
    print("3. Search for an animal by tag ID")
    print("4. Update an animal's health status")
    print("5. Record a vaccination")
    print("6. Remove an animal (sold or deceased)")
    print("7. View farm health report")
    print("0. Exit")


# MAIN PROGRAM 

def main():
    farm = Farm(farm_id="FM-001", district="Bo")

    print("Loading sample records...")
    load_sample_data(farm)
    print(f"{len(farm.animals)} sample animals loaded for farm {farm.farm_id}.")

    while True:
        show_menu()
        choice = input("Choose an option (0-7): ").strip()

        if choice == "1":
            register_animal(farm)
        elif choice == "2":
            farm.display_animals()
        elif choice == "3":
            search_animal(farm)
        elif choice == "4":
            update_animal_health(farm)
        elif choice == "5":
            record_vaccination(farm)
        elif choice == "6":
            remove_animal(farm)
        elif choice == "7":
            farm.display_health_report()
        elif choice == "0":
            print("Thank you for using the Livestock Health & Tracking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 0 to 7.")

if __name__ == "__main__":
    main()
