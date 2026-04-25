import streamlit as st
import pandas as pd
from analisa import analisa_wallet # Mengambil fungsi yang sudah kamu buat

# 1. Judul Aplikasi
st.title("Alat Analisa Wallet Sederhana")
st.write("Upload file CSV hasil export wallet kamu untuk melihat ringkasannya.")

# 2. Komponen Upload File
file_terpilih = st.file_uploader("Pilih file CSV", type=["csv"])

if file_terpilih is not None:
    # Simpan file sementara agar bisa dibaca oleh fungsi analisa_wallet
    with open("temp_wallet.csv", "wb") as f:
        f.write(file_terpilih.getbuffer())

    # 3. Jalankan Fungsi Analisa
    # Kita panggil fungsi buatanmu tanpa mengubah isinya
    hasil = analisa_wallet("temp_wallet.csv")

    # 4. Tampilkan Hasil ke Layar Streamlit
    st.divider() # Garis pemisah
    st.header("Hasil Analisis")

    # Menampilkan angka-angka penting dalam kolom agar rapi
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Transaksi", hasil["total_transaksi"])
    col2.metric("Total Masuk (ETH)", f"{hasil['total_masuk_eth']:.4f}")
    col3.metric("Total Keluar (ETH)", f"{hasil['total_keluar_eth']:.4f}")

    st.subheader("Wawasan Transaksi")
    st.write(f"**Jam Terpadat:** Jam {hasil['jam_terpadat']}:00")
    st.write(f"**Method Terbanyak:** {hasil['method_terbanyak']} ({hasil['persen_method_terbanyak']}%)")
    st.write(f"**Persentase Value IN Kosong:** {hasil['persen_value_in_kosong']}%")
    st.write(f"**Rata-rata Fee (saat Value IN 0):** {hasil['rata_fee_tanpa_value_in']:.9f} ETH")

    # 5. Menampilkan Data Tabel
    st.subheader("5 Transaksi Keluar Terbesar")
    st.table(hasil["top_transaksi"])

    st.subheader("10 Wallet yang Paling Sering Berinteraksi")
    st.text(hasil["wallet_tersering"])