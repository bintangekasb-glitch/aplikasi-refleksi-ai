"""
=========================================================
Preview Service
=========================================================
Mengelola preview file.
=========================================================
"""

from pathlib import Path


class PreviewService:

    ROOT = Path("mata_kuliah")

    def file(
        self,
        nama_mk: str,
        kategori: str,
        nama_file: str
    ) -> Path:

        file = (
            self.ROOT
            / nama_mk
            / kategori
            / nama_file
        )

        if not file.exists():

            raise FileNotFoundError(
                "File tidak ditemukan."
            )

        return file

    def bisa_preview(
        self,
        file: Path
    ) -> bool:

        return file.suffix.lower() == ".pdf"