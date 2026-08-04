"""
=========================================================
Token Estimator Service
=========================================================
"""

from services.models import MataKuliah
from services.models import EstimasiToken

from services.config import (
    KARAKTER_PER_TOKEN,
    HARGA_PER_1000_TOKEN,
    DETIK_PER_1000_TOKEN,
    MODE_ANALISIS,
)


class TokenEstimator:

    def hitung(
        self,
        mata_kuliah: MataKuliah
    ) -> EstimasiToken:

        karakter = mata_kuliah.jumlah_karakter

        token = max(
            1,
            karakter // KARAKTER_PER_TOKEN
        )

        biaya = (
            token / 1000
        ) * HARGA_PER_1000_TOKEN

        waktu = max(
            1,
            round(
                (token / 1000)
                * DETIK_PER_1000_TOKEN
            )
        )

        return EstimasiToken(

            jumlah_karakter=karakter,

            estimasi_token=token,

            estimasi_biaya=biaya,

            estimasi_waktu=waktu,

            mode=MODE_ANALISIS

        )