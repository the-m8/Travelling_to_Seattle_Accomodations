# Disaster Response Pipeline

With the Disaster Response Pipeline, messages regarding disasters gets classified by a machine learning pipeline.

## Table of contents
1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Results](#results)
5. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

This project uses the re, nltk, sqlite3, pickle, sqlalchemie, Pandas, Numpy and some sklearn libraries. The code should run with no issues using Python versions 3.*.

## Project Motivation<a name="motivation"></a>

With this project I would like to show my Data Science and Data Engineering skills. Though especially the webpage and model adjustments were tough for me, I was thrilled to use Machine Learning Pipelines for text analysis. Although I might not have used the best model and didn't explore the dataset to every extend, I am looking forward to use Machine Learning in other Use Cases.

## File Descriptions <a name="files"></a>

This projects contains csv files of messages and categories that gets cleaned and tranformed in an ETL Pipeline. The pipeline preparation in Jupyther Notebook as well as the final ETL python pipeline can be found in the folder "data". Second, a Machine Learning pipeline trains and tests on the dataset to select the respective categories after a message input. This machine learning pipeline preparation as well as the final ML python pipeline can be found in the folder "model". Third, a webpage with an application on Disaster Response is provided with the past data and created model underlying. The python code for the webapp is provided in the folder "app".

## Results<a name="results"></a>

All results can be found after running the run.py script in the webapp under the following [link] (https://view6914b2f4-3001.udacity-student-workspaces.com/)

Please be aware that it can only be accessed through Udacity courses.

## Licensing, Authors, Acknowledgements<a name="licensing"></a>

Credits to [appen](https://appen.com/) (former Figure Eight) for the data and [Udacity](https://www.udacity.com/) for the app code where I made only minor adjustments. 
