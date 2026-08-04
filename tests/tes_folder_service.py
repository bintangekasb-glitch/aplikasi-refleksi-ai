from services.folder_service import FolderService


def main():

    service = FolderService()

    folder = service.buat_mata_kuliah(
        "Contoh Mata Kuliah"
    )

    print("Berhasil membuat:")

    print(folder)


if __name__ == "__main__":
    main()