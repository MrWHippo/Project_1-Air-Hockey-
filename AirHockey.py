from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.clock import Clock


class DifficultyScreen(Widget):

    def update(self, dt):
        pass

class HockeyGame(Widget):
    pass

class HockeyApp(App):
    def build(self):
        Game= HockeyGame()
        return Game
        #Clock.schedule_interval(Game.update, 1.0 / 60.0)
        #return DifficultyScreen()

if __name__ == '__main__':
    HockeyApp().run()