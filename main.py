import streamlit as st 

st.title(""" 
Jejes Harus Olahraga  
Biar Langsing 
""")

tanya =st.write("jejes gendut ? ")
benar = st.button("iya")
salah = st.button("tidak")
if benar:
    st.success(f"iya") 
    st.balloons()

if salah: 
    st.error(f"tidak")



