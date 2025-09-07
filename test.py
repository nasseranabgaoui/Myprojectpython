#1st
print("Hello World")

# 1️⃣ Demander ton nom
name = input("Enter your name: ")
print(f"Hello, {name}!\n")

# 2️⃣ Demander un nombre et le convertir en int
age = input("Enter your age: ")
age = int(age)  # convertir en entier
print(f"Great! You are {age} years old.\n")

# 3️⃣ Demander un type de données
data_type = input("Choose a type (int, float, str): ").lower()

# 4️⃣ Créer une variable aléatoire selon le type choisi
if data_type == "int":
    var = int(input("Enter an integer: "))
elif data_type == "float":
    var = float(input("Enter a float number: "))
else:
    var = input("Enter a string: ")

print(f"You created a variable with value: {var} and type: {type(var)}\n")

# 5️⃣ Fonction simple pour multiplier un nombre
def multiply_by_two(x):
    return x * 2

# 6️⃣ Utiliser la fonction si la variable est un nombre
if isinstance(var, (int, float)):
    result = multiply_by_two(var)
    print(f"{var} multiplied by 2 is: {result}")
else:
    print(f"Cannot multiply '{var}' because it's not a number.\n")

# 7️⃣ Petite boucle pour répéter quelque chose
for i in range(3):
    print(f"{name}, this is loop iteration {i+1}")

print("\n✅ Script finished. Keep experimenting!")

