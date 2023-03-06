from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

# Load the KV language file
Builder.load_file("TheLab.kv")

# Define the MainWidget class
class MainWidget(Widget):
    def on_button_click(self):
        print("Button clicked!")
    
    def on_button2_click(self):
        print("Button 2 clicked!")

class TheLabApp(App):
    def build(self):
        return MainWidget()

TheLabApp().run()