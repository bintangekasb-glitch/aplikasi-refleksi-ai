from services.file_service import FileService


def main():

    service = FileService()

    print("=" * 60)

    print("TES FILE SERVICE")

    print("=" * 60)

    print()

    hasil = service.daftar(
        "filosofi",
        "modul"
    )

    for file in hasil:

        print(file["nama"])

    print()

    print("Jumlah :", len(hasil))


if __name__ == "__main__":

    main()