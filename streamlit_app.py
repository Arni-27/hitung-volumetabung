

    import streamlit as st

st.title("Kalkulator BMI")

# Input
nama = st.text_input("Masukkan Nama")
berat = st.number_input("Masukkan Berat Badan (kg)", min_value=1.0)
tinggi = st.number_input("Masukkan Tinggi Badan (cm)", min_value=50.0)

# Tombol hitung
if st.button("Hitung BMI"):
    tinggi_m = tinggi / 100  # cm ke meter
    bmi = berat / (tinggi_m ** 2)

    # Kategori BMI
    if bmi < 18.5:
        kategori = "Kurus"
    elif bmi < 25:
        kategori = "Normal"
    elif bmi < 30:
        kategori = "Gemuk"
    else:
        kategori = "Obesitas"

    st.success(f"Halo {nama}, BMI kamu adalah **{bmi:.2f}**")
    st.info(f"Kategori: **{kategori}**")

        

   

