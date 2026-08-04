"""
=========================================================
AI Service
=========================================================
Mengirim prompt ke Google Gemini dan menerima hasil analisis.
=========================================================
"""

import time

from google import genai

from services.config import (
    GEMINI_API_KEY,
    AI_MODEL,
)

from services.models import (
    PromptAI,
    HasilAnalisis,
)


class AIService:

    def __init__(self):

        if not GEMINI_API_KEY:

            raise ValueError(
                "GEMINI_API_KEY belum ditemukan pada file .env"
            )

        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

   # =====================================================
# ANALISIS
# =====================================================

def analisis(
    self,
    mata_kuliah: str,
    prompt: PromptAI
) -> HasilAnalisis:

    mulai = time.perf_counter()

    try:

        response = self.client.models.generate_content(

            model=AI_MODEL,

            contents=prompt.isi

        )

        selesai = time.perf_counter()

        waktu = selesai - mulai

        isi = getattr(
            response,
            "text",
            ""
        )

        if not isi.strip():

            raise RuntimeError(
                "Gemini tidak mengembalikan hasil analisis."
            )

        return HasilAnalisis(

            mata_kuliah=mata_kuliah,

            model=AI_MODEL,

            prompt_token=prompt.estimasi_token,

            completion_token=0,

            total_token=prompt.estimasi_token,

            estimasi_biaya=0.0,

            waktu_proses=waktu,

            isi=isi

        )

    except Exception as e:

        raise RuntimeError(
            f"Gagal menghubungi Google Gemini: {e}"
        ) from e