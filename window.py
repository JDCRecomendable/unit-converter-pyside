# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QModelIndex, Qt, Slot
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from unit_conversion import UnitCategory

class MainWindow(QMainWindow):
    def __init__(self, unit_definitions: list[UnitCategory], parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        unit_category_model = QStandardItemModel()
        self.ui.unitCategoryListView.setModel(unit_category_model)
        for unit_category in unit_definitions:
            unit_category_name = unit_category.get_name()
            unit_category_item = QStandardItem(unit_category_name)
            unit_category_item.setFlags(unit_category_item.flags()  & ~Qt.ItemIsEditable)
            unit_category_model.appendRow(unit_category_item)

    @Slot("QModelIndex")
    def on_unitCategoryListView_clicked(self, model_index: QModelIndex):
        print(type(model_index))
        print(model_index)
        print(model_index.row())
        print(model_index.data())
        print()
