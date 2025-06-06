import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
st.set_page_config(page_title="LinkedIn Job Analysis", layout="wide")
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://www.transparenttextures.com/patterns/cubes.png");
        background-color: #f0f8ff;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.title("📊 LinkedIn Tech Job Market Analysis")

# Sidebar Navigation
st.sidebar.title("📂 InsightBar")
page = st.sidebar.selectbox(
    "Go to Section",
    (
        "Upload Dataset",
        "Show Dataset",
        "Top 10 Companies",
        "Top 10 Designations",
        "Top 10 Locations",
        "Correlation Heatmap",
        "Skills - Project Manager",
        "Skills - Team Lead",
        "Skills - Associate Tech Specialist",
        "Outlier Distributions"
    )
)

# File Input
file = st.text_input("Enter Dataset File Path or URL")
df = None

if st.button("Upload"):
    try:
        df = pd.read_csv(file)
        df.columns = [col.replace(" ", "_") for col in df.columns]
        st.success("✅ File uploaded successfully.")
    except FileNotFoundError:
        st.error("❌ File or URL not found. Please check and try again.")
    except Exception as e:
        st.error(f"❌ Error loading file: {e}")

# After dataset is loaded
if 'df' in locals() and df is not None:

    if page == "Show Dataset":
        st.subheader("📌 Dataset Preview")
        st.dataframe(df.head())

    elif page == "Top 10 Companies":
        st.subheader("🏢 Top 10 Companies with Most Job Listings")
        fig1, ax1 = plt.subplots()
        sns.countplot(y=df['Company_Name'], order=df['Company_Name'].value_counts().index[:10], ax=ax1)
        st.pyplot(fig1)

    elif page == "Top 10 Designations":
        st.subheader("💼 Top 10 Most Common Job Designations")
        fig2, ax2 = plt.subplots()
        sns.countplot(y=df['Designation'], order=df['Designation'].value_counts().index[:10], ax=ax2)
        st.pyplot(fig2)

    elif page == "Top 10 Locations":
        st.subheader("📍 Top 10 Locations with Most Job Listings")
        fig3, ax3 = plt.subplots()
        sns.countplot(y=df['Location'], order=df['Location'].value_counts().index[:10], ax=ax3)
        st.pyplot(fig3)

    elif page == "Correlation Heatmap":
        st.subheader("🔗 Correlation Between LinkedIn Followers and Applicants")
        corr = df[['LinkedIn_Followers', 'Total_applicants']].corr()
        fig4, ax4 = plt.subplots()
        sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1, ax=ax4)
        st.pyplot(fig4)

    elif page == "Skills - Project Manager":
        st.subheader("🚀 Top Skills for Project Manager")
        filtered = df[df['Designation'] == 'Project Manager']
        skills = df.columns[10:]
        skill_data = filtered[skills].sum()
        fig_pm, ax_pm = plt.subplots()
        skill_data.sort_values(ascending=False).head(5).plot(kind='bar', ax=ax_pm)
        ax_pm.set_ylabel('Number of Listings')
        st.pyplot(fig_pm)

    elif page == "Skills - Team Lead":
        st.subheader("🚀 Top Skills for Team Lead")
        filtered = df[df['Designation'] == 'Team Lead']
        skills = df.columns[10:]
        skill_data = filtered[skills].sum()
        fig_tl, ax_tl = plt.subplots()
        skill_data.sort_values(ascending=False).head(5).plot(kind='bar', ax=ax_tl)
        ax_tl.set_ylabel('Number of Listings')
        st.pyplot(fig_tl)

    elif page == "Skills - Associate Tech Specialist":
        st.subheader("🚀 Top Skills for Associate Tech Specialist")
        filtered = df[df['Designation'] == 'Associate Tech Specialist']
        skills = df.columns[10:]
        skill_data = filtered[skills].sum()
        fig_ats, ax_ats = plt.subplots()
        skill_data.sort_values(ascending=False).head(5).plot(kind='bar', ax=ax_ats)
        ax_ats.set_ylabel('Number of Listings')
        st.pyplot(fig_ats)

    elif page == "Outlier Distributions":
        st.subheader("📉 Outlier Distributions")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Total Applicants**")
            fig5, ax5 = plt.subplots()
            sns.histplot(df['Total_applicants'], kde=True, ax=ax5)
            st.pyplot(fig5)

        with col2:
            st.markdown("**LinkedIn Followers**")
            fig6, ax6 = plt.subplots()
            sns.histplot(df['LinkedIn_Followers'], kde=True, ax=ax6)
            st.pyplot(fig6)

else:
    if page != "Upload Dataset":
        st.warning("📎 Please upload a valid dataset to access this section.")

