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
            raise ValueError("Kategori tidak valid.")

        if file is None:
            raise ValueError("File belum dipilih.")

        if not file.filename:
            raise ValueError("File belum dipilih.")

        ekstensi = Path(file.filename).suffix.lower()

        if ekstensi not in self.ALLOWED_EXTENSIONS:
            raise ValueError(
                f"Format file {ekstensi} tidak didukung."
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

        # Hindari nama file sama
        if tujuan.exists():

            stem = tujuan.stem
            suffix = tujuan.suffix

            nomor = 1

            while True:

                kandidat = folder / f"{stem}_{nomor}{suffix}"

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
        files: list[FileStorage]
    ) -> list[Path]:

        hasil = []

        if not files:
            raise ValueError(
                "Tidak ada file yang dipilih."
            )

        for file in files:

            if file is None:
                continue

            if not file.filename:
                continue

            hasil.append(
                self.upload(
                    nama_mk=nama_mk,
                    kategori=kategori,
                    file=file
                )
            )

        if not hasil:
            raise ValueError(
                "Tidak ada file valid yang berhasil diupload."
            )

        return hasil