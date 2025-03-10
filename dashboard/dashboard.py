import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


day_df = pd.read_csv("data/day.csv")
hour_df = pd.read_csv("data/hour.csv")

day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

daily_bike_rentals = day_df.groupby('weekday')['cnt'].sum()

hourly_bike_rentals = hour_df.groupby('hr')['cnt'].sum()

st.set_page_config(layout="wide")
st.title("Dashboard Peminjaman Sepeda")

st.subheader("Hari dengan peminjaman sepeda paling banyak dalam seminggu")

fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(x=daily_bike_rentals.index, y=daily_bike_rentals.values, palette='Blues_d', ax=ax, hue=None, legend=False)
ax.set_title('Total Peminjaman Sepeda Berdasarkan Hari dalam Seminggu')
ax.set_xlabel('Hari dalam Seminggu')
ax.set_ylabel('Total Peminjaman Sepeda')
ax.set_xticks(range(7))
ax.set_xticklabels(['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'])
st.pyplot(fig)

st.subheader("Jam paling sering dipinjam dalam sehari")

fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(x=hourly_bike_rentals.index, y=hourly_bike_rentals.values, palette='viridis', ax=ax, hue=None, legend=False)
ax.set_title('Jam dengan peminjaman sepeda paling banyak dalam sehari')
ax.set_xlabel('Jam dalam Sehari')
ax.set_ylabel('Total Peminjaman Sepeda')
ax.set_xticks(range(0, 24, 1))
st.pyplot(fig)
