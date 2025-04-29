import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import os

DB_NAME = "airbnb_paris"
DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_HOST = "localhost" 
DB_PORT = "5432"

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
    isolation_level="AUTOCOMMIT"
)


csv_files = {
    
    "neighbourhoods.csv": ("neighbourhoods", None),
    "listings_t1.csv": ("listings", 1),
    "reviews_t1.csv": ("reviews", 1),
    "listings_t2.csv": ("listings", 2),
    "reviews_t2.csv": ("reviews", 2),
    "listings_t3.csv": ("listings", 3),
    "reviews_t3.csv": ("reviews", 3),
    "listings_t4.csv": ("listings", 4),
    "reviews_t4.csv": ("reviews", 4)
}



folder = 'data'
chunksize = 100000  


def import_csv_to_postgres(csv_file, table_name, trimestre):
    try:
        file_path = os.path.join(folder, csv_file)
        print(f"Importation de {csv_file} dans la table {table_name}...")

        for chunk in pd.read_csv(file_path, low_memory=False, chunksize=chunksize, dtype=str):

            
            if ("price" in chunk.columns):
                chunk['price'] = chunk['price'].fillna('0').replace('[\$,]', '', regex=True).astype(float)

            
            if trimestre:
                chunk["trimestre"] = trimestre

            
            if "neighbourhood_group" in chunk.columns:
                chunk['neighbourhood_group'] = chunk['neighbourhood_group'].fillna("Unknow")

            
            chunk.to_sql(table_name, con=engine, if_exists="append", index=False)

        print(f" Importation terminée pour {table_name} (T{trimestre if trimestre else '-'})\n")
    except Exception as e:
        print(f" Erreur lors de l'importation de {table_name} : {e}")


for file, (table, trimestre) in csv_files.items():
    import_csv_to_postgres(file, table, trimestre)

print(" Toutes les données ont été importées avec succès !")

