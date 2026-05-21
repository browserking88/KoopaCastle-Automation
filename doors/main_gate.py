#!/usr/bin/env python3

class MainGate:
    def __init__(self):
        self.status = "locked"
        self.alarm = True
        self.location = "KoopaCastle-LDN"
    
    def unlock(self, code):
        if code == "1985":
            self.status = "unlocked"
            return True
        return False
    
    def lock(self):
        self.status = "locked"
        return True
    
    def trigger_alarm(self):
        self.alarm = True
        return "ALARM TRIGGERED"

if __name__ == "__main__":
    gate = MainGate()
    print(f"Gate Status: {gate.status}")
