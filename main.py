from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2
        self.Label_input("name", "Name:", False)
    def Label_input(self, variable_name, label_text, multipleline=False):
        self.add_widget(Label(text=label_text))
        self.variable_name = TextInput(multiline=multipleline)
        self.add_widget(self.variable_name)

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()