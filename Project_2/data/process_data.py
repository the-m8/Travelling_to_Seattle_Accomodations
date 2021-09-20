import sys
import pandas as pd
import numpy as np
import sqlite3
import re
from sqlalchemy import create_engine


def load_data(messages_filepath, categories_filepath):
    
    """
    Loading raw data in message_filepath (csv) and categories_filepath (csv) and merges them into one dataframe.
    This function reads both csv-files and merges them on the column "id" into one dataframe.
   
    Parameters:
    messages_filepath, categories_filepath: csv-Files with one common column called "id".
   
    Returns:
    df (DataFrame): Merged dataframe with all information from the filepaths connected via the column "id".
  
    """
    
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    df = pd.merge(messages, categories, how='outer', on=['id'])
    
    return df


def clean_data(df):
    
    """
    Cleaning of the dataframe.
    This function cleans the dataset by splitting and transforming the column "categories" in the dataframe.
   
    Parameters:
    df (DataFrame): loaded dataframe.
   
    Returns:
    df (DataFrame): Transformed dataframe.
  
    """
    
    categories = df['categories'].str.split(';', expand=True)
    row = categories.iloc[1]
    category_colnames = list(row.apply(lambda x: re.sub('\W+[0-9]+\Z', '', x)))
    categories.columns = category_colnames
    
    for column in categories:
        categories[column] = categories[column].apply(lambda x: re.sub('[^0-9]','', x))
        categories[column] = pd.to_numeric(categories[column])
        
    df.drop(columns=['categories'], inplace=True)
    df = pd.concat([df, categories], axis=1)
    df.drop_duplicates(inplace=True)
    
    return df

    
def save_data(df, database_filename):
    
    """
    Saving the dataframe on sqlite-server.
    This function saves the transformed dataframe in sql and replaced the table if it already exists.
   
    Parameters:
    df (DataFrame): cleaned dataframe.
    database_filename: name of file where df will be stored in.
   
    Returns:
    None.
  
    """
    engine = create_engine('sqlite:///{}'.format(database_filename))
    df.to_sql('messages', engine, index=False, if_exists = 'replace') 


def main():
    
    """
    Executes the functions above.
    This function combines the functions above and executes them one after the other.
   
    Parameters:
    input needed for functions parameters: messages_filepath, categories_filepath, database_filepath
   
    Returns:
    Message whether the Workflow was successful or not.
  
    """
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