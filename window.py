# This Python file uses the following encoding: utf-8
from decimal import Decimal

from PySide6.QtCore import QModelIndex, Qt, Slot
from PySide6.QtGui import QDoubleValidator, QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from unit_conversion import convert, UnitCategory

class MainWindow(QMainWindow):
    def __init__(self, unit_definitions: list[UnitCategory], parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.unit_definitions = unit_definitions

        unit_category_model = QStandardItemModel()
        self.from_unit_model = QStandardItemModel()
        self.to_unit_model = QStandardItemModel()
        double_validator = QDoubleValidator(parent=self.ui.fromUnitInput)

        self.ui.unitCategoryListView.setModel(unit_category_model)
        self.ui.fromUnitPicker.setModel(self.from_unit_model)
        self.ui.toUnitPicker.setModel(self.to_unit_model)
        self.ui.fromUnitInput.setValidator(double_validator)

        unit_category_selection_model = self.ui.unitCategoryListView.selectionModel()
        from_unit_selection_model = self.ui.fromUnitPicker.selectionModel()
        to_unit_selection_model = self.ui.toUnitPicker.selectionModel()
        unit_category_selection_model.currentChanged.connect(self.on_unitCategoryListView_currentChanged)
        from_unit_selection_model.currentChanged.connect(self.on_fromUnitPicker_currentChanged)
        to_unit_selection_model.currentChanged.connect(self.on_toUnitPicker_currentChanged)

        for unit_category in self.unit_definitions:
            unit_category_name = unit_category.get_name()
            unit_category_item = QStandardItem(unit_category_name)
            unit_category_item.setFlags(unit_category_item.flags()  & ~Qt.ItemIsEditable)
            unit_category_model.appendRow(unit_category_item)

        self.ui.statusbar.showMessage("Application ready. Select a unit category.")

    @Slot("QModelIndex")
    def on_unitCategoryListView_currentChanged(self, model_index: QModelIndex):
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

        self.ui.statusbar.showMessage(f"{target_unit_category.get_name()} units loaded.")

    @Slot("QModelIndex")
    def on_fromUnitPicker_currentChanged(self, model_index: QModelIndex):
        self.perform_conversion()

    @Slot("QModelIndex")
    def on_toUnitPicker_currentChanged(self, model_index: QModelIndex):
        self.perform_conversion()

    @Slot(str)
    def on_fromUnitInput_textEdited(self, text: str):
        self.perform_conversion()

    @Slot(bool)
    def on_resetButton_clicked(self, checked: bool):
        self.ui.fromUnitInput.setText("")
        self.perform_conversion()
        self.ui.statusbar.showMessage("Text fields have been reset.")

    def perform_conversion(self):
        raw_value = self.ui.fromUnitInput.text()
        if len(raw_value) == 0:
            self.ui.toUnitOutput.setText("")
            self.ui.statusbar.clearMessage()
            return
        value = Decimal(raw_value)
        unit_category_index = self.ui.unitCategoryListView.currentIndex()
        from_unit_index = self.ui.fromUnitPicker.currentIndex()
        to_unit_index = self.ui.toUnitPicker.currentIndex()

        from_unit_index_int = from_unit_index.row()
        to_unit_index_int = to_unit_index.row()
        if (from_unit_index_int == -1 or to_unit_index_int == -1):
            self.ui.fromUnitInput.setText("")
            self.ui.toUnitOutput.setText("")
            self.ui.statusbar.clearMessage()
            return

        target_units = self.unit_definitions[unit_category_index.row()]
        from_unit = target_units.get_units()[from_unit_index_int]
        to_unit = target_units.get_units()[to_unit_index_int]
        decimal_result = convert(value, from_unit, to_unit)
        f_result = float(decimal_result)
        i_result = int(decimal_result)
        result = str(i_result) if (i_result - f_result == 0) else str(round(f_result, 5))
        self.ui.toUnitOutput.setText(result)
        self.ui.statusbar.showMessage(f"Conversion from {from_unit.get_name()} to {to_unit.get_name()} successful.")
