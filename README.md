# 🧠 Gestion de Stock Moderne avec Django

Ce projet est une application web complète de **gestion de stock** développée avec **Django**, offrant une architecture modulaire, une interface moderne, et des fonctionnalités prêtes à l’emploi pour les PME ou les entreprises en croissance.

## 🚀 Fonctionnalités principales

- 🔐 **Authentification sécurisée** (app `utilisateurs`)
- 📦 **Gestion des produits et des stocks** (app `stocks`, `produit`)
- 🧾 **Facturation intelligente** (app `facturation`)
- 🏪 **Gestion des clients et fournisseurs**
- 💼 **Suivi des ventes et des caisses**
- 🏢 **Gestion des informations d’entreprise**
- 🔔 **Système d’alertes** (ex: stock critique)
- 🖼️ Upload & gestion des médias (dossier `media`)
- 🌐 Interface web responsive

---

## 🛠️ Structure du projet

gestion_stock/
├── alertes/ → Gestion des notifications et alertes (ex: stock bas)
├── caisse/ → Suivi des entrées/sorties de caisse
├── clients/ → Module de gestion client
├── entreprise/ → Paramètres de l’entreprise
├── facturation/ → Génération de factures, suivi des paiements
├── fournisseur/ → Gestion des fournisseurs
├── gestion_stock/ → Fichiers de configuration Django (settings, urls, wsgi)
├── media/ → Fichiers uploadés (ex: logos, documents)
├── produit/ → Catégories, types et gestion des produits
├── static/ → Fichiers statiques CSS/JS
├── staticfiles/ → Output de collectstatic
├── stocks/ → Logique de gestion de stock
├── templates/ → Templates HTML
├── utilisateurs/ → Authentification, permissions, profils
├── ventes/ → Suivi des ventes
├── db.sqlite3 → Base de données (par défaut)
├── manage.py
├── README.md
└── requirement.txt

---

## ⚙️ Installation

# Cloner le repo
git clone https://github.com/ton-utilisateur/gestion-stock.git
cd gestion-stock

# Créer un environnement virtuel
python -m venv env
source env/bin/activate  # ou env\Scripts\activate sur Windows

# Installer les dépendances
pip install -r requirement.txt

# Lancer les migrations
python manage.py migrate

# Créer un superutilisateur
python manage.py createsuperuser
Interface d’admin Django : http://localhost:8000/admin

# Lancer le serveur
python manage.py runserver

Ce projet est open source. Tu peux l'utiliser librement dans tes projets personnels ou professionnels.


