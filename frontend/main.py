from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button 
from kivy.uix.popup import Popup
from kivy.uix.checkbox import CheckBox
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from RuleTable import RuleTable
import time

class PromptScreen(ScrollView):

    def __init__(self, **kwargs):
        super(PromptScreen, self).__init__(**kwargs)
        self.rule_table = RuleTable.getInstance()
        print(self.rule_table)
        self.size_hint = (1, None)
        self.size = (Window.width, Window.height)
        self.gridlayout = GridLayout(cols=6, spacing=10, size_hint_y=None)
        self.gridlayout.bind(minimum_height=self.gridlayout.setter('height'))
        columns = ["", "id", "ip", "port", "protocol", "allowed"]
        for col in columns:
            self.add_label(col)
        '''for rule_id, rule in self.rule_table.table.items():
            self.add_row(rule.get_parameters())'''
            
        self.add_widget(self.gridlayout)

    def add_label(self, label_text):
        label = Label(text=label_text, size_hint_y=None, height=40)
        self.gridlayout.add_widget(label)

    def add_row(self, label_list):
        self.gridlayout.add_widget(CheckBox())
        for label in label_list:
            self.add_label(str(label))
    
    def add_rule_to_row(self):
        all_keys = self.rule_table.table.keys()
        max_key = max(all_keys)
        rule = self.rule_table.table[max_key]
        self.add_row(rule.get_parameters())
    
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
        #self.add_rule_to_row()
    
    def deny_connection(self, instance):
        self.popup.dismiss()
        self.deny_action(self.checkbox_value)
        #self.add_rule_to_row()
     

class MyApp(App):

    def build(self):
        self.prompt_screen = PromptScreen()
        return self.prompt_screen
    
    def show_pop_up(self, text, allow_action, deny_action):
        try:
            self.prompt_screen.pop_up(text, allow_action, deny_action)
        except Exception as e:
            print("Popup exception:", e)
    
    def on_stop(self):
        print('Closing')
        
    
        