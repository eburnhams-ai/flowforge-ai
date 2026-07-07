from views.dashboard import render_dashboard
from views.placeholder import render_placeholder
from views.file_organizer import render_file_organizer
from views.duplicates import render_duplicates
from views.settings import render_settings


ROUTES = {
    "dashboard": render_dashboard,
    "file_organizer": render_file_organizer,
    "duplicates": render_duplicates,
    "pdf": lambda: render_placeholder("PDF Toolkit", "Merge, split, compress, and prepare PDFs."),
    "images": lambda: render_placeholder("Image Toolkit", "Resize, convert, compress, and watermark images."),
    "excel": lambda: render_placeholder("Excel Toolkit", "Clean spreadsheets, remove duplicates, and standardize data."),
    "ai": lambda: render_placeholder("AI Assistant", "Classify, summarize, and rename documents intelligently."),
    "settings": render_settings,
}


def render_current_page(page_key: str) -> None:
    view = ROUTES.get(page_key, render_dashboard)
    view()
