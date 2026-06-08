from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from config import API_KEY,WEATHER_URL
import requests
class WeatherScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.search()
    def get_weather(self,city):
        params={
            "q":city,
            "appid":API_KEY,
            "units":"metric",
            "lang":"ua"}
        response=requests.get(WEATHER_URL,params=params)
        data=response.json()
        return data
    def search(self):
        weather=self.get_weather("Львів")
        print(weather)
class WeatherApp(MDApp):
    def build(self):
        Builder.load_file("style.kv")
        self.theme_cls.primary_palette="Purple"
        sm=MDScreenManager()
        sm.add_widget(WeatherScreen(name="weather"))
        return sm


WeatherApp().run()
