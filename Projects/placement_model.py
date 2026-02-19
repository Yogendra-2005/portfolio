import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

st.set_page_config(page_title="AI Placement Intelligence", layout="wide")

# --------- DARK HEADER ----------
st.markdown("<h1 style='text-align:center;color:#00ADB5;'>🤖 AI Placement Intelligence Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Predict placement chances using Machine Learning</p>", unsafe_allow_html=True)

# --------- DATASET ----------
data = {
    "CGPA":[7.5,8.2,6.8,9.0,5.5,8.5,6.0,7.8,8.9,5.8,7.2,6.5,8.7,9.1,6.2],
    "IQ":[110,120,105,130,95,125,100,115,128,98,108,102,132,135,101],
    "Communication":[7,8,6,9,5,8,6,7,9,5,7,6,9,9,6],
    "Placed":[1,1,0,1,0,1,0,1,1,0,1,0,1,1,0]
}
df = pd.DataFrame(data)

# --------- MODEL ----------
X = df[["CGPA","IQ","Communication"]]
y = df["Placed"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = LogisticRegression()
model.fit(X_train,y_train)

acc = accuracy_score(y_test, model.predict(X_test))

# --------- METRICS ----------
col1,col2,col3 = st.columns(3)
col1.metric("Model Accuracy", f"{round(acc*100,2)}%")
col2.metric("Dataset Size", len(df))
col3.metric("Algorithm", "Logistic Regression")

st.divider()

# --------- CHARTS ----------
c1,c2 = st.columns(2)

with c1:
    st.subheader("Placement Distribution")
    fig, ax = plt.subplots()
    df["Placed"].value_counts().plot(kind="pie", autopct="%1.1f%%",
                                     labels=["Placed","Not Placed"], ax=ax)
    st.pyplot(fig)

with c2:
    st.subheader("Feature Importance")
    importance = model.coef_[0]
    features = ["CGPA","IQ","Communication"]
    fig2, ax2 = plt.subplots()
    ax2.barh(features, importance)
    st.pyplot(fig2)

st.divider()

# --------- SIDEBAR PREDICTION ----------
st.sidebar.header("🎓 Enter Student Data")

cgpa = st.sidebar.slider("CGPA",0.0,10.0,7.0)
iq = st.sidebar.slider("IQ Score",80,150,110)
comm = st.sidebar.slider("Communication",1,10,7)

if st.sidebar.button("Predict Placement"):
    prob = model.predict_proba([[cgpa,iq,comm]])[0][1]
    result = model.predict([[cgpa,iq,comm]])[0]

    st.subheader("Prediction Result")

    st.write(f"### Placement Probability: {round(prob*100,2)}%")

    # progress bar
    st.progress(int(prob*100))

    if result==1:
        st.success("🎉 HIGH chance of placement")
    else:
        st.error("⚠ LOW chance of placement")

st.divider()

# --------- MULTI STUDENT CHECK ----------
st.subheader("📂 Upload CSV to Predict Multiple Students")

uploaded = st.file_uploader("Upload CSV with CGPA, IQ, Communication", type=["csv"])

if uploaded:
    new_df = pd.read_csv(uploaded)
    preds = model.predict(new_df)
    new_df["Prediction"] = preds
    st.dataframe(new_df)
    st.success("Predictions generated successfully!")

st.divider()
st.caption("Built by Yogendar | Python • ML • Streamlit")
