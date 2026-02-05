
import streamlit as st

st.title("Kalkulator Berat Badan Ideal (BBI)")

# Input data
nama = st.text_input("Masukkan Nama")
jenis_kelamin = st.selectbox("Pilih Jenis Kelamin", ["Pria", "Wanita"])
tinggi = st.number_input("Masukkan Tinggi Badan (cm)", min_value=100, max_value=250)

# Tombol hitung
if st.button("Hitung Berat Badan Ideal"):
    if jenis_kelamin == "Pria":
        bbi = (tinggi - 100) - ((tinggi - 100) * 0.10)
    else:
        bbi = (tinggi - 100) - ((tinggi - 100) * 0.15)

    st.success(f"Halo {nama}, berat badan ideal kamu adalah **{bbi:.1f} kg**")



