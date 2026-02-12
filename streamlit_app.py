

import streamlit as st

st.title("Kalkulator hitung volume tabung")
import streamlit as st
import math

# Judul aplikasi
st.title("Kalkulator Volume Tabung")

st.write("Menghitung volume tabung menggunakan rumus:")
st.latex("V = \pi \times r^2 \times t")

# Input dari user
jari_jari = st.number_input("Masukkan jari-jari (r):", min_value=0.0, step=0.1)
tinggi = st.number_input("Masukkan tinggi (t):", min_value=0.0, step=0.1)

# Tombol hitung
if st.button("Hitung Volume"):
    volume = math.pi * jari_jari**2 * tinggi
    st.success(f"Volume tabung adalah: {volume:.2f}")


   

