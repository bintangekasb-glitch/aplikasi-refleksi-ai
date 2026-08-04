from pathlib import Path
from config import HASIL_DIR, MATA_KULIAH_DIR


def folder_mata_kuliah(nama_mk):
    """
    Mengembalikan folder mata kuliah.
    """
    return MATA_KULIAH_DIR / nama_mk


def file_cache(nama_mk):
    """
    Mengembalikan lokasi file cache JSON.
    """
    return HASIL_DIR / f"{nama_mk}.json"


def pastikan_folder(path):
    """
    Membuat folder jika belum ada.
    """
    Path(path).mkdir(parents=True, exist_ok=True)