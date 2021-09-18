import sys
import pandas as pd
import numpy as np
import sqlite3
import re
from sqlalchemy import create_engine


def load_data(messages_filepath, categories_filepath):
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    return pd.merge(messages, categories, how='outer', on=['id'])


def clean_data(df):
    categories = df['categories'].str.split(';', expand=True)
    row = categories.iloc[1]
    category_colnames = list(row.apply(lambda x: re.sub('\W+[0-9]+\Z', '', x)))
    categories.columns = category_colnames
    for column in categories:
        categories[column] = categories[column].apply(lambda x: re.sub('[^0-9]','', x))
        categories[column] = pd.to_numeric(categories[column])
    df.drop(columns=['categories'], inplace=True)
    df = pd.concat([df, categories], axis=1)
    return df.drop_duplicates(inplace=True)


def save_data(df, database_filename):
    engine = create_engine('sqlite:///DisasterResponseData.db')
    return df.to_sql(database_filename, engine, index=False, if_exists = 'replace')  


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()
