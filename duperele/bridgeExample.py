# Define the abstraction interface
class GUI:
    def __init__(self, implementation):
        self.implementation = implementation

    def draw_button(self):
        self.implementation.draw_button()

    def draw_textbox(self):
        self.implementation.draw_textbox()


# Define the implementation interface
class GUIImplementation:
    def draw_button(self):
        pass

    def draw_textbox(self):
        pass


# Create concrete implementations
class WinAPI(GUIImplementation):
    def draw_button(self):
        print("Drawing a button using WinAPI")

    def draw_textbox(self):
        print("Drawing a textbox using WinAPI")


class GTK(GUIImplementation):
    def draw_button(self):
        print("Drawing a button using GTK")

    def draw_textbox(self):
        print("Drawing a textbox using GTK")


# Create the client code
class Main:
    def __init__(self, gui):
        self.gui = gui

    def run(self):
        self.gui.draw_button()
        self.gui.draw_textbox()


# Use the Bridge Design Pattern to create a GUI application that can work with different APIs
win_gui = GUI(WinAPI())
gtk_gui = GUI(GTK())

main1 = Main(win_gui)
main1.run()  # Output: Drawing a button using WinAPI\nDrawing a textbox using WinAPI

main2 = Main(gtk_gui)
main2.run()  # Output: Drawing a button using GTK\nDrawing a textbox using GTK
