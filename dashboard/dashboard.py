import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


day_df = pd.read_csv("data/day.csv")
hour_df = pd.read_csv("data/hour.csv")

day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

min_date = day_df["dteday"].min()
max_date = day_df["dteday"].max()

st.set_page_config(layout="wide")
st.title("Dashboard Peminjaman Sepeda")

with st.sidebar:
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

filtered_day_df = day_df[(day_df["dteday"] >= pd.to_datetime(start_date)) & 
                         (day_df["dteday"] <= pd.to_datetime(end_date))]

filtered_hour_df = hour_df[(hour_df["dteday"] >= pd.to_datetime(start_date)) & 
                           (hour_df["dteday"] <= pd.to_datetime(end_date))]

daily_bike_rentals = filtered_day_df.groupby('weekday')['cnt'].sum()
hourly_bike_rentals = filtered_hour_df.groupby('hr')['cnt'].sum()

st.subheader("Hari dengan peminjaman sepeda paling banyak dalam seminggu")

fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(x=daily_bike_rentals.index, y=daily_bike_rentals.values, palette='Blues_d', ax=ax)
ax.set_title('Total Peminjaman Sepeda Berdasarkan Hari dalam Seminggu')
ax.set_xlabel('Hari dalam Seminggu')
ax.set_ylabel('Total Peminjaman Sepeda')
ax.set_xticks(range(7))
ax.set_xticklabels(['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'])
st.pyplot(fig)

st.subheader("Jam dengan peminjaman sepeda paling banyak dalam sehari")

fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(x=hourly_bike_rentals.index, y=hourly_bike_rentals.values, palette='viridis', ax=ax)
ax.set_title('Jam dengan peminjaman sepeda paling banyak dalam sehari')
ax.set_xlabel('Jam dalam Sehari')
ax.set_ylabel('Total Peminjaman Sepeda')
ax.set_xticks(range(0, 24, 1))
st.pyplot(fig)

st.subheader("Clustering Waktu Peminjaman Sepeda")

def categorize_time(hour):
    if 6 <= hour < 12:
        return 'Pagi'
    elif 12 <= hour < 18:
        return 'Siang'
    else:
        return 'Malam'

hourly_rentals = hour_df.groupby('hr')['cnt'].sum().reset_index()
hourly_rentals['cluster'] = hourly_rentals['hr'].apply(categorize_time)

fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x=hourly_rentals['hr'], y=hourly_rentals['cnt'], hue=hourly_rentals['cluster'], palette='coolwarm', ax=ax)
ax.set_title('Clustering Waktu Peminjaman Sepeda', fontsize=14)
ax.set_xlabel('Jam', fontsize=12)
ax.set_ylabel('Total Peminjaman Sepeda', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.7)
st.pyplot(fig)

