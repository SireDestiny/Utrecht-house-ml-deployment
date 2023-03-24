
import numpy as np
import pandas as pd 
import sklearn
import pickle
from sklearn.ensemble import RandomForestRegressor 
from sklearn.model_selection import train_test_split



# And the value that needs to be predicted (retailvalue)

# Load data
df = pd.read_csv('./utrechthousinglarge.csv')

# Independent variables
features = ['zipcode',	'lot-len',	'lot-area', 'house-area',	'garden-size',	'y-coor', 'energy-eff']

x = df[features]
y = df['retailvalue']

# Call fit method to train the model using the independent variables.
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state = 52, test_size = 20)

#Create Gradient Boosting Regression model
model = RandomForestRegressor()
model.fit(x_train, y_train) #Indep variables, dep. variable to be predicted

prediction_test = model.predict(x_test)    

# load model
import pickle
pickle.dump(model, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))
