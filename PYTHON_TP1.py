# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 23:33:51 2025

@author: sowma
"""
#%%
class Contact:
   def __init__(self, name, lastName, email, telephone):
        self._name=name
        self._lastName=lastName
        self._email=email
        self._telephone=telephone
   @property
   def name(self):
       return self._name
   @name.setter
   def name(self, name):
       self._name = name
   @property
   def lastName(self):
        return self._lastName
   @lastName.setter
   def lastName(self, lastName):
        self._lastName = lastName
   @property
   def email(self):
        return self._email
   @email.setter
   def email(self, email):
        self._email = email
   @property
   def telephone(self):
        return self._telephone
   @telephone.setter
   def telephone(self, telephone):
        self._telephone = telephone
   def __str__(self):
        return f"name : {self._name}, lastName : {self._lastName}, telephone : \
            {self._telephone}, email : {self.email}"
#%%
class GestionnaireContact:
    def __init__(self):
        self.contacts = []

    def ajouter_contact(self, name, lastName, email, telephone):
        """Ajouter un nouveau contact à la liste."""
        new_contact = Contact(name, lastName, email, telephone)
        self.contacts.append(new_contact)
        print(f"Contact {lastName} {name} ajouté.")

    def afficher_contacts(self):
        """Afficher tous les contacts."""
        if not self.contacts:
            print("Aucun contact à afficher.")
        else:
            for contact in self.contacts:
                print(contact)

    def rechercher_contact(self, name):
        """Rechercher un contact par son name."""
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        return None

    def modifier_contact(self, name, new_lastName=None, nouveau_email=None, new_telephone=None):
        """Modifier les informations d'un contact existant."""
        contact = self.rechercher_contact(name)
        if contact:
            if new_lastName:
                contact.lastName = new_lastName
            if nouveau_email:
                contact.email = nouveau_email
            if new_telephone:
                contact.telephone = new_telephone
            print(f"Contact {contact.name} modifié.")
        else:
            print(f"Contact {name} non trouvé.")

    def supprimer_contact(self, name):
        """Supprimer un contact de la liste."""
        contact = self.rechercher_contact(name)
        if contact:cdexit
            self.contacts.remove(contact)
            print(f"Contact {name} supprimé.")
        else:
            print(f"Contact {name} non trouvé.")

def charger_contacts(self):
        """Charger les contacts depuis le fichier texte."""
        try:
            with open("contacts.txt", "r") as f:
                lignes = f.readlines()
                for ligne in lignes:
                    name, lastName, email, telephone = ligne.strip().split(",")
                    contact = Contact(name, lastName, email, telephone)
                    self.contacts.append(contact)
        except FileNotFoundError:
            print("Le fichier contacts.txt n'existe pas. Aucun contact chargé.")
            
class Main:
    def __init__(self):
        self.gestionnaire = GestionnaireContact()

    def afficher_menu(self):
        """Afficher le menu des options disponibles."""
        print("\n--- Menu ---")
        print("1. Ajouter un contact")
        print("2. Consulter les contacts")
        print("3. Rechercher un contact")
        print("4. Modifier un contact")
        print("5. Supprimer un contact")
        print("6. Quitter")

    def ajouter_contact(self):
        """Permet à l'utilisateur d'ajouter un contact."""
        name = input("name : ")
        lastName = input("Préname : ")
        email = input("Email : ")
        telephone = input("Téléphone : ")
        self.gestionnaire.ajouter_contact(name, lastName, email, telephone)

    def consulter_contacts(self):
        """Afficher la liste de tous les contacts."""
        self.gestionnaire.afficher_contacts()

    def rechercher_contact(self):
        """Rechercher un contact par son name."""
        name = input("name du contact à rechercher : ")
        contact = self.gestionnaire.rechercher_contact(name)
        if contact:
            print(contact)
        else:
            print(f"Contact {name} non trouvé.")

    def modifier_contact(self):
        """Modifier un contact existant."""
        name = input("name du contact à modifier : ")
        new_lastName = input("Nouveau préname (laisser vide pour ne pas modifier) : ")
        nouveau_email = input("Nouvel email (laisser vide pour ne pas modifier) : ")
        new_telephone = input("Nouveau téléphone (laisser vide pour ne pas modifier) : ")
        self.gestionnaire.modifier_contact(name, new_lastName, nouveau_email, new_telephone)

    def supprimer_contact(self):
        """Supprimer un contact."""
        name = input("name du contact à supprimer : ")
        self.gestionnaire.supprimer_contact(name)

    def main(self):
        """Lancer l'application et interagir avec l'utilisateur."""
        while True:
            self.afficher_menu()
            choix = input("Choisissez une option (1-6) : ")
            if choix == "1":
                self.ajouter_contact()
            elif choix == "2":
                self.consulter_contacts()
            elif choix == "3":
                self.rechercher_contact()
            elif choix == "4":
                self.modifier_contact()
            elif choix == "5":
                self.supprimer_contact()
            elif choix == "6":
                print("Au revoir!")
                break
            else:
                print("Choix invalide, veuillez réessayer.")
