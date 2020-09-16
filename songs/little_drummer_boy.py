class NewDrumSong():

    def __init__(self, win):
        self.win = win

    def startsong(self):
        print("Little button was clicked")
        self.win.updatelabel2("You clicked: Little Drummer Boy")