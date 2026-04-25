

    
### KODE BERSIH FUNGSI 
import requests
import pandas as pd


def analisa_wallet(path_file):
    df=pd.read_csv(path_file)
    df_bersihkan = df.dropna(axis=1, how='all')

    # format tampilan
    pd.options.display.float_format = '{:.9f}'.format

    # 1. total transaksi
    total_transaksi = len(df_bersihkan)

    # 2. Value IN
    value_in_kosong = (df_bersihkan['Value_IN(ETH)'] == 0).sum()
    value_in_isi = (df_bersihkan['Value_IN(ETH)'] > 0).sum()
    persen_kosong = (value_in_kosong / total_transaksi) * 100

    # 3. total masuk & keluar
    total_masuk = df_bersihkan['Value_IN(ETH)'].sum()
    total_keluar = df_bersihkan['Value_OUT(ETH)'].sum()

    # 4. jam transaksi
    df_bersihkan['DateTime (UTC)'] = pd.to_datetime(df_bersihkan['DateTime (UTC)'])
    df_bersihkan['jam'] = df_bersihkan['DateTime (UTC)'].dt.hour
    jam_terbanyak = df_bersihkan['jam'].value_counts().idxmax()

    # 5. method terbanyak
    method_terbanyak = df_bersihkan['Method'].value_counts().idxmax()
    jumlah_method = df_bersihkan['Method'].value_counts().max()
    persen_method = (jumlah_method / total_transaksi) * 100

    # 6. fee rata-rata saat tidak ada Value_IN
    fee_rata = df_bersihkan[df_bersihkan['Value_IN(ETH)'] == 0]['TxnFee(ETH)'].mean()

    # 7. ambil transaksi terbesar
    top_transaksi = df_bersihkan.nlargest(5, 'Value_OUT(ETH)')[
        ['Value_IN(ETH)','Value_OUT(ETH)','TxnFee(ETH)','Method','DateTime (UTC)']
    ]

    #8. transaksi paling banyak
    wallet_tersering = df_bersihkan['To'].value_counts().head(10)


    # 🎯 OUTPUT RINGKAS
    hasil = {
        "total_transaksi": total_transaksi,
        "persen_value_in_kosong": round(persen_kosong, 2),
        "total_masuk_eth": total_masuk,
        "total_keluar_eth": total_keluar,
        "jam_terpadat": int(jam_terbanyak),
        "method_terbanyak": method_terbanyak,
        "persen_method_terbanyak": round(persen_method, 2),
        "rata_fee_tanpa_value_in": fee_rata,
        "top_transaksi": top_transaksi,
        "wallet_tersering":str(wallet_tersering)
    }

    return hasil



