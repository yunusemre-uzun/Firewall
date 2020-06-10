from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button 
from kivy.uix.popup import Popup
from kivy.uix.checkbox import CheckBox
import time

class PromptScreen(GridLayout):

    def __init__(self, **kwargs):
        super(PromptScreen, self).__init__(**kwargs)
        self.cols = 2
        self.username = TextInput(multiline=False)
        self.add_widget(Label(text='prompt'))
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)
    
    
    def pop_up(self, text, allow_action, deny_action):
        self.allow_action = allow_action
        self.deny_action = deny_action
        self.checkbox_value = False

        layout = GridLayout(cols = 1, padding = 10) 
  
        popup_label = Label(text = text) 
        allow_button = Button(text = "Allow") 
        deny_button = Button(text = "Deny")
        checkbox = CheckBox()
  
        layout.add_widget(popup_label) 
        layout.add_widget(allow_button)
        layout.add_widget(deny_button)
        layout.add_widget(checkbox)        

        # Instantiate the modal popup and display 
        popup = Popup(title ='Hello', 
                      content = layout)      

        self.popup = popup
        # Attach close button press with popup.dismiss action 
        allow_button.bind(on_press = self.allow_connection)
        deny_button.bind(on_press = self.deny_connection)
        checkbox.bind(active=self.set_checkbox_active)

        popup.open()
    
    def set_checkbox_active(self, checkbox, value):
        self.checkbox_value = value

    def allow_connection(self, instance):
        self.popup.dismiss()
        self.allow_action(self.checkbox_value)
    
    def deny_connection(self, instance):
        self.popup.dismiss()
        self.deny_action(self.checkbox_value)
     

class MyApp(App):

    def build(self):
        self.prompt_screen = PromptScreen()
        return self.prompt_screen
    
    def show_pop_up(self, text, allow_action, deny_action):
        self.prompt_screen.pop_up(text, allow_action, deny_action)
        