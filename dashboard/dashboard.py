import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

# Convert date column to datetime
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

# Calculate bike rentals per day
daily_bike_rentals = day_df.groupby('weekday')['cnt'].sum()

# Calculate bike rentals per hour
hourly_bike_rentals = hour_df.groupby('hr')['cnt'].sum()

# Streamlit Dashboard
st.set_page_config(layout="wide")
st.title("Dashboard Peminjaman Sepeda")

# Penjelasan Pertanyaan 1: Kapan peminjaman sepeda paling banyak dalam seminggu?
st.subheader("Hari dengan peminjaman sepeda paling banyak dalam seminggu")

# Plot rentals per weekday
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(x=daily_bike_rentals.index, y=daily_bike_rentals.values, palette='Blues_d', ax=ax, hue=None, legend=False)
ax.set_title('Total Peminjaman Sepeda Berdasarkan Hari dalam Seminggu')
ax.set_xlabel('Hari dalam Seminggu')
ax.set_ylabel('Total Peminjaman Sepeda')
ax.set_xticks(range(7))
ax.set_xticklabels(['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'])
st.pyplot(fig)

# Penjelasan Pertanyaan 2: Pada jam berapa sepeda paling sering dipinjam dalam sehari?
st.subheader("Jam paling sering dipinjam dalam sehari")

# Plot rentals per hour
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(x=hourly_bike_rentals.index, y=hourly_bike_rentals.values, palette='viridis', ax=ax, hue=None, legend=False)
ax.set_title('Jam dengan peminjaman sepeda paling banyak dalam sehari')
ax.set_xlabel('Jam dalam Sehari')
ax.set_ylabel('Total Peminjaman Sepeda')
ax.set_xticks(range(0, 24, 1))
st.pyplot(fig)
