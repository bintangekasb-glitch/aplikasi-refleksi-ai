from pathlib import Path

from services.document_reader import DocumentReader
from services.token_estimator import TokenEstimator


def main():

    reader = DocumentReader()

    folder = Path("mata_kuliah")

    daftar = sorted(
        [
            item
            for item in folder.iterdir()
            if item.is_dir()
        ]
    )

    if not daftar:

        print("Belum ada mata kuliah.")
        return

    mk = reader.baca_mata_kuliah(
        daftar[0]
    )

    estimator = TokenEstimator()

    hasil = estimator.hitung(mk)

    print("=" * 60)
    print("TES TOKEN ESTIMATOR")
    print("=" * 60)

    print()

    print(f"Mata Kuliah      : {mk.nama}")
    print(f"Karakter         : {hasil.jumlah_karakter:,}")
    print(f"Estimasi Token   : {hasil.estimasi_token:,}")
    print(f"Estimasi Biaya   : ${hasil.estimasi_biaya:.6f}")
    print(f"Estimasi Waktu   : {hasil.estimasi_waktu} detik")
    print(f"Mode             : {hasil.mode}")


if __name__ == "__main__":
    main()