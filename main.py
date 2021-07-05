from kivy.core.window import Window
Window.size = (1000, 800)

from kivy.clock import Clock
Clock.max_iteration = 20

from kivy.lang import Builder
from kivy.app import App
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen



class MyBoxLayout(MDBoxLayout):
    pass

class InputPage(Screen):
    pass

class OutputPage(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class MainApp(MDApp):
    def build(self):
        return MyBoxLayout()
 
blApp = MainApp()
 
blApp.run()

