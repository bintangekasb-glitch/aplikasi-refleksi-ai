"""
=========================================================
Validator Service
=========================================================
Memvalidasi struktur folder mata kuliah.
=========================================================
"""

from pathlib import Path

from services.models import ValidasiMataKuliah


class Validator:

    FILE_DIABAIKAN = (
        "desktop.ini",
    )

    PREFIX_DIABAIKAN = (
        "~$",
    )

    # =====================================================
    # VALIDASI SATU MATA KULIAH
    # =====================================================

    def validasi(
        self,
        folder_mk: Path
    ) -> ValidasiMataKuliah:

        peringatan = []

        valid = True

        jumlah_modul = 0

        jumlah_artefak = 0

        # -----------------------------------------
        # Folder Modul
        # -----------------------------------------

        folder_modul = folder_mk / "modul"

        if not folder_modul.exists():

            valid = False

            peringatan.append(
                "Folder modul tidak ditemukan."
            )

        else:

            jumlah_modul = self.hitung_file(
                folder_modul
            )

            if jumlah_modul == 0:

                valid = False

                peringatan.append(
                    "Folder modul kosong."
                )

        # -----------------------------------------
        # Folder Artefak
        # -----------------------------------------

        folder_artefak = folder_mk / "artefak"

        if not folder_artefak.exists():

            valid = False

            peringatan.append(
                "Folder artefak tidak ditemukan."
            )

        else:

            jumlah_artefak = self.hitung_file(
                folder_artefak
            )

            if jumlah_artefak == 0:

                valid = False

                peringatan.append(
                    "Folder artefak kosong."
                )

        return ValidasiMataKuliah(

            nama=folder_mk.name,

            valid=valid,

            jumlah_modul=jumlah_modul,

            jumlah_artefak=jumlah_artefak,

            peringatan=peringatan

        )

    # =====================================================
    # HITUNG FILE VALID
    # =====================================================

    def hitung_file(
        self,
        folder: Path
    ) -> int:

        jumlah = 0

        for file in folder.iterdir():

            if not file.is_file():
                continue

            if file.name.lower() in self.FILE_DIABAIKAN:
                continue

            if file.name.startswith(
                self.PREFIX_DIABAIKAN
            ):
                continue

            jumlah += 1

        return jumlah