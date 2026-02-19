import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sales Analytics Dashboard", layout="wide")

st.title("📊 Company Sales Analytics Dashboard")

# load data
df = pd.read_csv("sales.csv")

# sidebar filters
st.sidebar.header("Filter Data")
region_filter = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

product_filter = st.sidebar.multiselect(
    "Select Product",
    options=df["Product"].unique(),
    default=df["Product"].unique()
)

filtered_df = df[
    (df["Region"].isin(region_filter)) &
    (df["Product"].isin(product_filter))
]

# metrics row
total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
best_region = filtered_df.groupby("Region")["Sales"].sum().idxmax()
best_product = filtered_df.groupby("Product")["Sales"].sum().idxmax()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"₹{total_sales}")
col2.metric("Total Profit", f"₹{total_profit}")
col3.metric("Top Region", best_region)
col4.metric("Top Product", best_product)

st.divider()

# charts
col5, col6 = st.columns(2)

with col5:
    st.subheader("Sales by Region")
    region_sales = filtered_df.groupby("Region")["Sales"].sum()
    st.bar_chart(region_sales)

with col6:
    st.subheader("Sales by Product")
    product_sales = filtered_df.groupby("Product")["Sales"].sum()

    fig, ax = plt.subplots()
    ax.pie(product_sales, labels=product_sales.index, autopct="%1.1f%%")
    st.pyplot(fig)

st.divider()

st.subheader("Filtered Data")
st.dataframe(filtered_df)

st.success("🔥 Professional Dashboard Ready")
