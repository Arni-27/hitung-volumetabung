import streamlit as st

st.title("💪 Kalkulator Berat Badan Ideal (BMI)")

# Input user
nama = st.text_input("Masukkan nama Anda")
berat = st.number_input("Berat badan (kg)", min_value=1.0)
tinggi = st.number_input("Tinggi badan (cm)", min_value=1.0)

if st.button("Hitung BMI"):
    tinggi_m = tinggi / 100  # konversi cm ke meter
    bmi = berat / (tinggi_m ** 2)

    st.subheader(f"Halo, {nama} 👋")
    st.write(f"**BMI Anda:** {bmi:.2f}")

    if bmi < 18.5:
        st.warning("Kategori: Kurus")
    elif bmi < 25:
        st.success("Kategori: Ideal")
    elif bmi < 30:
        st.warning("Kategori: Overweight")
    else:
        st.error("Kategori: Obesitas")

