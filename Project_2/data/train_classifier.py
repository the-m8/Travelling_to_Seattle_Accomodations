import sys
import pandas as pd
import numpy as np
import sqlite3
import pickle
import nltk
nltk.download(['punkt', 'wordnet', 'stopwords'])
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

from sqlalchemy import create_engine
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.datasets import make_multilabel_classification
from sklearn.multioutput import MultiOutputClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.utils.multiclass import type_of_target
from sklearn.ensemble import RandomForestClassifier

def load_data(database_filepath):
    
    """
    Loading transformed data in database_filepath and split into X and y.
    This function connects to the sqlite server DisasterResponseData.db, loads the stored dataset, 
    removes the column "id" and splits the remaining columns into messages (X) and number values (y).
   
    Parameters:
    None
  
    Returns:
    array (X, Y): messages and number values.
  
    """
    
    engine = create_engine('sqlite:///{}'.format(database_filepath))
    df = pd.read_sql('SELECT * FROM messages', engine)
    df.drop(columns=['id'], inplace=True)
    X = df.message.values
    Y = df.select_dtypes(include=np.number).values
    category_names = list(df.select_dtypes(include=np.number).columns)
    return X, Y, category_names


def tokenize(text):
    
    """
    Transforming string text into arrays of words.
    This function splits strings into words, removes stopwords and lemmatize the words.
      
    Parameters:
    text (string): string input containing text.
  
    Returns:
    lemmed (array): array with separate text strings for machine learning model input.
  
    """
    tokens = word_tokenize(text.lower().strip())
    tokens = [w for w in tokens if w not in stopwords.words("english")]
    lemmed = [WordNetLemmatizer().lemmatize(w) for w in tokens]
    return lemmed


def build_model():
    
    """
    Building a prediction model.
    This function contains a pipeline that vectorizes and categorizes the model input to predict y values.
      
    Parameters:
    None
  
    Returns:
    Model Pipeline.
  
    """
    pipeline = Pipeline([
            ('vec', CountVectorizer(tokenizer=tokenize)),
            ('tfidf', TfidfTransformer()),
            ('clf', MultiOutputClassifier(RandomForestClassifier(n_estimators=5)))
        ])
    
    parameters = {'clf__estimator__max_features':['sqrt', 0.5]}

    cv = GridSearchCV(pipeline, param_grid = parameters, cv = 2, n_jobs = 6, verbose = True)

    return cv


def evaluate_model(model, X_test, Y_test, category_names):
    
    """
    Evaluate and display model results.
  
    This function predicts the values and matches them against the actual values. 
    It displays the f1 score, precision and recall in the classification report of the predicted output and shows how well the selected prediction model works.
      
    Parameters:
    model: model output from build_model
    X_test, Y_test: Test-split returned from build_model
    category_names: Unique values of Y.
  
    Returns:
    classification report: shows precision, recall, f1-score and support on different target names.
      
    """
    Y_pred = model.predict(X_test)
    for idx, column in enumerate(category_names):
        print(column)
        print(classification_report(Y_test, Y_pred))


def save_model(model, model_filepath):
    
    """
    Saving model to filepath.
    This function saves a model to a chosen filepath.
      
    Parameters:
    model: model to be saved.
    model_filepath: path where model should be saved.
  
    Returns:
    None
  
    """
    pickle.dump(model, open(model_filepath, 'wb'))


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()