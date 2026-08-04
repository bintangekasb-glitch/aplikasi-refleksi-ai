"""
=========================================================
Prompt Builder Service
=========================================================
Menyusun prompt AI berdasarkan template dan dokumen.
=========================================================
"""

from pathlib import Path

from services.config import KARAKTER_PER_TOKEN
from services.models import (
    MataKuliah,
    PromptAI,
)


class PromptBuilder:

    def __init__(self):

        self.prompt_path = (
            Path(__file__).resolve().parent.parent
            / "prompts"
            / "prompt_refleksi.txt"
        )

    # =====================================================
    # MEMBACA TEMPLATE PROMPT
    # =====================================================

    def baca_template(self) -> str:

        with open(
            self.prompt_path,
            "r",
            encoding="utf-8"
        ) as file:

            return file.read()

    # =====================================================
    # MEMBANGUN PROMPT
    # =====================================================

    def buat_prompt(
        self,
        mata_kuliah: MataKuliah
    ) -> PromptAI:

        bagian = []

        # Template Prompt
        bagian.append(
            self.baca_template()
        )

        # Data Mata Kuliah
        bagian.append("")
        bagian.append("=" * 60)
        bagian.append("DATA MATA KULIAH")
        bagian.append("=" * 60)

        bagian.append(
            f"Nama Mata Kuliah : {mata_kuliah.nama}"
        )

        # Modul
        bagian.append("")
        bagian.append("=" * 60)
        bagian.append("MODUL")
        bagian.append("=" * 60)

        for dokumen in mata_kuliah.modul:

            bagian.append("")
            bagian.append(
                f"Nama File : {dokumen.nama}"
            )

            bagian.append(
                f"Format    : {dokumen.format}"
            )

            bagian.append("")
            bagian.append(
                dokumen.isi
            )

        # Artefak
        bagian.append("")
        bagian.append("=" * 60)
        bagian.append("ARTEFAK")
        bagian.append("=" * 60)

        for dokumen in mata_kuliah.artefak:

            bagian.append("")
            bagian.append(
                f"Nama File : {dokumen.nama}"
            )

            bagian.append(
                f"Format    : {dokumen.format}"
            )

            bagian.append("")
            bagian.append(
                dokumen.isi
            )

        isi_prompt = "\n".join(
            bagian
        )

        jumlah_karakter = len(
            isi_prompt
        )

        estimasi_token = max(
            1,
            jumlah_karakter // KARAKTER_PER_TOKEN
        )

        return PromptAI(

            isi=isi_prompt,

            jumlah_karakter=jumlah_karakter,

            estimasi_token=estimasi_token

        )