""" nombre=input("Dime cual es tu nombre?")
p=float(input("Dime cual es tu peso en kilogramos:"))
c=p*2.20462
print("Hola", nombre, "tu peso en libras es:", c)
print(f"Hola {nombre}! Tu peso en libras es: {c:.2f}")
# Para pedir el nombre al usuario y permitir que lo ingrese desde teclado, se puede usar la función input():
#nombre_usuario = input("Por favor, introduce tu nombre: ")
#print("¡Hola,", nombre_usuario + "!")

"""
#Fomas de mandar a imprimir
n="Pepe"
e=31
#Function calls
print(f"Nombre en mayuscúlas: {n.upper()}")

#Strings methods
print(f"¿El nombre comienza con 'J'?{n.startswith('J')}") #Se agrea un metodo aunque esto es mas convencional que el ejemplo siguiente 

#Condicional expressions
print(f"{n} es {"mayor de edad" if e>=18 else "menor de edad"}")# Es interesante porque el condicoonal lo anexa dentro del print
