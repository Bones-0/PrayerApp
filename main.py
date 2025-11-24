from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        
        self.grid_one = GridLayout()    
        self.grid_one.cols = 2

        self.grid_two = GridLayout()
        self.grid_two.cols = 2

        self.Label_input("name", "Name:", False, self.grid_one)
        self.Label_input("address", "Address:", True, self.grid_one)
        self.Label_input("email", "Email:", False, self.grid_one)
        self.Make_button("Submit", self.grid_two)

    def Label_input(self, variable_name, label_text, multipleline=False, grid_position):
        if grid_position is None:
            self.add_widget(Label(text=label_text, font_size=32))
            if multipleline:
                setattr(self, variable_name, TextInput(font_size=32, multiline=True))
            else:
                setattr(self, variable_name, TextInput(font_size=32, multiline=False))
            self.add_widget(getattr(self, variable_name))
        else:
            grid_position.add_widget(Label(text=label_text))
            grid_position.variable_name = TextInput(multiline=multipleline)
            grid_position.add_widget(self.variable_name)
    def Make_button(self, button_text):
        self.add_widget(Button(text=button_text, font_size=32))

class MyApp(App):
    def build(self):
        Window.clear_color = (1, 0, 0, 1)
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()