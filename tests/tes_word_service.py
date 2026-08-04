"""
=========================================================
Tes Word Service
=========================================================
"""

from services.result_service import ResultService
from services.models import HasilAnalisis
from services.word_service import WordService


def main():

    print("=" * 60)
    print("TES WORD SERVICE")
    print("=" * 60)

    result = ResultService()

    data = result.baca("filosofi")

    if data is None:

        print("Belum ada hasil analisis.")

        return

    hasil = HasilAnalisis(**data)

    service = WordService()

    file = service.export(
        hasil
    )

    print()

    print("Berhasil membuat:")

    print(file)


if __name__ == "__main__":

    main()
    