from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.clock import Clock

#parent widget!!
class DifficultyScreen(Widget):
    def update(self, dt):
        pass
    def CheckClick(self, num):
        pass

class DifficultyScreen(Widget):

    def update(self, dt):
        pass

class HockeyGame(Widget):
    pass

class HockeyApp(App):
    def build(self):
        Game= HockeyGame()
<<<<<<< HEAD
        #Clock.schedule_interval(Game.update, 1.0 / 60.0)
        #return DifficultyScreen()
        return Game
    
=======
        return Game
        #Clock.schedule_interval(Game.update, 1.0 / 60.0)
        #return DifficultyScreen()

>>>>>>> main
if __name__ == '__main__':
    HockeyApp().run()