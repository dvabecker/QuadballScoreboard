from PyQt5.QtWidgets import QDialog
from timekeeper_ui import Ui_Timekeeper
from Timekeeper import Timekeeper
import time
import subprocess


class TimekeeperWindow(QDialog):
    def __init__(self, scoreboard, main_ui):
        super().__init__()
        self.ui = Ui_Timekeeper()
        self.ui.setupUi(self)
        self.scoreboard = scoreboard
        self.main = main_ui
        self.timekeeper = Timekeeper()

    def fetch_games(self):
        file_path = "quadballlive_api/gameidstonames_livestream.txt"
        open(file_path, "w").write("")
        self.gameidstonames_proc = subprocess.Popen('node .\quadballlive_api\quadballlive_gameidtonames.js GameIDs_Livestream.txt gameidstonames_livestream.txt')
        time.sleep(3)
        self.gameidstonames_proc.kill()
        try:
            with open(file_path, "r") as file:
                lines = file.readlines()  # Read all lines from the file
                self.ui.comboBox.clear()  # Clear existing items from comboBox
                for line in lines:
                    line = line.strip()  # Remove any extra whitespace/newlines
                    if line:  # Only add non-empty lines
                        self.ui.comboBox.addItem(line)  # Add each line as an item
        except FileNotFoundError:
            print(f"File {file_path} not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def connect(self):
        self.scoreboard.time.stop()
        current_gameID = self.ui.comboBox.currentText()
        if ":" in current_gameID:
            current_gameID = current_gameID.split(":")[0]
        self.timekeeper.gameid = current_gameID
        if (self.timekeeper.gameid == ""):
            return
        self.timekeeper.connect_js(self.timekeeper.gameid)
        self.scoreboard.timekeeper = self.timekeeper
        if self.timekeeper.connected:
            self.main.ui.timekeeperButton.setText("Stop Timekeeper")
        self.accept()

    def disconnect(self):
        self.timekeeper.disconnect_js()