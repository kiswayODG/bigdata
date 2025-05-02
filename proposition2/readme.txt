veuiller placer les fichiers csv 
    "listings.csv": "listing",
    "calendar.csv": "calendar",
    "reviews.csv": "reviews",
    "neighbourhoods.csv": "neighbourhoods" à importer dans la bd postgresql dans le repertoire data.

Le script d'extraction prend en compte le csv listings summary qui contient 18 colonne au lieu de 75. Le csv summary
et le détaillé contiennent le même nombre de ligne. 


les liens vers les données:

1er trimestre de 2024:
listings -> https://data.insideairbnb.com/france/ile-de-france/paris/2024-03-16/visualisations/listings.csv.gz

2eme trimestre de 2024:
listings -> https://data.insideairbnb.com/france/ile-de-france/paris/2024-06-10/visualisations/listings.csv.gz

3eme trimestre de 2024:
 listings -> https://data.insideairbnb.com/france/ile-de-france/paris/2024-09-06/visualisations/listings.csv.gz



quebec listings -> https://data.insideairbnb.com/canada/qc/quebec-city/2025-03-04/data/listings.csv.gz



les données sur neighbourhoods reste inchangé tout le long de l'année
neighbourhoods -> 'https://data.insideairbnb.com/france/ile-de-france/paris/2024-12-06/visualisations/neighbourhoods.csv'

installation pyspark sur windows -> https://www.machinelearningplus.com/pyspark/install-pyspark-on-windows/

difficulté rencontré: https://stackoverflow.com/questions/70512835/how-to-fix-connection-refused-error-winerror-10061-on-pyspark-jupyter-noteboo