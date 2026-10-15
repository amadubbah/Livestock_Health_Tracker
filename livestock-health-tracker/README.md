# Livestock Health & Tracking System
## About the Project
Many small farmers keep their animal health records on paper or not at all. This makes it hard to know which animals are sick or when they were last vaccinated.

This is a simple Python program that helps a farmer keep health records for farm animals. Each animal is recorded by its tag ID (for example, LV001), and the farmer can track its health and vaccinations.

## Features
1. Register a new animal
2. View all animals
3. Search for an animal by tag ID
4. Update an animal's health status
5. Record a vaccination
6. Remove an animal (sold or deceased)
7. View a farm health report

## Files
| File | What it contains |
|---|---|
| `animal.py` | The Animal class (one animal's record) |
| `farm.py` | The Farm class (stores all animals in a list) |
| `main.py` | The menu – run this file to start the program |
| `LICENSE` | MIT open-source licence |

## How to Run
You only need Python 3 installed. No extra libraries are required.
```
python main.py
```
The program loads four sample animals at the start so it can be tested straight away.

## OOP Concepts Used
- **Classes and objects:** two classes, `Animal` and `Farm`. One Farm object holds many Animal objects.
- **Attributes:** each animal has its own `tag_id`, `species`, `age`, `weight_kg` and `health_status`. Some values, like the list of allowed species, are shared by all animals (class attributes).
- **List:** the farm stores all Animal objects in a list called `animals`. Animals are added with `add_animal()` and shown with `display_animals()`.
- **Tuples:** used for the fixed species and health options, and for vaccination records, because this data should not change.
- **Instance methods:** e.g. `display_info()`, `update_health()`, `add_vaccination()`
- **Class methods:** `get_total_animals()` and `from_record()`
- **Static method:** `is_valid_tag_id()` checks that a tag ID is in the correct format (LV followed by 3 digits)

## How It Meets DPG Standards
- **Open-source:** the code is free on GitHub under the MIT licence, so anyone can use and improve it.
- **Inclusive and accessible:** simple menus with numbered choices, clear messages, and wrong input does not crash the program. It runs on any computer with Python and does not need the internet.
- **Privacy-respecting:** no personal data is stored. Animals are identified by tag ID, and the farm only by a farm code and district. No farmer names or phone numbers are collected.
- **Modular and reusable:** the code is split into separate files, so the `Animal` and `Farm` classes can be reused in other projects.

This project also supports **SDG 2 – Zero Hunger**, because healthy animals mean more food and income for farming families.

## Sample Input/Output

**Viewing all animals**
```
Choose an option (0-7): 2

--- Animals on Farm FM-001 (Bo District) ---
1. LV001 | Cow | 4 yr(s) | 320 kg | Healthy
2. LV002 | Goat | 2 yr(s) | 35 kg | Sick
3. LV003 | Sheep | 3 yr(s) | 48 kg | Healthy
4. LV004 | Chicken | 1 yr(s) | 2 kg | Under Treatment
Total animals: 4
```

**Searching for an animal**
```
Choose an option (0-7): 3

--- Search Animal ---
Enter tag ID (e.g. LV001): LV001

--- Animal Record: LV001 ---
Tag ID        : LV001
Species       : Cow
Age           : 4 year(s)
Weight        : 320 kg
Health Status : Healthy
Vaccinations  :
   - Anthrax Vaccine (given on 2026-08-14)
```

**Wrong input is handled safely**
```
--- Register New Animal ---
Enter tag ID (LV followed by 3 digits, e.g. LV005): COW9
Invalid tag ID. It must be LV followed by 3 digits, e.g. LV005.
```

## Licence
This project is released under the MIT Licence.