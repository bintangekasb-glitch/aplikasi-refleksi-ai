from services.upload_service import UploadService


def main():

    service = UploadService()

    print(service.ALLOWED_EXTENSIONS)


if __name__ == "__main__":
    main()