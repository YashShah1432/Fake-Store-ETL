from sqlalchemy import create_engine
from config import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD
)

def load_to_postgres(df, table_name):
    engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

    df.to_sql(table_name, engine, if_exists = 'replace', index = False)

    print("Data loaded to postgres successfully")