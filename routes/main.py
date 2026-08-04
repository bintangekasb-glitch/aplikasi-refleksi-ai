"""
=========================================================
Main Routes
=========================================================
"""

from pathlib import Path

from flask import (
    Blueprint,
    render_template,
    abort,
    send_file,
    request,
    redirect,
    url_for,
    flash,
)

from services.document_reader import DocumentReader
from services.analysis_service import AnalysisService
from services.result_service import ResultService
from services.dashboard_service import DashboardService
from services.word_service import WordService
from services.folder_service import FolderService
from services.upload_service import UploadService
from services.file_service import FileService
from services.models import HasilAnalisis
from services.preview_service import PreviewService


main = Blueprint("main", __name__)

ROOT_FOLDER = Path("mata_kuliah")


reader = DocumentReader()
analysis_service = AnalysisService()
result_service = ResultService()
dashboard_service = DashboardService()
word_service = WordService()
folder_service = FolderService()
upload_service = UploadService()
file_service = FileService()
preview_service = PreviewService()


# ==========================================================
# DASHBOARD
# ==========================================================

@main.route("/")
def index():

    dashboard = dashboard_service.data_dashboard()

    return render_template(
        "index.html",
        dashboard=dashboard
    )


# ==========================================================
# FORM TAMBAH MATA KULIAH
# ==========================================================

@main.route("/mata-kuliah/baru")
def form_tambah_mata_kuliah():

    return render_template(
        "tambah_mata_kuliah.html"
    )


# ==========================================================
# SIMPAN MATA KULIAH
# ==========================================================

@main.route(
    "/mata-kuliah/tambah",
    methods=["POST"]
)
def tambah_mata_kuliah():

    nama = request.form.get(
        "nama",
        ""
    ).strip()

    try:

        folder_service.buat_mata_kuliah(
            nama
        )

        flash(
            "Mata kuliah berhasil dibuat.",
            "success"
        )

        return redirect(
            url_for("main.index")
        )

    except Exception as e:

        flash(
            str(e),
            "danger"
        )

        return redirect(
            url_for(
                "main.form_tambah_mata_kuliah"
            )
        )


# ==========================================================
# FORM RENAME MATA KULIAH
# ==========================================================

@main.route(
    "/mata-kuliah/<nama>/rename"
)
def form_rename_mata_kuliah(nama):

    folder = ROOT_FOLDER / nama

    if not folder.exists():

        abort(404)

    return render_template(
        "rename_mata_kuliah.html",
        nama=nama
    )


# ==========================================================
# SIMPAN RENAME MATA KULIAH
# ==========================================================

@main.route(
    "/mata-kuliah/<nama>/rename",
    methods=["POST"]
)
def rename_mata_kuliah(nama):

    nama_baru = request.form.get(
        "nama",
        ""
    ).strip()

    try:

        folder_service.rename_mata_kuliah(
            nama,
            nama_baru
        )

        flash(
            "Nama mata kuliah berhasil diubah.",
            "success"
        )

        return redirect(
            url_for(
                "main.detail_mata_kuliah",
                nama=nama_baru
            )
        )

    except Exception as e:

        flash(
            str(e),
            "danger"
        )

        return redirect(
            url_for(
                "main.form_rename_mata_kuliah",
                nama=nama
            )
        )


# ==========================================================
# HAPUS MATA KULIAH
# ==========================================================

@main.route(
    "/mata-kuliah/<nama>/hapus",
    methods=["POST"]
)
def hapus_mata_kuliah(nama):

    try:

        folder_service.hapus_mata_kuliah(
            nama
        )

        flash(
            "Mata kuliah berhasil dihapus.",
            "success"
        )

    except Exception as e:

        flash(
            str(e),
            "danger"
        )

    return redirect(
        url_for("main.index")
    )


# ==========================================================
# DETAIL MATA KULIAH
# ==========================================================

@main.route("/mata-kuliah/<nama>")
def detail_mata_kuliah(nama):

    folder = ROOT_FOLDER / nama

    if not folder.exists():

        abort(404)

    mk = reader.baca_mata_kuliah(
        folder
    )

    hasil = result_service.baca(
        nama
    )

    return render_template(
        "detail.html",
        mata_kuliah=mk,
        hasil=hasil
    )


# ==========================================================
# UPLOAD MODUL
# ==========================================================

