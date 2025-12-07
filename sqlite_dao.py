import sqlite3
from classes import Produit, Client

def connexion():
    return sqlite3.connect("boutique.db")

def init_db():
    conn = connexion()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS produit (id INTEGER PRIMARY KEY, nom TEXT, prix REAL)")
    cursor.execute("CREATE TABLE IF NOT EXISTS client (id INTEGER PRIMARY KEY, nom TEXT, email TEXT UNIQUE)")
    conn.commit()
    conn.close()

def ajouter_produit(produit):
    conn = connexion()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO produit (id, nom, prix) VALUES (?, ?, ?)", (produit.id, produit.nom, produit.prix))
    conn.commit()
    conn.close()

def lister_produits():
    conn = connexion()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nom, prix FROM produit")
    rows = cursor.fetchall()
    conn.close()
    return [Produit(*row) for row in rows]

def ajouter_client(client):
    conn = connexion()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO client (id, nom, email) VALUES (?, ?, ?)", (client.id, client.nom, client.email))
    conn.commit()
    conn.close()

def lister_clients():
    conn = connexion()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nom, email FROM client")
    rows = cursor.fetchall()
    conn.close()
    return [Client(*row) for row in rows]

def rechercher_client_email(email):
    conn = connexion()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nom, email FROM client WHERE email=?", (email,))
    row = cursor.fetchone()
    conn.close()
    return Client(*row) if row else None

def modifier_prix_produit(id, nouveau_prix):
    conn = connexion()
    cursor = conn.cursor()
    cursor.execute("UPDATE produit SET prix=? WHERE id=?", (nouveau_prix, id))
    conn.commit()
    conn.close()
