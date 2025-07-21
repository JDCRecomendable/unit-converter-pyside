# This Python file uses the following encoding: utf-8
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication

from unit_conversion import load_units
from window import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow(load_units(Path("unitDefinitions.json")))
    widget.show()
    sys.exit(app.exec())
