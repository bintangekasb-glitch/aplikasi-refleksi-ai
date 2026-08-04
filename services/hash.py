from pathlib import Path
import hashlib


def hitung_hash(file_path):
    """
    Menghasilkan hash SHA256 dari sebuah file.
    Digunakan untuk mendeteksi apakah isi file berubah.
    """

    file_path = Path(file_path)

    if not file_path.exists():
        return None

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while True:
            data = file.read(4096)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()