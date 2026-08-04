from dotenv import load_dotenv
from openai import OpenAI
import os

# Membaca file .env
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

print("=" * 50)
print("TES PEMBACAAN .ENV")
print("=" * 50)

if api_key:
    print("API Key ditemukan.")
    print("Awalan key:", api_key[:10] + "...")
else:
    print("API Key TIDAK ditemukan.")

try:
    client = OpenAI(api_key=api_key)

    models = client.models.list()

    print("\nKoneksi ke OpenAI berhasil!")
    print("Jumlah model:", len(models.data))

except Exception as e:
    print("\nTerjadi error:")
    print(e)