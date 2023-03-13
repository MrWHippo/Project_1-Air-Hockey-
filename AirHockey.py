from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty, ListProperty, ObjectProperty
from kivy.vector import Vector

class DifficultyScreen(Widget):
    def CheckClick(self, num):
        print(num)
        self.parent.changescreen(num)

    
class HockeyGame(Widget):
    hockey_puck = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def serve_puck(self, vel=(4, 0)):
        self.puck.center = self.center
        self.puck.velocity = vel
    
    def update(self, dt):
        self.player1.Color = (0,0,1,1) 
        self.player2.Color = (1,0,0,1)

        self.puck.move()
        #collisions
        if self.puck.x < 0 or self.puck.x > self.width:
            self.puck.velocity_x *= -1
            print(self.puck.velocity_x)
        
        if self.puck.y < 0 or self.puck.y > self.height:
            self.puck.velocity_y *= -1


class Players(Widget):
    score = NumericProperty(0)
    Color = ListProperty((1,1,1,1))
    
class HockeyPuck(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    Color = ListProperty((1, 1, 1, 1))

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class HockeyRoot(FloatLayout):
    def __init__(self, **kwargs):
        super(HockeyRoot, self).__init__(**kwargs)
        self.add_widget(DifficultyScreen())
    
    def changescreen(self, num):
        self.clear_widgets()
        self.add_widget(HockeyGame())
        #self.add_widget(Players())
        #self.add_widget(HockeyPuck())
        Game = HockeyGame()
        Clock.schedule_interval(Game.update, 1.0 / 60.0)
        return Game


class HockeyApp(App):
    def build(self):
        Game = HockeyGame()
        Window = HockeyRoot()
        Clock.schedule_interval(Game.update, 1.0 / 60.0)
        return Window
    
if __name__ == '__main__':
    HockeyApp().run()