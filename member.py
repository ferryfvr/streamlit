import pandas as pd
import random
from faker import Faker

# Initialize Faker
fake = Faker('id_ID')

# Function to generate random data for members with some shopping multiple times
def generate_member_data_with_multiple_transactions(member_code_prefix, n_members, min_transactions, max_transactions):
    data = []
    for _ in range(n_members):
        name = fake.name()
        member_code = f"{member_code_prefix}{random.randint(1000, 9999)}"
        num_transactions = random.randint(min_transactions, max_transactions)
        for _ in range(num_transactions):
            transaction_date = fake.date_this_year()
            total_spending = random.randint(10, 1000) * 1000  # Rounded spending in IDR
            data.append([member_code, name, transaction_date, total_spending])
    return data

# Generate data for 100 members with some having multiple transactions
member_data_multiple = generate_member_data_with_multiple_transactions("BR", 100, 1, 3)
df_multiple = pd.DataFrame(member_data_multiple, columns=["Kode Member", "Nama", "Tanggal Belanja", "Total Belanja (IDR)"])

# Calculate points for each transaction
df_multiple["Poin"] = df_multiple["Total Belanja (IDR)"] // 10000

# Save to CSV
csv_path_multiple = "/Users/ferryfvr/Documents/DATA_RAYA_BISDIG_FERRY/member_multiple_transactions_with_points.csv"
df_multiple.to_csv(csv_path_multiple, index=False)

print(f"File CSV telah dibuat di lokasi: {csv_path_multiple}")