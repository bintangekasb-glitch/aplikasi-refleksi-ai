"""
=========================================================
Dashboard Service
=========================================================
Menghasilkan data statistik dashboard.
=========================================================
"""

from pathlib import Path

from services.document_reader import DocumentReader
from services.result_service import ResultService


class DashboardService:

    def __init__(self):

        self.reader = DocumentReader()

        self.result = ResultService()

        self.root = Path("mata_kuliah")

    # =====================================================
    # DATA DASHBOARD
    # =====================================================

    def data_dashboard(self):

        daftar = []

        total_file = 0

        total_karakter = 0

        total_analisis = 0

        for folder in sorted(self.root.iterdir()):

            if not folder.is_dir():

                continue

            mk = self.reader.baca_mata_kuliah(folder)

            sudah = self.result.sudah_ada(
                mk.nama
            )

            if sudah:

                total_analisis += 1

            total_file += mk.jumlah_file

            total_karakter += mk.jumlah_karakter

            daftar.append({

                "nama": mk.nama,

                "jumlah_file": mk.jumlah_file,

                "jumlah_karakter": mk.jumlah_karakter,

                "sudah_dianalisis": sudah

            })

        return {

            "jumlah_mata_kuliah": len(daftar),

            "jumlah_file": total_file,

            "jumlah_karakter": total_karakter,

            "jumlah_analisis": total_analisis,

            "daftar": daftar

        }
        