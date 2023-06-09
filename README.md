## Tomi
==============================
# Uthrecht house retail value prediction and deployment

This project is an exploratory, descriptive, and predictive analysis of houses in Utrecht, Netherlands. A Machine learning model was trained and deployed to predict house retail values, and the model was deployed as a fast API application.

The whole project entailing all imports, training, testing, the deployed app and real-time inference can be seen at https://github.com/SireDestiny/Utrecht-house-ml-deployment/blob/master/Structure/notebooks/Uthrecht%20house.ipynb

Note: To see the full EDA, the whole Python Notebook can be explored at https://nbviewer.org/github/SireDestiny/Utrecht-house-ml-deployment/blob/master/Structure/notebooks/Uthrecht%20house.ipynb

The test of the deployed model can be seen at https://github.com/SireDestiny/Utrecht-house-ml-deployment/blob/master/Structure/notebooks/utrecht%20house%20testing.ipynb

Directory structure of the project
------------
```
├── LICENSE
├── train`
├── README.md          <- The project description.
├── data
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── models             <- Trained and serialized model
│
├── notebooks          <- Jupyter notebooks
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.py           <- makes project pip installable (pip install -e .)  
└── src                <- Source code for use in this project.
    │
    ├─ App           
    │  └── app.py      <- Script to build the FastAPI application
    │
    ├─ Scoring script  
    │  └── train.py    <- Script to train and make inference 
    │
    └─ visualization  
       └──Importance   <-  exploratory and results oriented visual of the feature importance
```
