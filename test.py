# my_project_python.py

# Demande le nom et l'âge de l'utilisateur
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Fonction pour saluer
def greet(person_name, person_age):
    print(f"Hello {person_name}, you are {person_age} years old!")

# Boucle pour répéter le salut
for i in range(3):
    greet(name, age)

# Manipulation de liste
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
print("Numbers squared:", squared)

# Condition selon l'âge
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Petit dictionnaire
info = {"name": name, "age": age, "squared_numbers": squared}
print("Info dictionary:", info)

# Fin du script
print("Script executed successfully!")

