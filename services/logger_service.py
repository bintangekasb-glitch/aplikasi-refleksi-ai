"""
=========================================================
Logger Service
=========================================================
Menyediakan logger sederhana untuk aplikasi.
=========================================================
"""

import logging
from pathlib import Path


class LoggerService:
    """
    Service untuk membuat logger aplikasi.
    """

    def __init__(self):

        folder = Path("logs")

        folder.mkdir(exist_ok=True)

        self.logger = logging.getLogger(
            "RefleksiAI"
        )

        if not self.logger.handlers:

            self.logger.setLevel(
                logging.INFO
            )

            file_handler = logging.FileHandler(
                folder / "app.log",
                encoding="utf-8"
            )

            formatter = logging.Formatter(

                "%(asctime)s | %(levelname)s | %(message)s"

            )

            file_handler.setFormatter(
                formatter
            )

            self.logger.addHandler(
                file_handler
            )

    def info(
        self,
        pesan: str
    ):

        self.logger.info(
            pesan
        )

    def error(
        self,
        pesan: str
    ):

        self.logger.error(
            pesan
        )