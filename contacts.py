contacts = {
    "number": 4,
    "students": 
    [
        {"name": "Wodson Luiz Correia", "email": "wodsonluiz@live.com"},
        {"name": "Joao Luiz Correia", "email": "joao@live.com"},
        {"name": "Maria Luiza Correia", "email": "maria@live.com"},
        {"name": "Maria Nubia Correia", "email": "marianubia@live.com"},
    ]
}

print("Student emails:")
for student in contacts["students"]:
    print(student["email"])