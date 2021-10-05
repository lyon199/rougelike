#Does all the handling of the ui and objects associated with it
import ui, uiObjects, asciiDisplay

class UiMaster():
    def __init__(self):
        self.aui = ui.Ui(asciiDisplay.AsciiDisplay(204, 8))

    def create_ui_obj(x_pos, y_pos, string, var):
        uiObjects(x_pos, y_pos, string, var)

    def add_ui_obj():
        ui.aui.render_obj()

    def print():
        ui.self.print()
