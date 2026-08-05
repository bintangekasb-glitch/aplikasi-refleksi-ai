"""
=========================================================
Upload Service
=========================================================
Mengelola upload file modul dan artefak.
=========================================================
"""

from pathlib import Path

from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename


class UploadService:

    ALLOWED_EXTENSIONS = {
        ".pdf",
        ".docx",
        ".pptx",
        ".xlsx"
    }

    ALLOWED_KATEGORI = {
        "modul",
        "artefak"
    }

    def __init__(self):

        self.root = Path("mata_kuliah")

    # =====================================================
    # Upload satu file
    # =====================================================

    def upload(
        self,
        nama_mk: str,
        kategori: str,
        file: FileStorage
    ) -> Path:

        if kategori not in self.ALLOWED_KATEGORI:

            raise ValueError(
                "Kategori tidak valid."
            )

        if file is None:

            raise ValueError(
                "File belum dipilih."
            )

        if not file.filename:

            raise ValueError(
                "File belum dipilih."
            )

        ekstensi = Path(
            file.filename
        ).suffix.lower()

        if ekstensi not in self.ALLOWED_EXTENSIONS:

            raise ValueError(
                "Format file tidak didukung."
            )

        folder = (
            self.root /
            nama_mk /
            kategori
        )

        folder.mkdir(
            parents=True,
            exist_ok=True
        )

        nama_file = secure_filename(
            file.filename
        )

        tujuan = folder / nama_file

        # ============================================
        # Hindari file tertimpa
        # ============================================

        if tujuan.exists():

            stem = tujuan.stem
            suffix = tujuan.suffix

            nomor = 1

            while True:

                kandidat = (
                    folder /
                    f"{stem}_{nomor}{suffix}"
                )

                if not kandidat.exists():

                    tujuan = kandidat

                    break

                nomor += 1

        file.save(tujuan)

        return tujuan

    # =====================================================
    # Upload banyak file
    # =====================================================

    def upload_banyak(
        self,
        nama_mk: str,
        kategori: str,
        files
    ):

        hasil = []

        if files is None:

            return hasil

        for file in files:

            if file is None:

                continue

            if not file.filename:

                continue

            path = self.upload(
                nama_mk,
                kategori,
                file
            )

            hasil.append(path)

        return hasil