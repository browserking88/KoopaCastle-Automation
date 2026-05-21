#!/usr/bin/env python3

class LightingSystem:
    def __init__(self):
        self.lights = {}
        self.mode = "auto"
    
    def set_light(self, room, brightness):
        self.lights[room] = brightness
        return f"{room} brightness set to {brightness}%"
    
    def all_on(self):
        for room in self.lights:
            self.lights[room] = 100
        return "All lights on"
    
    def all_off(self):
        for room in self.lights:
            self.lights[room] = 0
        return "All lights off"
    
    def set_mode(self, mode):
        self.mode = mode
        return f"Mode set to {mode}"

if __name__ == "__main__":
    lights = LightingSystem()
    print(lights.all_on())
