from fastapi import FastAPI
import joblib
import pandas as pd 
from pydantic import BaseModel
import json

app = FastAPI()

model = joblib.load("C:/Users/DPCS6481/Documents/Projet Postgresql/Titanic/random_forest_model.joblib")


class titanic_format (BaseModel): 
    Pclass : object	
    Sex : object
    SibSp : int	
    Parch : int	
    Fare  :  float	
    Embarked : object
    civility : object
    Age_levels : object



@app.post("/score")
def prediction (data_sent:titanic_format): 
    # Convertir l'instance en dictionnaire
    data_dict = data_sent.dict()
    data = pd.DataFrame.from_dict([data_dict])
    result = model.predict(data)
    return  int(result[0]) 
#uvicorn Titanic_fastapi:app --reload


