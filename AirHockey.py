from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock

class DifficultyScreen(Widget):
    def update(self, dt):
        pass
    def CheckClick(self, num):
        print(num)
        self.parent.changescreen(num)
        pass

class HockeyRoot(FloatLayout):
    def __init__(self, **kwargs):
        super(HockeyRoot, self).__init__(**kwargs)
        self.add_widget(DifficultyScreen())
    
    def changescreen(self, num):
        self.clear_widgets()
        self.add_widget(HockeyGame())
        self.add_widget(Players())
        self.add_widget(HockeyPuck())
    
    def update(self, dt):
        pass

class HockeyGame(Widget):
    def update(self, dt):
        pass

class Players(Widget):
    pass
    
class HockeyPuck(Widget):
    pass


class HockeyApp(App):
    def build(self):
        Game = HockeyRoot()
        Clock.schedule_interval(Game.update, 1.0 / 60.0)
        return Game
    
if __name__ == '__main__':
    HockeyApp().run()
