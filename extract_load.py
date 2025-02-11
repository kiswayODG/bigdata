import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import os

DB_NAME = "parisairbnb"
DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_HOST = "localhost" 
DB_PORT = "5432"

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
    isolation_level="AUTOCOMMIT"
)


csv_files = {
    "listings.csv": "listing",
    "calendar.csv": "calendar",
    "reviews.csv": "reviews",
    "neighbourhoods.csv": "neighbourhoods"
}



folder = 'data'
chunksize = 100000  


def import_csv_to_postgres(csv_file, table_name):
    try:
        file_path = os.path.join(folder, csv_file)  

        print(f"Importation de {csv_file} dans la table {table_name}...")
        
        for chunk in pd.read_csv(file_path, low_memory=False, chunksize=chunksize, dtype=str):
            
        
            if ("price" in chunk.columns) and ("adjusted_price" in chunk.columns):
                chunk['price'] = chunk['price'].fillna(0)
                chunk['adjusted_price'] = chunk['adjusted_price'].fillna(0)
                chunk["price"] = chunk["price"].replace('[\$,]', '', regex=True).astype(float).astype(int)
                chunk["adjusted_price"] = chunk["adjusted_price"].replace('[\$,]', '', regex=True).astype(float).astype(int)
                
            if ("neighbourhood_group" in chunk.columns):
                chunk['neighbourhood_group'] = chunk['neighbourhood_group'].fillna("Unknow")

            
            
            chunk.to_sql(table_name, con=engine, if_exists="append", index=False)
        
        print(f"Importation terminée pour {table_name} !\n")
    except Exception as e:
        print(f"Erreur lors de l'importation de {table_name} : {e}")


for file, table in csv_files.items():
    import_csv_to_postgres(file, table)

print("Toutes les données ont été importées avec succès !")
