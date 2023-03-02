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
    
    def update(self, dt):
        pass
    

class HockeyApp(App):
    def build(self):
        Game = HockeyGame()
        Menu = DifficultyScreen()
        #Clock.schedule_interval(Game.update, 1.0 / 60.0)
        #HockeyRoot.add_widget(Menu)
        #HockeyRoot.add_widget(Game)
        return Game
    
if __name__ == '__main__':
    HockeyApp().run()