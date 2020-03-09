
# Installation api

1. Python et pip doivent être disponibles sur l'environnement
1. lancer l'install de falsk-restfull: `pip install restful-api`

# Lancement serveur

Se placer dans le répertoire contenant le fichier "intervention.py" et lancer le serveur: `python ./intervention.py`

Les données sont sauvegardées en mémoire et réinitialisées à chaque redémarrage du serveur

# Divers

Les données présentes à l'initialisation soit déclarées en début de fichier : 

```
TODOS = {
    'intervention_1': {'libelle': 'build an API', 'description': 'do the exercice', 'nom_intervenant': 'Adrian', 'lieu': 'bureau', 'date': '01-01-1970' },
    'intervention_2': {'libelle': 'acheter le pain', 'description': 'trouver un truc dans lequel mettre mon pat&eacute;', 'nom_intervenant': 'Sebastien', 'lieu': 'boulangerie', 'date': '02-03-2020' },
    'intervention_3': {'libelle': 'Trouver un emploi', 'description': '', 'nom_intervenant': 'Adrian', 'lieu': 'Nantes', 'date': '03-03-2020' },
}
```

L'adresse et le port d'écoute du serveur sont précisés lors du lancement de celui-ci :

```
app.run(host="0.0.0.0", port=8080,debug=True)
```

Le répertoire "examples" contient des exemples de requêtes postman pour les opérations CRUD sur l'api.