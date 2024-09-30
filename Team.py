import codecs

class Team:
    def __init__(self):
        self.color = ""
        self.score = 0
        self.score_str = ""
        self.name = ""
        self.snitch_catch = []
        self.path = ""
        self.logo = ""
        self.roster = {}
        self.logo_scoreboard = ""

    def get_score_str(self):
        if self.score_str != "":
            return self.score_str
        else:
            out = str(self.score)
            if len(self.snitch_catch) == 0:
                return out
            else:
                for i in self.snitch_catch:
                    if i:
                        out += "*"
                    else:
                        out += "°"
                return out

    def set_path(self, path, datafile=""):
        self.path = path
        self.roster = {}
        if not datafile == "":
            with open(datafile, "w") as dat:
                dat.write(self.path)
        # set logo path
        self.logo = "Input/Teamlogos/" + self.path + ".png"
        self.logo_scoreboard = "Input/TeamlogosScoreboard/" + self.path + ".png"
        # set name and roster
        try:
            with codecs.open("Input/Teamrosters/"+self.path+".txt", "r", 'utf-8-sig') as roster_file:
                content = roster_file.read().splitlines()
                self.name = content[0]
            for line in content[1:]:
                if ":" not in line:
                    continue
                number, name = line.split(":")
                self.roster[number] = name
        except FileNotFoundError as e:
            pass
