# This Python file uses the following encoding: utf-8
from decimal import Decimal
import sys

from PySide6.QtCore import QModelIndex, Qt, Slot
from PySide6.QtGui import QDoubleValidator, QStandardItem, QStandardItemModel, QKeySequence
from PySide6.QtWidgets import QLineEdit, QMainWindow, QTextEdit, QApplication
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

        # region KEYBOARD SHORTCUTS > File menu shortcuts
        self.ui.actionQuit.setShortcut(QKeySequence.Quit)
        self.ui.actionQuit.triggered.connect(self.close)
        # endregion

        # region KEYBOARD SHORTCUTS > Edit menu shortcuts
        self.ui.actionUndo.setShortcut(QKeySequence.Undo)
        self.ui.actionRedo.setShortcut(QKeySequence.Redo)
        self.ui.actionCut.setShortcut(QKeySequence.Cut)
        self.ui.actionCopy.setShortcut(QKeySequence.Copy)
        self.ui.actionPaste.setShortcut(QKeySequence.Paste)
        self.ui.actionDelete.setShortcut(QKeySequence.Delete)
        self.ui.actionSelect_All.setShortcut(QKeySequence.SelectAll)
        self.ui.actionReset.setShortcut(QKeySequence.Refresh)
        # Clipboard copy actions shortcuts
        if sys.platform == "darwin":
            self.ui.actionCopy_Input_to_Clipboard.setShortcut(QKeySequence("Ctrl+Shift+C"))
            self.ui.actionCopy_Result_to_Clipboard.setShortcut(QKeySequence("Ctrl+Alt+C"))
        else:
            self.ui.actionCopy_Input_to_Clipboard.setShortcut(QKeySequence("Ctrl+Alt+C"))
            self.ui.actionCopy_Result_to_Clipboard.setShortcut(QKeySequence("Ctrl+Shift+C"))
        # endregion

        # region KEYBOARD SHORTCUTS > View menu shortcuts
        self.ui.actionUse_Smart_Rounding.setShortcut("Alt+Shift+Z")
        self.ui.actionRound_off_to_whole_number.setShortcut("Alt+Shift+W")
        self.ui.actionRound_off_to_1_d_p.setShortcut("Alt+Shift+1")
        self.ui.actionRound_off_to_2_d_p.setShortcut("Alt+Shift+2")
        self.ui.actionRound_off_to_3_d_p.setShortcut("Alt+Shift+3")
        self.ui.actionRound_off_to_4_d_p.setShortcut("Alt+Shift+4")
        self.ui.actionRound_off_to_5_d_p.setShortcut("Alt+Shift+5")
        self.ui.actionRound_off_to_6_d_p.setShortcut("Alt+Shift+6")
        self.ui.actionRound_off_to_7_d_p.setShortcut("Alt+Shift+7")
        self.ui.actionRound_off_to_8_d_p.setShortcut("Alt+Shift+8")
        self.ui.actionRound_off_to_9_d_p.setShortcut("Alt+Shift+9")
        self.ui.actionRound_off_to_10_d_p.setShortcut("Alt+Shift+0")
        # endregion

        # region KEYBOARD SHORTCUTS > Window menu shortcuts
        self.ui.actionMinimize.setShortcut(QKeySequence("Ctrl+M"))
        self.ui.actionZoom.setShortcut(QKeySequence("Ctrl+Shift+M"))
        self.ui.actionEnter_Full_Screen.setShortcut(QKeySequence.FullScreen)
        # endregion

        # region MAIN INIT

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

        # endregion

    # region MAIN ACTIONS

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

    @Slot()
    def on_resetButton_clicked(self):
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
        i_result = round(decimal_result)
        result = str(i_result) if (i_result - f_result == 0) else str(round(f_result, 5))
        self.ui.toUnitOutput.setText(result)
        self.ui.statusbar.showMessage(f"Conversion from {from_unit.get_name()} to {to_unit.get_name()} successful.")

    # endregion

    # region MENU ACTIONS > Edit menu

    @Slot()
    def on_actionUndo_triggered(self):
        w = self.focusWidget()
        if hasattr(w, "undo"):
            w.undo()
            self.ui.statusbar.showMessage("Undo successful.")

    @Slot()
    def on_actionRedo_triggered(self):
        w = self.focusWidget()
        if hasattr(w, "redo"):
            w.redo()
            self.ui.statusbar.showMessage("Redo successful.")

    @Slot()
    def on_actionCut_triggered(self):
        w = self.focusWidget()
        if hasattr(w, "cut"):
            w.cut()

    @Slot()
    def on_actionCopy_triggered(self):
        w = self.focusWidget()
        if hasattr(w, "copy"):
            w.copy()

    @Slot()
    def on_actionPaste_triggered(self):
        w = self.focusWidget()
        if hasattr(w, "paste"):
            w.paste()

    @Slot()
    def on_actionDelete_triggered(self):
        w = self.focusWidget()
        if isinstance(w, QLineEdit):
            pos = w.cursorPosition()
            text = w.text()
            sel_len = len(w.selectedText())
            if sel_len > 0:
                start = w.selectionStart()
                text = text[:start] + text[start + sel_len:]
                w.setText(text)
                w.setCursorPosition(start)
            elif pos < len(text):
                text = text[:pos] + text[pos + 1:]
                w.setText(text)
                w.setCursorPosition(pos)
        elif isinstance(w, QTextEdit):
            cursor = w.textCursor()
            if cursor.hasSelection():
                cursor.removeSelectedText()
            else:
                cursor.deleteChar()
            w.setTextCursor(cursor)

    @Slot()
    def on_actionSelect_All_triggered(self):
        w = self.focusWidget()
        if hasattr(w, "selectAll"):
            w.selectAll()

    @Slot()
    def on_actionReset_triggered(self):
        self.on_resetButton_clicked()

    @Slot()
    def on_actionCopy_Input_to_Clipboard_triggered(self):
        text = self.ui.fromUnitInput.text()
        QApplication.clipboard().setText(text)
        self.ui.statusbar.showMessage("Input value copied to clipboard.")

    @Slot()
    def on_actionCopy_Result_to_Clipboard_triggered(self):
        text = self.ui.toUnitOutput.text()
        QApplication.clipboard().setText(text)
        self.ui.statusbar.showMessage("Result copied to clipboard.")

    # endregion

    # region MENU ACTIONS > Window menu

    @Slot()
    def on_actionMinimize_triggered(self):
        self.showMinimized()

    @Slot()
    def on_actionZoom_triggered(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    @Slot()
    def on_actionEnter_Full_Screen_triggered(self):
        if self.windowState() & Qt.WindowFullScreen:
            self.showNormal()
        else:
            self.showFullScreen()

    # endregion
