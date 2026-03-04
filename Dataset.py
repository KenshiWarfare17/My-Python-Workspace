import pandas as pd

# ================= DATA PROFIT TIKET =================
DATA_PROFIT_TIKET = [
    {"tickets_sold": 100, "profit": 10},
    {"tickets_sold": 200, "profit": 20},
    {"tickets_sold": 300, "profit": 27},
    {"tickets_sold": 400, "profit": 38},
    {"tickets_sold": 500, "profit": 48},
    {"tickets_sold": 600, "profit": 58},
    {"tickets_sold": 700, "profit": 67},
]

df = pd.DataFrame(DATA_PROFIT_TIKET)

print("=== DATA PROFIT TIKET ===")
print(df)
