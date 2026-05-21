#!/usr/bin/env python3

class WeatherControl:
    def __init__(self):
        self.city = "London"
        self.weather_mode = "Rainy"
        self.bridge_view = "Tower Bridge"
    
    def get_conditions(self):
        return {
            "city": self.city,
            "weather": self.weather_mode,
            "landmark": self.bridge_view
        }
    
    def set_weather_mode(self, mode):
        self.weather_mode = mode
        return f"Weather mode set to {mode}"

if __name__ == "__main__":
    weather = WeatherControl()
    print(weather.get_conditions())
