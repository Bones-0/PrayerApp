from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1
        
        self.grid_one = GridLayout()    
        self.grid_one.cols = 2

        self.Label_input("name", "Name:", False, self.grid_one)
        self.Label_input("address", "Address:", True, self.grid_one)
        self.Label_input("email", "Email:", False, self.grid_one)
        self.add_widget(self.grid_one)

        button = self.Make_button("Submit")
        button.bind(on_press=self.pressed(any, self.grid_one))

    def Label_input(self, variable_name, label_text, multipleline=False, grid_position=None):
        if grid_position is None:
            self.add_widget(Label(text=label_text))
            self.variable_name = TextInput(multiline=multipleline)
            self.add_widget(self.variable_name)
        else:
            grid_position.add_widget(Label(text=label_text))
            grid_position.variable_name = TextInput(multiline=multipleline)
            grid_position.add_widget(grid_position.variable_name)
    def Make_button(self, button_text, grid_position=None):
        button = None
        if grid_position is None:
            button = Button(text=button_text, font_size=32)
            self.add_widget(button)
        else:
            button = Button(text=button_text)
            grid_position.add_widget(button)
            self.add_widget(grid_position)
        return button;

    def pressed(self, instance):
        grid_one.name.text = "Name: " + self.name.text
        print("pressed")

class MyApp(App):
    def build(self):
        Window.clear_color = (1, 0, 0, 1)
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()