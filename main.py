from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen

import requests
class WeatherScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class WeatherApp(MDApp):
    def build(self):
        Builder.load_file("style.kv")
        self.theme_cls.primary_palette="Purple"
        sm=MDScreenManager()
        sm.add_widget(WeatherScreen(name="weather"))
        return sm


WeatherApp().run()
