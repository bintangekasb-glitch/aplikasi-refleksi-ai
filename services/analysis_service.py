"""
=========================================================
Analysis Service
=========================================================
Mengatur seluruh proses analisis mata kuliah.
=========================================================
"""

from pathlib import Path

from services.document_reader import DocumentReader
from services.prompt_builder import PromptBuilder
from services.ai_service import AIService
from services.result_service import ResultService
from services.logger_service import LoggerService

from services.models import HasilAnalisis


class AnalysisService:
    """
    Service utama untuk melakukan analisis satu mata kuliah.
    """

    def __init__(self):

        self.reader = DocumentReader()

        self.builder = PromptBuilder()

        self.ai = AIService()

        self.result = ResultService()

        self.logger = LoggerService()

    # =====================================================
    # ANALISIS SATU MATA KULIAH
    # =====================================================

    def analisis(
        self,
        folder_mata_kuliah: Path
    ) -> HasilAnalisis:

        self.logger.info(
            f"Memulai analisis: {folder_mata_kuliah.name}"
        )

        try:

            # ---------------------------------------------
            # Membaca dokumen
            # ---------------------------------------------
            self.logger.info(
                "Membaca dokumen..."
            )

            mata_kuliah = self.reader.baca_mata_kuliah(
                folder_mata_kuliah
            )

            self.logger.info(
                f"Dokumen berhasil dibaca ({mata_kuliah.jumlah_file} file)"
            )

            # ---------------------------------------------
            # Membuat prompt
            # ---------------------------------------------
            self.logger.info(
                "Menyusun prompt..."
            )

            prompt = self.builder.buat_prompt(
                mata_kuliah
            )

            self.logger.info(
                f"Prompt selesai ({prompt.estimasi_token:,} token)"
            )

            # ---------------------------------------------
            # Analisis AI
            # ---------------------------------------------
            self.logger.info(
                "Mengirim prompt ke Gemini..."
            )

            hasil = self.ai.analisis(
                mata_kuliah.nama,
                prompt
            )

            self.logger.info(
                "Gemini selesai memberikan jawaban."
            )

            # ---------------------------------------------
            # Simpan hasil
            # ---------------------------------------------
            self.result.simpan(
                hasil
            )

            self.logger.info(
                "Hasil berhasil disimpan."
            )

            self.logger.info(
                f"Analisis selesai: {mata_kuliah.nama}"
            )

            return hasil

        except Exception as e:

            self.logger.error(
                f"Terjadi kesalahan: {str(e)}"
            )

            raise