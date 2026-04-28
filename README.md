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



## 1. Persiapan

Pastikan Python sudah terinstall di komputer.

Install library yang dibutuhkan:

```bash
pip install streamlit pandas
```

## 2. Siapkan Data

* Letakkan file riwayat transaksi dalam format `.csv` ke dalam folder proyek.
* Cara mendapatkan file:

  * Buka Etherscan / Basescan / Arbiscan  / Optimistic
  * Scroll ke bawah
  * Klik **Export CSV** pada riwayat transaksi wallet

## 3. Jalankan Aplikasi

Buka terminal / CMD di folder proyek, lalu jalankan:

```bash
python -m streamlit run app.py
```
