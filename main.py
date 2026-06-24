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
        self.city="Попівці"
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
        try:
            self.city=self.ids.search_field.text
            weather=self.get_weather(self.city)
            self.show_weather(weather)
        except:
            print("помилка під час пошуку погоди")

    def show_weather(self, weather):
        temp=weather ["main"]["temp"]
        self.ids.temp_label.text=f"{round(temp)}°C"
        text=weather["weather"][0]["description"]
        self.ids.text_label.text=text
        icon= weather["weather"][0]["icon"]
        self.ids.icon.source=f"https://openweathermap.org/img/wn/{icon}@2x.png"
        rain=weather["rain"]["1h"] if "rain" in weather else 0
        self.ids.rain_label.text=f"Опади:{rain}мм"
        wind=weather["wind"]["speed"]
        self.ids.wind_label.text=f"Вітер:{wind}м/с"
        humidity=weather["main"]["humidity"]
        self.ids.humidity_label.text=f"Вологість:{humidity}%"
class WeatherApp(MDApp):
    def build(self):
        Builder.load_file("style.kv")
        self.theme_cls.primary_palette="Purple"
        sm=MDScreenManager()
        sm.add_widget(WeatherScreen(name="weather"))
        return sm


WeatherApp().run()
