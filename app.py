import streamlit as st
import runpy

st.set_page_config(page_title="Yogendar | Developer Portfolio", layout="wide")

# ---------- DARK HEADER ----------
st.markdown("""
<h1 style='text-align:center;color:#00ADB5;'>👨‍💻 Yogendar Singh</h1>
<p style='text-align:center;'>Python • SQL • Machine Learning • Future Software Engineer</p>
""", unsafe_allow_html=True)

st.divider()

# ---------- SIDEBAR ----------
st.sidebar.title("🚀 Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home","🛠 Skills","📂 Projects","📄 Resume","📬 Contact"])

# ---------- HOME ----------
if page == "🏠 Home":
    col1,col2 = st.columns([2,1])

    with col1:
        st.subheader("About Me")
        st.write("""
        • 3rd Year Computer Science Student  
        • Strong in Python, SQL & DSA  
        • Built real ML & Data projects  
        • Preparing for placements  
        """)

        st.success("Actively seeking Software Developer role")

    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=220)

    st.divider()

    c1,c2,c3 = st.columns(3)
    c1.metric("Projects Built","3")
    c2.metric("Tech Stack","Python + SQL + ML")
    c3.metric("Status","Placement Ready")

# ---------- SKILLS ----------
elif page == "🛠 Skills":
    st.subheader("Technical Skills")

    st.write("### Programming")
    st.progress(90); st.write("Python")
    st.progress(80); st.write("Java (DSA)")
    st.progress(85); st.write("SQL")

    st.write("### Tools")
    st.write("✔ Streamlit")
    st.write("✔ Pandas")
    st.write("✔ Scikit-learn")
    st.write("✔ Git & GitHub")

# ---------- PROJECTS ----------
elif page == "📂 Projects":
    st.subheader("🚀 Live Projects")

    project = st.selectbox("Select Project",[
        "📊 Sales Analytics Dashboard",
        "🤖 AI Placement Intelligence",
        "🌐 Portfolio Info"
    ])

    st.divider()

    # ---- SALES DASHBOARD ----
    if project == "📊 Sales Analytics Dashboard":
        st.info("Real company-level sales dashboard using Python & Streamlit")
        runpy.run_path("Projects/sales_dashboard.py")
        

    # ---- ML PROJECT ----
    elif project == "🤖 AI Placement Intelligence":
        st.info("Machine Learning model predicting placement probability")
        runpy.run_path("Projects/placement_model.py")
        

    # ---- PORTFOLIO ----
    elif project == "🌐 Portfolio Info":
        st.success("This portfolio built fully using Python & Streamlit")
        st.write("Includes ML + Data + Dashboard projects")

# ---------- RESUME ----------
elif page == "📄 Resume":
    st.subheader("Download Resume")

    try:
        with open("resume.pdf","rb") as f:
            st.download_button("⬇ Download Resume",f,"Yogendar_Resume.pdf")
    except:
        st.warning("Add resume.pdf to portfolio folder")

# ---------- CONTACT ----------
elif page == "📬 Contact":
    st.subheader("Contact Me")

    name = st.text_input("Name")
    msg = st.text_area("Message")

    if st.button("Send"):
        if name and msg:
            st.success("Message sent successfully!")
        else:
            st.error("Fill all fields")

    st.divider()
    st.write("📧 Email: yourmail@gmail.com")
    st.write("💻 GitHub: github.com/yourname")
    st.write("🔗 LinkedIn: linkedin.com/in/yourname")
