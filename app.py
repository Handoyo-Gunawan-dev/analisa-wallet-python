import streamlit as st
import pandas as pd
from analisa import analisa_wallet # Mengambil fungsi yang sudah kamu buat

# 1. Judul Aplikasi
st.title("Simple Wallet Analysis Tool.")
st.caption("(Alat analisa wallet sederhana)")
st.write("Upload the CSV file of your wallet export results to see the summary.")
st.caption("(Upload file CSV hasil export wallet kamu untuk melihat ringkasannya)")

# 2. Komponen Upload File
file_terpilih = st.file_uploader("Select CSV file", type=["csv"])

if file_terpilih is not None:
    # Simpan file sementara agar bisa dibaca oleh fungsi analisa_wallet
    df = pd.read_csv(file_terpilih)
    hasil = analisa_wallet(df)

    # 4. Tampilkan Hasil ke Layar Streamlit
    st.divider() # Garis pemisah
    st.header("Analysis Results")

    # Menampilkan angka-angka penting dalam kolom agar rapi
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Transaction", hasil['total_transaksi'])
    col2.metric("Total In (ETH)", f"{hasil['total_masuk_eth']:.4f}")
    col3.metric("Total Out (ETH)", f"{hasil['total_keluar_eth']:.4f}")

    st.subheader("Transaction Insights")
    import datetime
    jam_obj=datetime.time(hour=int(hasil["jam_terpadat"]))
    jam_en=jam_obj.strftime("%I:%M %p")
    st.write(F"**Busiest hours:** {jam_en}")
    st.write(f"**Most Methods:** {hasil['method_terbanyak']} ({hasil['persen_method_terbanyak']}%)")
    st.write(f"**Percentage of Value IN Empty :** {hasil['persen_value_in_kosong']}%")
    st.write(f"**Average Fee (when Value IN is 0):** {hasil['rata_fee_tanpa_value_in']:.9f} ETH")

    # 5. Menampilkan Data Tabel
    st.subheader("5 Largest Outgoing Transactions")
    st.table(hasil["top_transaksi"])

    st.subheader("10 Most Frequently Interacted Wallets")
    st.table(hasil["wallet_tersering"])