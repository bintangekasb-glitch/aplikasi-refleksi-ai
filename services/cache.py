import json
from pathlib import Path


def baca_cache(file_cache):
    """
    Membaca file cache JSON.
    Jika belum ada, kembalikan dictionary kosong.
    """

    file_cache = Path(file_cache)

    if not file_cache.exists():
        return {}

    try:
        with open(file_cache, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception:
        return {}


def simpan_cache(file_cache, data):
    """
    Menyimpan hasil analisis AI ke file JSON.
    """

    file_cache = Path(file_cache)

    file_cache.parent.mkdir(parents=True, exist_ok=True)

    with open(file_cache, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def cache_valid(hash_modul, hash_artefak, data_cache):
    """
    Mengecek apakah hash dokumen sama
    dengan hash yang ada di cache.
    """

    return (
        data_cache.get("hash_modul") == hash_modul
        and
        data_cache.get("hash_artefak") == hash_artefak
    )