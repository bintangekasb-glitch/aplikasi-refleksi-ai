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

    MAX_RETRY = 3

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

        error_terakhir = None

        for percobaan in range(1, self.MAX_RETRY + 1):

            try:

                print(
                    f"[Gemini] Percobaan {percobaan}/{self.MAX_RETRY}"
                )

                response = self.client.models.generate_content(

                    model=AI_MODEL,

                    contents=prompt.isi

                )

                selesai = time.perf_counter()

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

                    waktu_proses=selesai - mulai,

                    isi=isi

                )

            except Exception as e:

                error_terakhir = e

                pesan = str(e)

                print(f"[Gemini] Error: {pesan}")

                # Retry hanya untuk error sementara
                if (
                    "503" in pesan
                    or "429" in pesan
                ) and percobaan < self.MAX_RETRY:

                    jeda = 2 ** percobaan

                    print(
                        f"[Gemini] Menunggu {jeda} detik sebelum mencoba lagi..."
                    )

                    time.sleep(jeda)

                    continue

                break

        raise RuntimeError(
            f"Gagal menghubungi Google Gemini setelah {self.MAX_RETRY} percobaan.\n\n{error_terakhir}"
        ) from error_terakhir