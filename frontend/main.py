from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button 
from kivy.uix.popup import Popup
from kivy.uix.checkbox import CheckBox
from kivy.uix.boxlayout import BoxLayout
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

        main_layout = BoxLayout(orientation='vertical')
        second_layout = GridLayout(cols = 2, padding = 10, row_force_default=True, row_default_height=40)
        checkbox_layout = GridLayout(cols = 2, padding = 10, row_force_default=True, row_default_height=40)
  
        popup_label = Label(text = text) 
        allow_button = Button(text = "Allow") 
        deny_button = Button(text = "Deny")
        checkbox_text = Label(text = "Apply for all ports in destination host")
        checkbox = CheckBox()
  
        second_layout.add_widget(allow_button)
        second_layout.add_widget(deny_button)
        checkbox_layout.add_widget(checkbox)
        checkbox_layout.add_widget(checkbox_text)        

        main_layout.add_widget(popup_label) 
        main_layout.add_widget(checkbox_layout)
        main_layout.add_widget(second_layout)

        # Instantiate the modal popup and display 
        popup = Popup(title ='Hello', 
                      content = main_layout)      

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
    
    def on_stop(self):
        print('Closing')
        
    
        