@main.route(
    "/mata-kuliah/<nama>/upload/modul",
    methods=["POST"]
)
def upload_modul(nama):

    try:

        files = request.files.getlist(
            "file"
        )

        hasil = upload_service.upload_banyak(
            nama_mk=nama,
            kategori="modul",
            files=files
        )

        flash(
            f"{len(hasil)} file modul berhasil diupload.",
            "success"
        )

    except Exception as e:

        flash(
            str(e),
            "danger"
        )

    return redirect(
        url_for(
            "main.detail_mata_kuliah",
            nama=nama
        )
    )


# ==========================================================
# UPLOAD ARTEFAK
# ==========================================================

@main.route(
    "/mata-kuliah/<nama>/upload/artefak",
    methods=["POST"]
)
def upload_artefak(nama):

    try:

        files = request.files.getlist(
            "file"
        )

        hasil = upload_service.upload_banyak(
            nama_mk=nama,
            kategori="artefak",
            files=files
        )

        flash(
            f"{len(hasil)} file artefak berhasil diupload.",
            "success"
        )

    except Exception as e:

        flash(
            str(e),
            "danger"
        )

    return redirect(
        url_for(
            "main.detail_mata_kuliah",
            nama=nama
        )
    )
    
# ==========================================================
# DOWNLOAD FILE ASLI
# ==========================================================

@main.route(
    "/file/<nama>/<kategori>/<path:nama_file>"
)
def download_file(
    nama,
    kategori,
    nama_file
):

    try:

        folder = file_service.folder(
            nama,
            kategori
        )

        file = folder / nama_file

        if not file.exists():

            abort(404)

        return send_file(
            file,
            as_attachment=True,
            download_name=file.name
        )

    except Exception:

        abort(404)

# ==========================================================
# PREVIEW FILE
# ==========================================================

@main.route(
    "/preview/<nama>/<kategori>/<path:nama_file>"
)
def preview_file(
    nama,
    kategori,
    nama_file
):

    try:

        file = preview_service.file(
            nama,
            kategori,
            nama_file
        )

        if not preview_service.bisa_preview(file):

            flash(
                "Preview hanya tersedia untuk file PDF.",
                "warning"
            )

            return redirect(
                url_for(
                    "main.detail_mata_kuliah",
                    nama=nama
                )
            )

        return send_file(
            file,
            as_attachment=False
        )

    except Exception:

        abort(404)

# ==========================================================
# HAPUS FILE
# ==========================================================

@main.route(
    "/file/<nama>/<kategori>/<path:nama_file>/hapus",
    methods=["POST"]
)
def hapus_file(
    nama,
    kategori,
    nama_file
):

    try:

        file_service.hapus(
            nama,
            kategori,
            nama_file
        )

        flash(
            "File berhasil dihapus.",
            "success"
        )

    except Exception as e:

        flash(
            str(e),
            "danger"
        )

    return redirect(
        url_for(
            "main.detail_mata_kuliah",
            nama=nama
        )
    )


# ==========================================================
# ANALISIS
# ==========================================================

@main.route(
    "/mata-kuliah/<nama>/analisis"
)
def analisis(nama):

    folder = ROOT_FOLDER / nama

    if not folder.exists():

        abort(404)

    hasil = analysis_service.analisis(
        folder
    )

    return render_template(
        "hasil.html",
        hasil=hasil
    )


# ==========================================================
# HASIL TERAKHIR
# ==========================================================

@main.route(
    "/hasil/<nama>"
)
def hasil_terakhir(nama):

    data = result_service.baca(
        nama
    )

    if data is None:

        abort(404)

    hasil = HasilAnalisis(
        **data
    )

    return render_template(
        "hasil.html",
        hasil=hasil
    )


# ==========================================================
# DOWNLOAD WORD
# ==========================================================

@main.route(
    "/hasil/<nama>/word"
)
def download_word(nama):

    data = result_service.baca(
        nama
    )

    if data is None:

        abort(404)

    hasil = HasilAnalisis(
        **data
    )

    file = word_service.export(
        hasil
    )

    return send_file(
        file,
        as_attachment=True,
        download_name=file.name
    )


# ==========================================================
# ABOUT
# ==========================================================

@main.route("/about")
def about():

    return render_template(
        "about.html"
    )


# ==========================================================
# ERROR HANDLER
# ==========================================================

@main.app_errorhandler(404)
def error_404(error):

    return render_template(
        "404.html"
    ), 404


@main.app_errorhandler(500)
def error_500(error):

    return render_template(
        "500.html"
    ), 500