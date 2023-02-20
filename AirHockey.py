from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.clock import Clock


class HockeyGame(Widget):

    def update(self, dt):
        
        def on_touch_move(self, touch):
            if touch.y < self.hieght/2:
                print("High")
            elif touch.y > self.hieght/2:
                print("Low")
        pass


class HockeyApp(App):
    def build(self):
        Game= HockeyGame()
        Clock.schedule_interval(Game.update, 1.0 / 60.0)
        return Game

if __name__ == '__main__':
    HockeyApp().run()