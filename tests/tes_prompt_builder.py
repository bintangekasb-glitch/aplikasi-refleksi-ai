from pathlib import Path

from services.document_reader import DocumentReader
from services.prompt_builder import PromptBuilder


def main():

    folder = Path("mata_kuliah")

    daftar = sorted(
        item
        for item in folder.iterdir()
        if item.is_dir()
    )

    if not daftar:

        print("Belum ada mata kuliah.")
        return

    reader = DocumentReader()

    mata_kuliah = reader.baca_mata_kuliah(
        daftar[0]
    )

    builder = PromptBuilder()

    prompt = builder.buat_prompt(
        mata_kuliah
    )

    print("=" * 60)
    print("TES PROMPT BUILDER")
    print("=" * 60)

    print()

    print(
        prompt.isi[:3000]
    )

    print()

    print("=" * 60)
    print(
        f"Jumlah Karakter : {prompt.jumlah_karakter:,}"
    )

    print(
        f"Estimasi Token  : {prompt.estimasi_token:,}"
    )

    print("=" * 60)


if __name__ == "__main__":
    main()