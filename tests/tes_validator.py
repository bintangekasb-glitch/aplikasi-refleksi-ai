from pathlib import Path

from services.validator import Validator


def main():

    validator = Validator()

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

    hasil = validator.validasi(
        daftar[0]
    )

    print("=" * 60)
    print("TES VALIDATOR")
    print("=" * 60)

    print()

    print(f"Mata Kuliah : {hasil.nama}")

    print(f"Valid       : {hasil.valid}")

    print(f"Modul       : {hasil.jumlah_modul}")

    print(f"Artefak     : {hasil.jumlah_artefak}")

    print()

    if hasil.peringatan:

        print("PERINGATAN")

        for pesan in hasil.peringatan:

            print("-", pesan)

    else:

        print("Tidak ada peringatan.")


if __name__ == "__main__":
    main()