import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.sidebar.title("Belajar Analisis Data\n Bareng Dicoding")

day_df = pd.read_csv('../data/day.csv')  
hour_df = pd.read_csv('../data/hour.csv')  

data_choice = st.selectbox("Pilih Data yang Ingin Dilihat", ("Harian", "Jam"))

if data_choice == "Harian":
    st.title("Analisis Peminjaman Sepeda Harian")
    st.write(day_df.describe(include="all"))  # Menampilkan data harian

    with st.expander("Informasi Data Harian"):
        st.markdown("""
        **Data Harian**\n
- Rata-rata pada kolom cuaca menunjukkan nilai 1.39. Nilai tersebut menunjukkan pengaruh cuaca terhadap jumlah peminjam sepeda, dimana peminjam sepeda lebih memilih cuaca yang cerah, sedikit awan, dan atau berawan sebagian.

- Rata-rata pada kolom musim menunjukkan nilai 2.49. Hal tersebut menunjukkan bahwa jumlah peminjam sepeda lebih banyak pada musim panas dan musim gugur, yang mana berarti merupakan musim yang paling sesuai untuk bersepeda.
        """)

    # Visualisasi pengaruh cuaca terhadap jumlah peminjaman sepeda
    st.subheader('Pengaruh Cuaca terhadap Jumlah Peminjaman Sepeda')
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='weathersit', y='cnt', data=day_df)
    plt.title('Pengaruh Cuaca terhadap Jumlah Peminjaman Sepeda')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Jumlah Peminjaman Sepeda')
    plt.xticks(ticks=[0, 1, 2, 3], 
           labels=['Cerah', 'Kabut + Berawan', 'Hujan Ringan', 'Hujan Berat'])
    plt.grid(axis='y')
    st.pyplot(plt)


    # Visualisasi pola musiman peminjaman sepeda
    st.subheader('Pola Musiman dalam Peminjaman Sepeda')
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='season', y='cnt', data=day_df, estimator='mean')
    plt.title('Pola Musiman dalam Peminjaman Sepeda')
    plt.xlabel('Musim')
    plt.ylabel('Jumlah Peminjaman Sepeda (Rata-rata)')
    plt.xticks(ticks=[1, 2, 3, 4], 
           labels=['Musim Semi', 'Musim Panas', 'Musim Gugur', 'Musim Dingin'])
    plt.grid()
    st.pyplot(plt)

else:
    st.title("Analisis Peminjaman Sepeda Per Jam")
    st.write(hour_df.describe(include="all"))  # Menampilkan data per jam

    with st.expander("Informasi Data Perjam"):
        st.markdown("""
        **Data Perjam**\n
- Rata-rata pada kolom cuaca menunjukkan nilai 1.42. Nilai tersebut menunjukkan pengaruh cuaca terhadap jumlah peminjam sepeda, dimana peminjam sepeda lebih memilih cuaca yang cerah, sedikit awan, dan atau berawan sebagian.

- Rata-rata pada kolom musim menunjukkan nilai 2.50. Hal tersebut menunjukkan bahwa jumlah peminjam sepeda lebih banyak pada musim panas dan musim gugur, yang mana berarti merupakan musim yang paling sesuai untuk bersepeda.
        """)

    # Visualisasi pengaruh cuaca terhadap jumlah peminjaman sepeda per jam
    st.subheader('Pengaruh Cuaca terhadap Jumlah Peminjaman Sepeda Per Jam')
    plt.figure(figsize=(10, 6))
    sns.countplot(x='weathersit', data=hour_df)
    plt.title('Pengaruh Cuaca terhadap Jumlah Peminjaman Sepeda Per Jam')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Jumlah Peminjaman Sepeda')
    plt.xticks(ticks=[0, 1, 2, 3], 
            labels=['Cerah', 'Kabut + Berawan', 'Hujan Ringan', 'Hujan Berat'])
    plt.grid(axis='y')
    st.pyplot(plt)


    # Visualisasi pola musiman peminjaman sepeda per jam
    st.subheader('Pola Musiman dalam Peminjaman Sepeda Per Jam')
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='season', y='cnt', data=hour_df, estimator='mean')
    plt.title('Pola Musiman dalam Peminjaman Sepeda Per Jam')
    plt.xlabel('Musim')
    plt.ylabel('Jumlah Peminjaman Sepeda (Rata-rata)')
    plt.xticks(ticks=[1, 2, 3, 4], 
           labels=['Musim Semi', 'Musim Panas', 'Musim Gugur', 'Musim Dingin'])
    plt.grid()
    st.pyplot(plt)

with st.expander("Kesimpulan"):
        st.markdown("""
        **Dapat disimpulkan:**\n
- Cuaca memiliki pengaruh terhadap jumlah peminjam sepeda, yang mana peminjam sepeda lebih nyaman apabila bersepeda di cuaca yang cerah dan sedikit berawan.

- Terdapat pola musiman dalam peminjaman sepeda, terjadi peningkatan drastis peminjaman sepeda pada saat memasuki musim panas dan terus meningkat sampai pada musim gugur. Kemudian akan kembali penurun pada musim dingin.
        """)