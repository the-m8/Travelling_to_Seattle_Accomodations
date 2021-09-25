# Disaster Response Pipeline

With the Disaster Response Pipeline, messages regarding disasters gets classified by a machine learning pipeline.

## Table of contents
1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Instruction](#instructions)
5. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

This project uses the re, nltk, sqlite3, pickle, sqlalchemie, Pandas, Numpy and some sklearn libraries. The code should run with no issues using Python versions 3.*.

## Project Motivation<a name="motivation"></a>

With this project I would like to show my Data Science and Data Engineering skills. Though especially the webpage and model adjustments were tough for me, I was thrilled to use Machine Learning Pipelines for text analysis. Although I might not have used the best model and didn't explore the dataset to every extend, I am looking forward to use Machine Learning in other Use Cases.

## File Descriptions <a name="files"></a>

This projects contains csv files of messages and categories that gets cleaned and tranformed in an ETL Pipeline. The pipeline preparation in Jupyther Notebook as well as the final ETL python pipeline can be found in the folder "data". Second, a Machine Learning pipeline trains and tests on the dataset to select the respective categories after a message input. This machine learning pipeline preparation as well as the final ML python pipeline and the saved model can be found in the folder "model". Third, a webpage with an application on Disaster Response is provided with the past data and created model underlying. The python code for the webapp is provided in the folder "app".

## Instruction<a name="instructions"></a>

1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python app/run.py`

3. Go to https://view6914b2f4-3001.udacity-student-workspaces.com/

Please be aware that it can only be accessed through Udacity courses.

## Results <a name="results"></a>

below you can see some screenshots of my website:
![image](https://user-images.githubusercontent.com/84857216/134781543-292296af-2bd5-4b54-8f0b-e711cb4de285.png)
![image](https://user-images.githubusercontent.com/84857216/134781503-ba6c92c6-bec7-40c7-bd1b-d4ca23c2c6f4.png)
![image](https://user-images.githubusercontent.com/84857216/134781530-85a4e84a-73fc-42c5-be71-2ec3befbb795.png)


## Licensing, Authors, Acknowledgements<a name="licensing"></a>

Credits to [appen](https://appen.com/) (former Figure Eight) for the data and [Udacity](https://www.udacity.com/) for the app code where I made only minor adjustments. 
