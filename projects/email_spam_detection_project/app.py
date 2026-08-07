import streamlit as st
import pickle

with open("spam_model.pkl","rb") as f:
    model= pickle.load(f)

st.title("email spam detection")
message=st.text_area("enter your email message : ")

if st.button("Predict"):
    prediction=model.predict([message])[0]
    probability=model.predict_proba([message])[0]

    if prediction == 1:
        st.error("spam email")
    else:
        st.success("safe email")

    st.write(f"safe probability : {probability[0]*100:.2f}%")
    st.write(f"safe probability : {probability[1]*100:.2f}%")



