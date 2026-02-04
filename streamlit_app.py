import streamlit as st
from fractions import Fraction

st.title("🧮 Kalkulator Pecahan Biasa")

st.write("Masukkan dua pecahan, lalu pilih operasi hitungnya.")

# Input pecahan pertama
st.subheader("Pecahan Pertama")
a = st.number_input("Pembilang 1", step=1, format="%d")
b = st.number_input("Penyebut 1", min_value=1, step=1, format="%d")

# Input pecahan kedua
st.subheader("Pecahan Kedua")
c = st.number_input("Pembilang 2", step=1, format="%d")
d = st.number_input("Penyebut 2", min_value=1, step=1, format="%d")

# Pilih operasi
operasi = st.selectbox(
    "Pilih Operasi",
    ("Penjumlahan (+)", "Pengurangan (-)", "Perkalian (×)", "Pembagian (÷)")
)

if st.button("Hitung"):
    f1 = Fraction(a, b)
    f2 = Fraction(c, d)

    if operasi == "Penjumlahan (+)":
        hasil = f1 + f2
    elif operasi == "Pengurangan (-)":
        hasil = f1 - f2
    elif operasi == "Perkalian (×)":
        hasil = f1 * f2
    else:
        if c == 0:
            st.error("Tidak bisa dibagi dengan nol ❌")
            st.stop()
        hasil = f1 / f2

    st.success(f"Hasil = {hasil}")
    st.write(f"Dalam desimal = {float(hasil):.3f}")


