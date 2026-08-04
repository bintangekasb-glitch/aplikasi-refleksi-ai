"""
=========================================================
Tes Analysis Service
=========================================================
"""

from pathlib import Path

from services.analysis_service import AnalysisService


def main():

    print("=" * 60)
    print("TES ANALYSIS SERVICE")
    print("=" * 60)

    folder = Path("mata_kuliah")

    daftar = sorted(

        item

        for item in folder.iterdir()

        if item.is_dir()

    )

    if not daftar:

        print()

        print("Belum ada mata kuliah.")

        return

    service = AnalysisService()

    hasil = service.analisis(

        daftar[0]

    )

    print()

    print("=" * 60)
    print("HASIL")
    print("=" * 60)

    print()

    print("Mata Kuliah :", hasil.mata_kuliah)

    print("Model       :", hasil.model)

    print("Waktu       :", f"{hasil.waktu_proses:.2f} detik")

    print()

    print("=" * 60)
    print("PREVIEW HASIL")
    print("=" * 60)

    print()

    print(

        hasil.isi[:1500]

    )


if __name__ == "__main__":
    main()