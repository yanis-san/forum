# Base de données

## Tables :

Forum :
- titre
- slug
- description
- created_at

Thread :
- title
- slug
- author
- created_at
- forum foreign key
  

Message :
- content
- author
- created_at
- like
- dislike
  
  
User :
- username
- password
- email
- date de naissance
- nationalité


ForumUser :
- user foreign key
- forum foreign key

# Ne pas oublier

Rajouter l'admin d'un forum qui concerne le compte créé pour créer un forum et non un compte créé pour un thread.


## Fonctionnalités

### Afficher la liste des forums
### Créer un forum
### Supprimer un forum
### Créer un thread
### Supprimer un thread
### Création d'un compte pour créer un forum[]
### Permettre la connexion et la déconnexion d'un compte[]
### Création d'un compte pour créer des thread dans un forum spécifique
### Faire les autorisations spécifiques aux forums (à replanifier)
### Faire les autorisations spécifiques aux threads (à replanifier)


