import streamlit as st
import pickle

# Load the model
model = pickle.load(open('projetBekouan.pkl', 'rb'))
st.title('PREDICTION DU SENTIENT EN FONCTION D' 'UN TWEET')

st.header('Veuillez renseigner les données en entrée')

#Données entrée par l'utilisateur
pannee = st.number_input('année du tweet')
pmois = st.slider('mois du tweet', 1,12)
pjour = st.slider('jour du tweet', 1,31)
psite = st.radio('plateforme :',('Facebook', 'Twitter', 'Instagram'))
pperiode = st.radio('période :', ('matin','midi', 'soir'))

# Predict house price
site = 0
periode = 0
if st.button('Prédire le sentiment'):
    if psite == 'Facebook':
        site = 1
    elif psite == 'Instagram':
        site = 2
    else :
        site = 0

if pperiode == 'midi':
    periode = 1
elif pperiode == 'soir':
    periode = 2
else:
    periode = 2

prediction = model.predict([[pannee, pmois, pjour, periode,site]])
lib_pred = ''
if prediction ==0 :
    lib_pred = 'positive'
elif lib_pred == 'Neutre':
    lib_pred = 'Négative'
else:
    lib_pred = prediction
st.write(f'La prédiction du sentiment : ${lib_pred}')