from ETL.extract import extract_product, extract_user
from ETL.transform import transform_product, transform_user
from ETL.load import load_to_postgres

def run_pipeline():
    print("Starting pipeline")

    product_df = extract_product()
    user_df = extract_user()

    print("Starting transformation")

    product_df = transform_product(product_df)
    user_df = transform_user(user_df)

    print("Loading to postgres")

    load_to_postgres(product_df, 'products')
    load_to_postgres(user_df, 'users')

    print("ETL pipeline completed")

if __name__ == '__main__':
    run_pipeline()
