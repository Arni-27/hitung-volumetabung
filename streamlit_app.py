import streamlit as st
import math

st.title("_menghitung_ is :blue[volume tabung] :rocket:")


r = st.number_input("masukan jari-jari (cm): ",0)
t = st.number_input("masukan tinggi (cm): ",0)
if st button("hitung volume",type="primary"):
  v = math.pi**2)*t
  st.succes(f'volume tabung adalah (v:.2f)')
