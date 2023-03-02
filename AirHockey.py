from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock

class DifficultyScreen(Widget):
    def update(self, dt):
        pass
    def CheckClick(self, num):
        pass

class HockeyGame(Widget):

    def update(self, dt):
        pass

class HockeyRoot(FloatLayout):
    def __init__(self, **kwargs):
        super(HockeyRoot, self).__init__(**kwargs)
        self.add_widget(DifficultyScreen())
        #self.add_widget(HockeyGame())

    def update(self, dt):
        pass


class HockeyApp(App):
    def build(self):
        #Game = HockeyGame()
        #Menu = DifficultyScreen()
        #Clock.schedule_interval(Game.update, 1.0 / 60.0)
        Game = HockeyRoot()
        return Game
    
if __name__ == '__main__':
    HockeyApp().run()