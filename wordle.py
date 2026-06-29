import random


def adivinar(att):
    usadas = []
    intento = []

    while True:
        guess = list(input(f"Intento {att} de {dificultades[tries]}: ").lower())
        if len(guess) == len(lispa):
            break
        else:
            print("La palabra no es de el mismo  tamaño, intente de nuevo")

    if guess == lispa:
        print("Ganaste")
        return True
    else:
        for i in range(len(guess)):
            if guess[i] == lispa[i]:
                intento.append(guess[i].upper())
                usadas.append(guess[i])
            elif guess[i] in lispa and guess[i] not in usadas:
                intento.append(guess[i])
                usadas.append(guess[i])
            else:
                intento.append("-")
    print(intento)


palabras = [
    "caballo",
    "amigo",
    "animal",
    "perro",
    "gato",
    "casa",
    "arbol",
    "fuego",
    "agua",
    "monte",
    "playa",
    "musica",
    "camino",
    "puerta",
    "ventana",
    "jardin",
    "estrella",
    "montana",
    "control",
    "bosque",
]

pa = random.choice(palabras)

dificultades = {"facil": 10, "normal": 7, "dificil": 5}

while True:
    tries = input(
        "Eliga la dificultad\n\
-Facil: 10 intentos\n\
-Normal: 7 intentos\n\
-Dificl: 5 intentos\n :"
    ).lower()
    if tries in dificultades:
        break
    else:
        print("Error intente de nuevo")

lispa = list(pa)

print(f"La palabra tiene {len(pa)} caracteres")
win = False
att = 0

for i in range(dificultades[tries]):
    att += 1
    if adivinar(att):
        win = True
        break

if not win:
    print(f"Perdiste.\nLa palabra era {pa}")
