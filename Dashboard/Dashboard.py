import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import streamlit as st

#melakukan import data dari repository github
Day_df=pd.read_csv("https://raw.githubusercontent.com/Zakyybangkit/Submission/main/Data/day.csv")
Day_df

# Set page title
st.title("Weather Analysis Dashboard")

# Sidebar - Settings
st.sidebar.header("Settings")
selected_weathersit = st.sidebar.multiselect("Select Weathersit", Day_df['weathersit'].unique(), default=Day_df['weathersit'].unique())
selected_variable = st.sidebar.selectbox("Select Variable", ['temp', 'hum', 'windspeed'])

# Filter data based on selected settings
filtered_data = Day_df[Day_df['weathersit'].isin(selected_weathersit)]

# Calculate correlation
correlation_selected_variable = filtered_data[selected_variable].corr(filtered_data['cnt'])

# Plot bar chart for cnt by weathersit
cnt_by_weathersit = filtered_data.groupby('weathersit')['cnt'].sum()
plt.bar(cnt_by_weathersit.index, cnt_by_weathersit.values, color='skyblue')
plt.xlabel('Weathersit')
plt.ylabel('Jumlah cnt')
plt.title('Jumlah cnt berdasarkan Kategori Weathersit')
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

# Plot scatter plot for selected variable vs cnt
plt.figure(figsize=(8, 6))
sns.scatterplot(x=selected_variable, y='cnt', data=filtered_data, alpha=0.7)
plt.xlabel(selected_variable.capitalize())
plt.ylabel('cnt')
plt.title(f'Scatter Plot: {selected_variable.capitalize()} vs cnt')
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

# Display correlation information
st.write(f"Korelasi antara variabel {selected_variable} dan cnt: {correlation_selected_variable:.2f}")