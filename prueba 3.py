#Este programa es un calculador de operaciones basicas, este programa es muy basico y no tiene en cuenta los errores de usuario.
a=input("Que operacion deseseas realizar?")
b=float(input("Dime el primer numero:"))
c=float(input("Dime el segundo numero:"))
match a:
    case "suma":
        print(f"La suma de {b} y {c} es {b+c}")
    case "resta":
        print(f"La resta de {b} con {c} es {b-c}")
    case "Dividir":
        print(f"El resulytado de esta operacion es {b/c}")
    case "multiplicación":
        print(f"El resulytado de esta operacion es {b*c}")
    