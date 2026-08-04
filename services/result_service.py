"""
=========================================================
Result Service
=========================================================
Menyimpan dan membaca hasil analisis AI.
=========================================================
"""

import json
from pathlib import Path
from dataclasses import asdict

from services.models import HasilAnalisis
from services.config import HASIL_DIR


class ResultService:
    """
    Service untuk menyimpan dan membaca hasil analisis.
    """

    def __init__(self):

        self.folder = Path(HASIL_DIR)

        self.folder.mkdir(
            exist_ok=True
        )

    # =====================================================
    # NAMA FILE
    # =====================================================

    def _file_hasil(
        self,
        mata_kuliah: str
    ) -> Path:

        nama = mata_kuliah.lower()

        nama = nama.replace(" ", "_")

        return self.folder / f"{nama}.json"

    # =====================================================
    # SIMPAN
    # =====================================================

    def simpan(
        self,
        hasil: HasilAnalisis
    ) -> None:

        file = self._file_hasil(
            hasil.mata_kuliah
        )

        with open(
            file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(

                asdict(hasil),

                f,

                ensure_ascii=False,

                indent=4

            )

    # =====================================================
    # BACA
    # =====================================================

    def baca(
        self,
        mata_kuliah: str
    ) -> dict | None:

        file = self._file_hasil(
            mata_kuliah
        )

        if not file.exists():

            return None

        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    # =====================================================
    # CEK
    # =====================================================

    def sudah_ada(
        self,
        mata_kuliah: str
    ) -> bool:

        return self._file_hasil(
            mata_kuliah
        ).exists()