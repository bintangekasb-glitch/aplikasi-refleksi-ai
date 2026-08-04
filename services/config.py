"""
=========================================================
Configuration
=========================================================
Seluruh konfigurasi aplikasi.
=========================================================
"""

import os

from dotenv import load_dotenv


# =========================================================
# MEMBACA FILE .ENV
# =========================================================

load_dotenv()


# =========================================================
# GOOGLE GEMINI
# =========================================================

GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY"
)

AI_MODEL = "models/gemini-3.5-flash"

AI_MAX_OUTPUT_TOKENS = 4096


# =========================================================
# ESTIMASI TOKEN
# =========================================================

KARAKTER_PER_TOKEN = 4


# =========================================================
# BATAS DOKUMEN
# =========================================================

MAKSIMAL_UKURAN_FILE_MB = 25

MAKSIMAL_JUMLAH_FILE = 100


# =========================================================
# FOLDER
# =========================================================

ROOT_DIR = os.path.dirname(
    os.path.dirname(
        __file__
    )
)

PROMPT_DIR = os.path.join(
    ROOT_DIR,
    "prompts"
)

HASIL_DIR = os.path.join(
    ROOT_DIR,
    "hasil"
)