import pandas as pd
import sqlite3
import plotly.express as px

# ============================================================
# 1. Buat Data Penjualan Tiket
# ============================================================
data = {
    'event': ['XXI', 'Flix', 'CGV', 'LBT Bioskop'],
    'ticket_price': [30000, 60000, 40000, 0],
    'tickets_sold': [500, 200, 345, 0],
}

df = pd.DataFrame(data)

# Hitung total revenue dan profit
df['revenue'] = df['ticket_price'] * df['tickets_sold']
df['profit'] = df['revenue'] * 0.10  # misalnya profit 10% dari revenue

print("=== Data Penjualan Tiket ===")
print(df)

# ============================================================
# 2. Simpan ke Database (SQLite)
# ============================================================
conn = sqlite3.connect('ticket_sales.db')
df.to_sql('sales_data', conn, if_exists='replace', index=False)
print("\n✅ Data berhasil disimpan ke database 'ticket_sales.db' (table: sales_data)")

# ============================================================
# 3. Baca ulang dari Database
# ============================================================
df_db = pd.read_sql_query("SELECT * FROM sales_data", conn)
print("\n📦 Data dari database:")
print(df_db)

# ============================================================
# 4. Analisis Dasar
# ============================================================
total_profit = df_db['profit'].sum()
best_event = df_db.loc[df_db['profit'].idxmax(), 'event']
average_price = df_db['ticket_price'].mean()

print(f"\n💰 Total Profit: Rp {total_profit:,.0f}")
print(f"🏆 Event dengan Profit Tertinggi: {best_event}")
print(f"🎟️ Harga Tiket Rata-rata: Rp {average_price:,.0f}")

# ============================================================
# 5. Visualisasi dengan Plotly
# ============================================================
fig = px.bar(
    df_db,
    x='event',
    y='profit',
    color='event',
    text='profit',
    title='Profit per Event (Interactive)',
    labels={'profit': 'Profit (Rp)', 'event': 'Event'},
    color_discrete_sequence=px.colors.sequential.Viridis,
    hover_data={
        'revenue': ':.0f',
        'ticket_price': ':.0f',
        'tickets_sold': ':.0f'
    }
)

fig.update_traces(
    texttemplate='Rp %{text:,.0f}',
    textposition='outside',
    hovertemplate=
    "<b>%{x}</b><br>" +
    "Profit: Rp %{y:,.0f}<br>" +
    "Revenue: Rp %{customdata[0]:,.0f}<br>" +
    "Harga Tiket: Rp %{customdata[1]:,.0f}<br>" +
    "Tiket Terjual: %{customdata[2]:,.0f}"
)

fig.update_layout(
    yaxis_title='Profit (Rp)',
    xaxis_title='Event',
    title_x=0.5,
    title_font_size=20,
    plot_bgcolor='white',
    yaxis=dict(showgrid=True, gridcolor='lightgrey')
)

fig.show()

# ============================================================
# 6. Tutup koneksi
# ============================================================
conn.close()
