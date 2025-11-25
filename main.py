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

        # First grid: labels + inputs
        self.grid_one = GridLayout(cols=2)
        
        # Store inputs as attributes on self
        self.name_input = self.Label_input("name_input", "Name:", False, self.grid_one)
        self.address_input = self.Label_input("address_input", "Address:", True, self.grid_one)
        self.email_input = self.Label_input("email_input", "Email:", False, self.grid_one)

        self.add_widget(self.grid_one)

        # Example: access the textinput object
        print("Name widget:", self.name_input)
        # print("Name text:", self.name_input.text)  # empty at start

        button = self.Make_button("Submit")
        button.bind(on_press=self.pressed)

    def Label_input(self, attr_name, label_text, multiline=False, grid_position=None):
        """Create a label + text input, attach the text input to self.attr_name."""
        label = Label(text=label_text)
        text_input = TextInput(multiline=multiline)

        if grid_position is None:
            self.add_widget(label)
            self.add_widget(text_input)
        else:
            grid_position.add_widget(label)
            grid_position.add_widget(text_input)

        # Attach to self so you can use it later
        setattr(self, attr_name, text_input)
        return text_input

    def Make_button(self, button_text, grid_position=None):
        button = Button(text=button_text, font_size=32)
        if grid_position is None:
            self.add_widget(button)
        else:
            grid_position.add_widget(button)
        return button

    def pressed(self, instance):
        # Read user input from text fields
        name = self.name_input.text
        address = self.address_input.text
        email = self.email_input.text

        print("Name:", name)
        print("Address:", address)
        print("Email:", email)


class MyApp(App):
    def build(self):
        Window.clear_color = (1, 0, 0, 1)
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
