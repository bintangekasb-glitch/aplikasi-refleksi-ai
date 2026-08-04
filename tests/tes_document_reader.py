from pathlib import Path

from services.document_reader import DocumentReader


def main():

    print("=" * 60)
    print("TES DOCUMENT READER")
    print("=" * 60)

    reader = DocumentReader()

    folder = Path("mata_kuliah")

    daftar_mk = sorted(
        [
            item
            for item in folder.iterdir()
            if item.is_dir()
        ]
    )

    if not daftar_mk:

        print()
        print("Belum ada mata kuliah.")
        return

    mata_kuliah = reader.baca_mata_kuliah(
        daftar_mk[0]
    )

    print()

    print(f"Nama Mata Kuliah : {mata_kuliah.nama}")

    print(f"Jumlah File      : {mata_kuliah.jumlah_file}")

    print(
        f"Jumlah Karakter  : {mata_kuliah.jumlah_karakter:,}"
    )

    print()

    print("=" * 60)
    print("MODUL")
    print("=" * 60)

    for dokumen in mata_kuliah.modul:

        print(
            f"- {dokumen.nama} ({dokumen.format})"
        )

    print()

    print("=" * 60)
    print("ARTEFAK")
    print("=" * 60)

    for dokumen in mata_kuliah.artefak:

        print(
            f"- {dokumen.nama} ({dokumen.format})"
        )

    print()

    print("=" * 60)
    print("RINGKASAN")
    print("=" * 60)

    ringkasan = reader.ringkasan()

    print(
        f"File Dibaca      : {ringkasan['file_dibaca']}"
    )

    print(
        f"File Gagal       : {ringkasan['file_gagal']}"
    )

    print(
        f"Total Karakter   : {ringkasan['total_karakter']:,}"
    )


if __name__ == "__main__":
    main()