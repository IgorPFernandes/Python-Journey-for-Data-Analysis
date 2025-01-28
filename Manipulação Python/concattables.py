import os
import pandas as pd

# Caminho da pasta Downloads
caminho = r"C:\Users\igorp\Downloads"

# Nomes dos arquivos CSV
arquivos = {
    "users": os.path.join(caminho, "users_extended.csv"),
    "products": os.path.join(caminho, "products_extended.csv"),
    "orders": os.path.join(caminho, "orders_extended.csv"),
    "order_items": os.path.join(caminho, "order_items_extended.csv")
}

# Leitura dos CSVs em DataFrames
df_users = pd.read_csv(arquivos["users"])
df_products = pd.read_csv(arquivos["products"])
df_orders = pd.read_csv(arquivos["orders"])
df_order_items = pd.read_csv(arquivos["order_items"])

# Combinação geral (ordem: users -> products -> orders -> order_items)
df_combined = pd.concat([df_users, df_products, df_orders, df_order_items], ignore_index=True)

# Exportar o arquivo combinado
df_combined.to_csv("dados_combinados.csv", index=False)

print("Arquivo combinado gerado: dados_combinados.csv")
