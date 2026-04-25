# Analisa Wallet Sederhana 🚀

Proyek berbasis Python untuk melakukan audit dan analisa data keuangan pribadi dari file CSV (khususnya riwayat transaksi Ethereum L1 & L2).

## 📊 Fitur Utama
1. **Total Transaksi**: Rekapitulasi jumlah seluruh aktivitas wallet.
2. **Arus Kas ETH**: Pemisahan detail total ETH Masuk dan ETH Keluar.
3. **Analisa Waktu**: Menemukan jam paling aktif saat melakukan transaksi.
4. **Whale Tracker**: Melihat 5 transaksi terbesar yang pernah dilakukan.
5. **Top Interaction**: List 10 wallet yang paling sering berinteraksi dengan kamu.
6. **Ongoing Dev**: Fitur-fitur baru akan terus ditambahkan secara bertahap.

## 🛠️ Cara Penggunaan

### 1. Persiapan
Pastikan kamu sudah menginstall Python di komputer. Kemudian, install library yang dibutuhkan:
```bash
pip install streamlit pandas

2. Siapkan Data
Letakkan file riwayat transaksi kamu dalam format .csv ke dalam folder proyek.
(Tips: Buka Etherscan/Basescan/Bscscan, lalu scroll ke bawah dan klik Export CSV pada riwayat transaksi walletmu).

3. Jalankan Aplikasi
Buka terminal/CMD di folder proyek, lalu jalankan perintah:
python -m streamlit run app.py