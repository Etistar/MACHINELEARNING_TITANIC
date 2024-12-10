import streamlit as st
import requests
import pandas as pd
import json

# Définition de l'URL de l'API
url = "http://127.0.0.1:8000/score"

# Ajouter le logo dans la barre latérale
st.sidebar.image("C:/Users/DPCS6481/Documents/orange.PNG", use_column_width=True)

# Charger les données
data = pd.read_csv(r'C:\Users\DPCS6481\Downloads\archive (2)\ChanDarren_RaiTaran_Lab2a.csv', delimiter =",")
Name = data.Name.str.split(",", expand=True)
Name.columns = ["Country", "Name"]
data["civility"] = Name.Name.str.split(".", expand=True)[0]

# Définition des options pour les variables
options1 = {
    "Pclass": [str(element) for element in data.Pclass.unique()],
    "Sex": [str(element) for element in data.Sex.unique()],
    "SibSp": [min(data.SibSp), max(data.SibSp)],
    "Parch": [min(data.Parch), max(data.Parch)],
    "Fare": [min(data.Fare), max(data.Fare)],
    "Embarked": [str(element) for element in data.Embarked.unique()],
    "civility": [str(element) for element in data.civility.unique()],
    "Age_levels": ["(0, 10]", "(10, 25]", "(25, 50]", "(50, 100]"]
}

options = {
    "Pclass": [str(element) for element in data.Pclass.unique()],
    "Sex": [str(element) for element in data.Sex.unique()],
    "Embarked": [str(element) for element in data.Embarked.unique()],
    "civility": [str(element) for element in data.civility.unique()],
    "Age_levels": ["(0, 10]", "(10, 25]", "(25, 50]", "(50, 100]"]
}

# Création des boîtes glissantes et des listes déroulantes
selected_options = {}
for variable, values in options1.items():
    if variable in ["Parch", "SibSp", "Fare"]:
        min_value, max_value = values
        selected_options[variable] = st.slider(f"Sélectionnez une valeur pour {variable}", min_value, max_value)
        st.write(f"La valeur sélectionnée pour {variable} est : {selected_options[variable]}")
    else:
        selected_options[variable] = st.selectbox(variable, values)

# Ajouter un bouton pour envoyer la requête
if st.button("Envoyer la requête"):
    # Appel de l'API avec les données sélectionnées
    response = requests.post(url, json=selected_options)
    
    # Affichage du résultat de la prédiction
    st.write("Résultat de la prédiction :", response.text)
