# Fonction pour vérifier si un nombre est premier
def est_premier(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Fonction pour afficher les nombres premiers jusqu'à une limite
def afficher_nombres_premiers(limite):
    print(f"Nombres premiers jusqu'à {limite} :")
    for num in range(2, limite + 1):
        if est_premier(num):
            print(num, end=" ")

# Appel de la fonction avec une limite choisie
limite = int(input("Entrez une limite : "))
afficher_nombres_premiers(limite)
