"""
=========================================================
File Service
=========================================================
Mengelola file mata kuliah.
=========================================================
"""

from pathlib import Path

from werkzeug.utils import secure_filename


class FileService:

    ALLOWED_KATEGORI = {
        "modul",
        "artefak"
    }

    def __init__(self):

        self.root = Path("mata_kuliah")

    # =====================================================
    # Folder
    # =====================================================

    def folder(
        self,
        nama_mk: str,
        kategori: str
    ) -> Path:

        if kategori not in self.ALLOWED_KATEGORI:

            raise ValueError(
                "Kategori tidak valid."
            )

        folder = (
            self.root /
            nama_mk /
            kategori
        )

        if not folder.exists():

            raise FileNotFoundError(
                "Folder tidak ditemukan."
            )

        return folder

    # =====================================================
    # Path File (Private)
    # =====================================================

    def _path_file(
        self,
        nama_mk: str,
        kategori: str,
        nama_file: str
    ) -> Path:

        folder = self.folder(
            nama_mk,
            kategori
        ).resolve()

        file = (
            folder /
            nama_file
        ).resolve()

        if folder not in file.parents:

            raise ValueError(
                "Nama file tidak valid."
            )

        return file

    # =====================================================
    # Daftar File
    # =====================================================

    def daftar(
        self,
        nama_mk: str,
        kategori: str
    ):

        folder = self.folder(
            nama_mk,
            kategori
        )

        hasil = []

        for file in sorted(folder.iterdir()):

            if file.is_file():

                hasil.append({

                    "nama": file.name,

                    "ukuran": file.stat().st_size,

                    "path": str(file)

                })

        return hasil

    # =====================================================
    # Hapus
    # =====================================================

    def hapus(
        self,
        nama_mk: str,
        kategori: str,
        nama_file: str
    ):

        file = self._path_file(
            nama_mk,
            kategori,
            nama_file
        )

        if not file.exists():

            raise FileNotFoundError(
                "File tidak ditemukan."
            )

        file.unlink()

    # =====================================================
    # Rename
    # =====================================================

    def rename(
        self,
        nama_mk: str,
        kategori: str,
        nama_lama: str,
        nama_baru: str
    ):

        nama_baru = secure_filename(
            nama_baru
        )

        folder = self.folder(
            nama_mk,
            kategori
        )

        lama = self._path_file(
            nama_mk,
            kategori,
            nama_lama
        )

        baru = (
            folder /
            nama_baru
        ).resolve()

        if folder.resolve() not in baru.parents:

            raise ValueError(
                "Nama file tidak valid."
            )

        if not lama.exists():

            raise FileNotFoundError(
                "File tidak ditemukan."
            )

        if baru.exists():

            raise FileExistsError(
                "Nama file sudah digunakan."
            )

        lama.rename(baru)