veuiller placer les fichiers csv 
    "listings.csv": "listing",
    "calendar.csv": "calendar",
    "reviews.csv": "reviews",
    "neighbourhoods.csv": "neighbourhoods" à importer dans la bd postgresql dans le repertoire data.

Le script d'extraction prend en compte le csv listings summary qui contient 18 colonne au lieu de 75. Le csv summary
et le détaillé contiennent le même nombre de ligne. 

listings summary : https://data.insideairbnb.com/france/ile-de-france/paris/2024-12-06/visualisations/listings.csv
