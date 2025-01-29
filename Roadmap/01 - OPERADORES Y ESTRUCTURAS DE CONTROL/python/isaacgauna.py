#operadores aritmeticos. 
 
print(f"suma de 2 valores, 2 + 2 = {2+2},")
print(f"resto de 2 valores, 10 - 5 = {10-5}")
print(f"multiplica 2 valores,10 * 15 ={10*15}")
print(f"divide 2 valores, cociente con decimales, 15 / 5 ={15/5}")
print(f"residuo de una division, 15 % 2 ={15%2}")
print(f"potencia, 15 ** 10 ={15**10}")
print(f"division entera, 15 // 2 ={15//2}")

# Operadores de comparación, retorna true or false
print(f"Igualdad: 10 == 5 es {10 == 5}")
print(f"Desigualdad: 10 != 3 es {10 != 3}")
print(f"Mayor que: 10 > 3 es {10 > 3}")
print(f"Menor que: 10 < 3 es {10 < 3}")
print(f"Mayor o igual que: 10 >= 10 es {10 >= 10}")
print(f"Menor o igual que: 10 <= 3 es {10 <= 3}")

# Operadores lógicos
print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}") #ambas condiciones son true.
print(f"OR ||: 10 + 3 == 13 or 5 - 1 == 4 es {10 + 3 == 14 or 5 - 1 == 4}") #una de las condiciones es true.
print(f"NOT !: not 10 + 3 == 14 es {not 10 + 3 == 14}") #condicion falsa

# Operadores de identidad, ocupa una dirección dentro de la memoria, return true or false. 
my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is not my_new_number es {my_number is not my_new_number}")

# Operadores de pertenencia, return true or false
print(f"'i' in 'isaacgauna' = {'i' in 'isaacgauna'}")
print(f"'b' not in 'isaacgauna' = {'b' not in 'isaacgauna'}")

# Operadores de bit , transforma a binario y los resuelve, 
a = 10  # 1010
b = 3  # 0011
print(f"AND: 10 & 3 = {10 & 3}")  # 0010
print(f"OR: 10 | 3 = {10 | 3}")  # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}")  # 1001
print(f"NOT: ~10 = {~10}") 
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}")  # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}")  # 101000

"""
Estructuras de control
"""

# Condicionales

my_string = "isaac"

if my_string == "isaac":
    print("my_string es 'Macarrones'")
elif my_string == "macarrones":
    print("my_string es 'dev'")
else:
    print("my_string no es 'macarrones' ni 'isaac'")

# Iterativas, bucles, ejecutar una accion varias veces
for i in range(11):
    print(i)

i = 0
    #condicion se ejecuta mientras sea verdadera.
while i <= 10: 
    print(i)
    i += 1

# Manejo de excepciones
try:
    print(10 / 0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")

"""
Extra
"""

for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)
