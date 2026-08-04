"""
=========================================================
Folder Service
=========================================================
Membuat dan mengelola folder mata kuliah.
=========================================================
"""

from pathlib import Path
import shutil


class FolderService:

    def __init__(self):

        self.root = Path("mata_kuliah")

        self.root.mkdir(exist_ok=True)

    # =====================================================
    # Buat Mata Kuliah
    # =====================================================

    def buat_mata_kuliah(
        self,
        nama: str
    ) -> Path:

        nama = nama.strip()

        if not nama:

            raise ValueError(
                "Nama mata kuliah tidak boleh kosong."
            )

        folder = self.root / nama

        if folder.exists():

            raise FileExistsError(
                "Mata kuliah sudah ada."
            )

        (folder / "modul").mkdir(
            parents=True,
            exist_ok=True
        )

        (folder / "artefak").mkdir(
            parents=True,
            exist_ok=True
        )

        return folder

    # =====================================================
    # Rename Mata Kuliah
    # =====================================================

    def rename_mata_kuliah(
        self,
        nama_lama: str,
        nama_baru: str
    ) -> Path:

        nama_lama = nama_lama.strip()
        nama_baru = nama_baru.strip()

        if not nama_baru:

            raise ValueError(
                "Nama mata kuliah tidak boleh kosong."
            )

        folder_lama = self.root / nama_lama

        if not folder_lama.exists():

            raise FileNotFoundError(
                "Mata kuliah tidak ditemukan."
            )

        folder_baru = self.root / nama_baru

        if folder_baru.exists():

            raise FileExistsError(
                "Nama mata kuliah sudah digunakan."
            )

        folder_lama.rename(folder_baru)

        return folder_baru

    # =====================================================
    # Hapus Mata Kuliah
    # =====================================================

    def hapus_mata_kuliah(
        self,
        nama: str
    ):

        folder = self.root / nama

        if not folder.exists():

            raise FileNotFoundError(
                "Mata kuliah tidak ditemukan."
            )

        shutil.rmtree(folder)