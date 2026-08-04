"""
=========================================================
Aplikasi Refleksi AI Mahasiswa PPG
=========================================================
Entry Point Aplikasi Flask
=========================================================
"""

import os

from flask import Flask

from config import Config

from routes.main import main


# ==========================================================
# INISIALISASI FLASK
# ==========================================================

app = Flask(__name__)

app.config.from_object(Config)


# ==========================================================
# REGISTER BLUEPRINT
# ==========================================================

app.register_blueprint(main)


# ==========================================================
# MAIN
# ==========================================================

if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=int(
            os.environ.get(
                "PORT",
                5000
            )
        ),

        debug=True

    )