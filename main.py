# ma calculatrice 9000 !

def saisie_nombre():
    while True:
        try:
            nombre = float(input("Entrez un nombre : "))
            return nombre
        except ValueError:
            print("Erreur : Veuillez entrer un nombre valide.")

def saisie_operation():
    operations_valides = ['+', '-', '*', '/']
    while True:
        operation = input("Entrez une opération (+, -, *, /) : ")
        if operation in operations_valides:
            return operation
        else:
            print("Erreur : Opération non valide. Veuillez entrer une opération valide.")

def calculatrice():
    print("CALCULATRICE 9000 !")

    while True:
        # pour la Saisie des nombres et de l'opération
        nombre1 = saisie_nombre()
        nombre2 = saisie_nombre()
        operation = saisie_operation()

                                             # pour les calculs et l'affichage
        if operation == '+':
            resultat = nombre1 + nombre2
        elif operation == '-':
            resultat = nombre1 - nombre2
        elif operation == '*':
            resultat = nombre1 * nombre2
        elif operation == '/':
            if nombre2 != 0:
                resultat = nombre1 / nombre2
            else:
                print("Erreur : Division par zéro.")
                continue  # "else", pour recommencer la boucle while

        print(f"Résultat : {resultat}")

                                                                         #je mets un "imput" si l'utilisateur souhaite effectué d'autres calculs
        continuer = input("Voulez-vous effectuer une autre opération ? (y/n) : ").lower()
        if continuer != 'y':
            break

if __name__ == "__main__":
    calculatrice()