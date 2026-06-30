import pandas as pd

def transform_product(product_df):
    df = product_df.copy()

    df = df.rename(columns= {
        'id' : 'product_id',
        'title' : 'product_name',
        'price' : 'product_price',
        'category' : 'product_category',
        'description' : 'product_info'
    })

    df = df[[
        'product_id',
        'product_name',
        'product_price',
        'product_category',
        'product_info'
    ]]

    df['product_price'] = df['product_price'].astype(float)

    return df

def transform_user(user_df):
    df = user_df.copy()

    df[['firstname', 'lastname']] = df['username'].str.split('_', expand=True)

    df = df.rename(columns= {
        'id' : 'user_id'
    })

    df = df[[
        'user_id',
        'username',
        'firstname',
        'lastname',
        'email',
        'password'
    ]]

    return df