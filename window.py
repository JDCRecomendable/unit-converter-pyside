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

        self.unit_definitions = unit_definitions

        unit_category_model = QStandardItemModel()
        self.from_unit_model = QStandardItemModel()
        self.to_unit_model = QStandardItemModel()

        self.ui.unitCategoryListView.setModel(unit_category_model)
        self.ui.fromUnitPicker.setModel(self.from_unit_model)
        self.ui.toUnitPicker.setModel(self.to_unit_model)

        for unit_category in self.unit_definitions:
            unit_category_name = unit_category.get_name()
            unit_category_item = QStandardItem(unit_category_name)
            unit_category_item.setFlags(unit_category_item.flags()  & ~Qt.ItemIsEditable)
            unit_category_model.appendRow(unit_category_item)

    @Slot("QModelIndex")
    def on_unitCategoryListView_clicked(self, model_index: QModelIndex):
        self.from_unit_model.clear()
        self.to_unit_model.clear()

        target_unit_category = self.unit_definitions[model_index.row()]
        target_units = target_unit_category.get_units()
        for unit in target_units:
            from_unit_item = QStandardItem(f"{unit.get_name()} [{unit.get_abbr()}]")
            from_unit_item.setFlags(from_unit_item.flags()  & ~Qt.ItemIsEditable)
            self.from_unit_model.appendRow(from_unit_item)
            to_unit_item = QStandardItem(f"{unit.get_name()} [{unit.get_abbr()}]")
            to_unit_item.setFlags(to_unit_item.flags()  & ~Qt.ItemIsEditable)
            self.to_unit_model.appendRow(to_unit_item)

        if self.from_unit_model.rowCount() > 0:
            from_index = self.from_unit_model.index(0, 0)
            self.ui.fromUnitPicker.setCurrentIndex(from_index)
        if self.to_unit_model.rowCount() > 0:
            to_index = self.to_unit_model.index(0, 0)
            self.ui.toUnitPicker.setCurrentIndex(to_index)
