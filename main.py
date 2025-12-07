from classes import Produit, Client
import sqlite_dao as dao

dao.init_db()

while True:
    print("\n1. Ajouter produit\n2. Lister produits\n3. Ajouter client\n4. Lister clients\n5. Rechercher client par email\n6. Modifier prix produit\n0. Quitter")
    choix = input("Choix: ")
    if choix == "1":
        id = int(input("ID produit: "))
        nom = input("Nom: ")
        prix = float(input("Prix: "))
        dao.ajouter_produit(Produit(id, nom, prix))
    elif choix == "2":
        for p in dao.lister_produits():
            print(p)
    elif choix == "3":
        id = int(input("ID client: "))
        nom = input("Nom: ")
        email = input("Email: ")
        dao.ajouter_client(Client(id, nom, email))
    elif choix == "4":
        for c in dao.lister_clients():
            print(c)
    elif choix == "5":
        email = input("Email à rechercher: ")
        client = dao.rechercher_client_email(email)
        print(client if client else "Non trouvé")
    elif choix == "6":
        id = int(input("ID produit: "))
        prix = float(input("Nouveau prix: "))
        dao.modifier_prix_produit(id, prix)
    elif choix == "0":
        break
