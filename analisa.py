import pandas as pd

def analisa_wallet(data):
    # 1. fleksibel: bisa file path ATAU dataframe
    if isinstance(data, str):
        df = pd.read_csv(data)
    else:
        df = data.copy()

    df_bersihkan = df.dropna(axis=1, how='all')

    pd.options.display.float_format = '{:.9f}'.format

    total_transaksi = len(df_bersihkan)

    value_in_kosong = (df_bersihkan['Value_IN(ETH)'] == 0).sum()
    persen_kosong = (value_in_kosong / total_transaksi) * 100

    total_masuk = df_bersihkan['Value_IN(ETH)'].sum()
    total_keluar = df_bersihkan['Value_OUT(ETH)'].sum()

    df_bersihkan['DateTime (UTC)'] = pd.to_datetime(df_bersihkan['DateTime (UTC)'])
    df_bersihkan['jam'] = df_bersihkan['DateTime (UTC)'].dt.hour
    jam_terbanyak = df_bersihkan['jam'].value_counts().idxmax()

    method_terbanyak = df_bersihkan['Method'].value_counts().idxmax()
    jumlah_method = df_bersihkan['Method'].value_counts().max()
    persen_method = (jumlah_method / total_transaksi) * 100

    fee_rata = df_bersihkan[df_bersihkan['Value_IN(ETH)'] == 0]['TxnFee(ETH)'].mean()

    top_transaksi = df_bersihkan.nlargest(5, 'Value_OUT(ETH)')[
        ['Value_IN(ETH)','Value_OUT(ETH)','TxnFee(ETH)','Method','DateTime (UTC)']
    ]

    wallet_tersering = df_bersihkan['To'].value_counts().head(10)
    

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
        "wallet_tersering": wallet_tersering
    }

    return hasil