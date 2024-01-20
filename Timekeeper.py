import subprocess

class Timekeeper:
    def __init__(self):
        self.connected = False

    def connect_js(self, gameid):
        self.timekeeper_proc = subprocess.Popen('node .\quadballlive_api\quadballlive_api.js' + " " + gameid)
        self.connected = True

    def disconnect_js(self):
        self.timekeeper_proc.kill()
        open("quadballlive_api/connected.txt", "w").write("false")
        self.connected = False