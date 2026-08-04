"""
=========================================================
Tes AI Service
=========================================================
Menguji integrasi DocumentReader, PromptBuilder,
dan AIService (Google Gemini).
=========================================================
"""

from pathlib import Path

from services.document_reader import DocumentReader
from services.prompt_builder import PromptBuilder
from services.ai_service import AIService


def main():

    print("=" * 60)
    print("TES AI SERVICE (GOOGLE GEMINI)")
    print("=" * 60)

    folder = Path("mata_kuliah")

    daftar = sorted(
        item
        for item in folder.iterdir()
        if item.is_dir()
    )

    if not daftar:

        print()
        print("Belum ada mata kuliah.")
        return

    # =====================================================
    # BACA DOKUMEN
    # =====================================================

    reader = DocumentReader()

    mata_kuliah = reader.baca_mata_kuliah(
        daftar[0]
    )

    print()
    print(f"Mata Kuliah : {mata_kuliah.nama}")
    print(f"Jumlah File : {mata_kuliah.jumlah_file}")
    print(f"Karakter    : {mata_kuliah.jumlah_karakter:,}")

    # =====================================================
    # BANGUN PROMPT
    # =====================================================

    builder = PromptBuilder()

    prompt = builder.buat_prompt(
        mata_kuliah
    )

    print()
    print(f"Prompt : {prompt.jumlah_karakter:,} karakter")
    print(f"Token  : {prompt.estimasi_token:,}")

    # =====================================================
    # ANALISIS AI
    # =====================================================

    print()
    print("Mengirim prompt ke Google Gemini...")
    print()

    ai = AIService()

    hasil = ai.analisis(
        mata_kuliah.nama,
        prompt
    )

    print("=" * 60)
    print("HASIL ANALISIS")
    print("=" * 60)

    print()

    print(f"Model           : {hasil.model}")
    print(f"Waktu Proses    : {hasil.waktu_proses:.2f} detik")
    print(f"Prompt Token    : {hasil.prompt_token:,}")

    print()

    print("=" * 60)
    print("ISI REFLEKSI")
    print("=" * 60)

    print()

    print(hasil.isi)


if __name__ == "__main__":
    main()