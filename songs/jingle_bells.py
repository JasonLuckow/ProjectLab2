class NewJingleSong():

    def __init__(self, win):
        self.win = win

    def startsong(self, app):
        print("Jingle button was clicked")
        self.win.updatelabel2("You clicked: Jingle Bells")