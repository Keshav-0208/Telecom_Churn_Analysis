import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Function to calculate total minutes
def total_minutes(a, b, c, d):
    return a + b + c + d

# Sidebar for file upload
uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])
if uploaded_file is not None:
    df = load_data(uploaded_file)
else:
    df = load_data(r"TelecomChurnAnalysis.csv")

df.columns=['State', 'AccountLength', 'AreaCode', 'InternationalPlan',
       'VoiceMailPlan', 'NumberVmailMessages', 'TotalDayMinutes',
       'TotalDayCalls', 'TotalDayCharge', 'TotalEveMinutes',
       'TotalEveCalls', 'TotalEveCharge', 'TotalNightMinutes',
       'TotalNightCalls', 'TotalNightCharge', 'TotalIntlMinutes',
       'TotalIntlCalls', 'TotalIntlCharge', 'CustomerServiceCalls',
       'Churn']
df.head()
# Display data
st.write(df.head())

# Display data shape
st.write("Data Shape:", df.shape)

# Display data info
st.write("Data Info:", df.info())

# Display data columns
st.write("Data Columns:", df.columns)

# Create TotalMinutesSpent column
df["TotalMinutesSpent"] = df.apply(lambda x: total_minutes(x["TotalDayMinutes"], x["TotalEveMinutes"], x["TotalIntlMinutes"], x["TotalNightMinutes"]), axis=1)

# Plot Network usage of all users across different states
state_total_minutes = df.groupby("State")["TotalMinutesSpent"].sum()
st.subheader("Network usage of all users across different states")
st.bar_chart(state_total_minutes)

# Plot Distribution of Churned and Non Churned Users
churn_count = df["Churn"].value_counts()
st.subheader("Distribution of Churned and Non Churned Users")
# Create a pie chart using matplotlib.pyplot
plt.figure(figsize=(6, 6))
plt.pie(churn_count, labels=["Not Churned", "Churned"], autopct='%1.1f%%', startangle=90)
plt.title('Churn Distribution')
plt.axis('equal')
st.pyplot(plt)

# Plot Heatmap of correlations
corr = df.corr()
st.subheader("Heatmap of correlations")
st.write(sns.heatmap(corr, annot=True, cmap="YlGnBu"))

# Plot Number of churn and non churned users vs number of customer service calls
churn_vs_service_calls = df.groupby("CustomerServiceCalls")["Churn"].value_counts().unstack()
st.subheader("Number of churn and non churned users vs number of customer service calls")
st.line_chart(churn_vs_service_calls)

# Plot Average number of Customer Service Calls across different states
avg_service_calls = df.groupby("State")["CustomerServiceCalls"].mean()
st.subheader("Average number of Customer Service Calls across different states")
st.bar_chart(avg_service_calls)

