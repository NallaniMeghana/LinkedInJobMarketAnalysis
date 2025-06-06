
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load and clean the dataset
df = pd.read_csv('linkedIn_Data.csv')
df.columns = [col.replace(" ", "_") for col in df.columns]  # Replace spaces with underscores

# Preview the data
print(df.head())

# Step 1: Exploring the Data

# Top 10 companies with the most job listings
sns.countplot(y=df['Company_Name'], order=df['Company_Name'].value_counts().index[:10])
plt.title('Top 10 Companies with Most Job Listings')
plt.tight_layout()
plt.show()

# Top 10 job designations
sns.countplot(y=df['Designation'], order=df['Designation'].value_counts().index[:10])
plt.title('Top 10 Most Common Job Designations')
plt.tight_layout()
plt.show()

# Top 10 locations with the most job listings
sns.countplot(y=df['Location'], order=df['Location'].value_counts().index[:10])
plt.title('Top 10 Locations with Most Job Listings')
plt.tight_layout()
plt.show()

# Step 2: Check for Missing Values
missing_values = df.isnull().sum()
print("Missing values:\n", missing_values[missing_values > 0])  # Should print nothing if no missing data

# Step 3: Skill Analysis for Top Roles
top_roles = ['Project Manager', 'Team Lead', 'Associate Tech Specialist']
filterTop = df[df["Designation"].isin(top_roles)]
skills = df.columns[10:]  # Assuming first 10 columns are meta-data
skill_aggregate = filterTop.groupby('Designation')[skills].sum().transpose()

# Top skills for each role
for role in top_roles:
    skill_aggregate[role].sort_values(ascending=False).head(5).plot(kind='bar', title=f"Top 5 Skills for {role}")
    plt.ylabel('Number of Listings')
    plt.tight_layout()
    plt.show()

# Step 4: Correlation Between LinkedIn Followers and Total Applicants
correlation = df[['LinkedIn_Followers', 'Total_applicants']].corr()
sns.heatmap(correlation, annot=True, vmin=-1, vmax=1)
plt.title("Correlation between LinkedIn Followers and Total Applicants")
plt.tight_layout()
plt.show()

# Step 5: Top Industries with Job Listings
top_industries = df['Industry'].value_counts().index[:4]
sns.barplot(x=df['Industry'].value_counts().loc[top_industries], y=top_industries, palette='viridis')
plt.title('Top 4 Industries with Most Job Listings')
plt.tight_layout()
plt.show()

# Step 6: Outliers - Total Applicants and LinkedIn Followers

# Total Applicants Distribution
sns.histplot(df['Total_applicants'], kde=True)
plt.title('Histogram of Total Applicants')
plt.tight_layout()
plt.show()

# LinkedIn Followers Distribution
sns.histplot(df['LinkedIn_Followers'], kde=True)
plt.title('Histogram of LinkedIn Followers')
plt.tight_layout()
plt.show()
