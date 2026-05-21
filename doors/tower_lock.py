#!/usr/bin/env python3

class TowerLock:
    def __init__(self, tower_id):
        self.tower_id = tower_id
        self.locked = True
        self.access_log = []
    
    def unlock(self, device_id):
        self.locked = False
        self.access_log.append(f"Unlocked by {device_id}")
        return f"Tower {self.tower_id} unlocked"
    
    def lock(self):
        self.locked = True
        return f"Tower {self.tower_id} locked"
    
    def get_status(self):
        return {"tower": self.tower_id, "locked": self.locked, "logs": self.access_log}

if __name__ == "__main__":
    lock = TowerLock("Tower7")
    print(lock.get_status())
