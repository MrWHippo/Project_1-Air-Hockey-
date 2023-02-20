from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.clock import Clock




class HockeyGame(Widget):
    pass


class HockeyApp(App):
    def build(self):
        return HockeyGame()

if __name__ == '__main__':
    HockeyApp().run()