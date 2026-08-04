"""
=========================================================
Document Manager
=========================================================
Mengelola data mata kuliah
=========================================================
"""

from config import MATA_KULIAH_DIR


def daftar_file(folder):

    if not folder.exists():
        return []

    return sorted([
        file.name
        for file in folder.iterdir()
        if file.is_file()
    ])


def daftar_mata_kuliah():

    if not MATA_KULIAH_DIR.exists():
        return []

    daftar = []

    for folder in sorted(MATA_KULIAH_DIR.iterdir()):

        if not folder.is_dir():
            continue

        modul = daftar_file(folder / "modul")
        artefak = daftar_file(folder / "artefak")

        daftar.append({

            "nama": folder.name,

            "jumlah_modul": len(modul),

            "jumlah_artefak": len(artefak),

            "status": "Belum Dianalisis",

            "modul": modul,

            "artefak": artefak

        })

    return daftar


def statistik_dashboard():

    daftar = daftar_mata_kuliah()

    return {

        "jumlah_mata_kuliah": len(daftar),

        "jumlah_modul": sum(
            mk["jumlah_modul"]
            for mk in daftar
        ),

        "jumlah_artefak": sum(
            mk["jumlah_artefak"]
            for mk in daftar
        ),

        "mode_ai": "Hemat"

    }


def detail_mata_kuliah(nama):

    for mk in daftar_mata_kuliah():

        if mk["nama"] == nama:
            return mk

    return None