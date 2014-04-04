app-gestion-stage
=================

Application de gestion des stages pour l'IUT d'Orléans

INSTALLATION :

1. Installer Python. ( Déjà présent sur la plupart des distributions Linux, sinon : http://www.python.org )


2. Installation d'un environnement virtuel :

    - Installer virtualenv 
    - Créer un virtual env avec la commande : virtualenv venv
    (s'il n'est pas dans votre $PATH : python virtualenv.py --distribute venv)
    - Lancer le virtual env avec la commande : source ./venv/bin/activate
    
    ATTENTION : le virtual env devra être lancé à chaque fois que vous voulez lancer l'application.


2. Installation de Django :
    
    pip install django


3. Cloner le dépôt github :

    git clone https://github.com/quentinbarb/app-gestion-stage.git


4. Construire la base de données : 

    Lancer le script rebuild.sh qui construit la base et la remplit avec un jeu d'essais : ./rebuild.sh
    Il vous sera demandé de saisir un login administrateur ainsi qu'un mot de passe.
    

5. Lancer le serveur : 

    python manage.py runserver


6. Accéder à l'application :

    Vous pouvez maintenant ouvrir votre navigateur et accéder à l'application en tapant dans votre barre d'adresse :
    http://localhost:8000
    ou
    http://<IP serveur />:8000
    
    Vous pouvez alors vous logger avec le compte admin que vous avez créé avec le script rebuild.sh (toutes les permissions)
    ou utiliser l'un des comptes créés pour effectuer des tests :
    
    compte étudiant : 
      username : wroux, password : a
      
    compte enseignant : 
      username : chabin, password : a
    
    compte secrétariat : 
      username : bruletot, password : a
    
    compte responsable : 
      username : roza, password : a
      
    Interface d'administration : 
      http://localhost:8000/admin (accessible avec le compte admin que vous avez créé avec rebuild.sh)
  









    
