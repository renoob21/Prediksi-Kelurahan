import joblib
import pandas as pd
import streamlit as st
import string

def clear_text(alamat):
    nopunc = []
    for char in alamat:
        if char not in string.punctuation:
            nopunc.append(char)
        else:
            nopunc.append(' ')
            continue
    nopunc = ''.join(nopunc)
    return nopunc.split()


model = joblib.load('C:\\Users\\renoi\\Data Science Project\\NLP Project\\kelurahan_model.sav')

st.title('Aplikasi Prediksi Kelurahan v0.1.0')

alamat = st.text_input('Masukkan alamat wajib pajak . . .')

pred = model.predict([alamat])[0]

if st.button('Cari Kelurahan'):
    st.write(pred)

st.header('Mode Upload')

data = st.file_uploader('Upload csv dengan pembatas titik koma (;), dengan kolom **Alamat** dan **Kelurahan**')

if data is not None:
    df = pd.read_csv(data,sep=';')
    address = df['Alamat'].values
    preds = model.predict(address)
    df = pd.DataFrame({'Alamat':address,'Kelurahan':preds})
    st.dataframe(df)
    csv = df.to_csv()
    st.download_button('Download CSV',
                       data=csv,
                       file_name='Kelurahan WP.csv')