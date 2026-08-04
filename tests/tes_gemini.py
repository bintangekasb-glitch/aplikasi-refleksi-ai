from dotenv import load_dotenv
from google import genai

import os


def main():

    print("=" * 60)
    print("DAFTAR MODEL GEMINI")
    print("=" * 60)

    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print("GEMINI_API_KEY belum ditemukan.")
        return

    client = genai.Client(api_key=api_key)

    for model in client.models.list():

        if "generateContent" in model.supported_actions:

            print(model.name)


if __name__ == "__main__":
    main()