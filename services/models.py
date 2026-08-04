"""
=========================================================
Models
=========================================================
Model data yang digunakan oleh seluruh aplikasi.
=========================================================
"""

from dataclasses import dataclass, field


# =========================================================
# DOKUMEN
# =========================================================

@dataclass
class Dokumen:

    nama: str

    path: str

    kategori: str

    format: str

    ukuran: int

    isi: str


# =========================================================
# MATA KULIAH
# =========================================================

@dataclass
class MataKuliah:

    nama: str

    modul: list[Dokumen] = field(default_factory=list)

    artefak: list[Dokumen] = field(default_factory=list)

    jumlah_file: int = 0

    jumlah_karakter: int = 0


# =========================================================
# HASIL VALIDASI
# =========================================================

@dataclass
class ValidasiMataKuliah:

    nama: str

    valid: bool

    jumlah_modul: int

    jumlah_artefak: int

    peringatan: list[str] = field(default_factory=list)


# =========================================================
# ESTIMASI TOKEN
# =========================================================

@dataclass
class EstimasiToken:

    jumlah_karakter: int

    estimasi_token: int

    estimasi_biaya: float

    estimasi_waktu: int

    mode: str


# =========================================================
# PROMPT AI
# =========================================================

@dataclass
class PromptAI:

    isi: str

    jumlah_karakter: int

    estimasi_token: int


# =========================================================
# HASIL ANALISIS AI
# =========================================================

@dataclass
class HasilAnalisis:

    mata_kuliah: str

    model: str

    prompt_token: int

    completion_token: int

    total_token: int

    estimasi_biaya: float

    waktu_proses: float

    isi: str