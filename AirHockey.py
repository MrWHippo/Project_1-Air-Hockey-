from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty, ListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.core.window import Window

class DifficultyScreen(Widget):
    def CheckClick(self, num):
        print(num)
        self.parent.changescreen(num)

    
class HockeyGame(Widget):
    hockey_puck = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def init(self):
        self.keyboard = Window.request_keyboard(self.keyboardclosed, self)

        self.keyboard.bind(on_key_down = self.on_keyboard_down)
        self.keyboard.bind(on_key_up = self.on_keyboard_up)

        self.player1_up = False
        self.player1_down = False
        self.player1_left = False
        self.player1_right = False

        self.player1.isplayer1 = True
        self.player2.isplayer1 = False
        

    def serve_puck(self, vel=(4, 0)):
        self.puck.center = self.center
        self.puck.velocity = vel
    
    def update(self, dt):
        self.player1.Color = (1,0,0,1) 
        self.player2.Color = (0,0,1,1)

        self.puck.move()
        self.player1.moveplayer()
        self.player2.moveplayer()

        #
        #self.puck.reset()

        #collisions
        if self.puck.x < 0 or self.puck.x > self.width:
            self.puck.velocity_x *= -1
            print(self.puck.velocity_x)
        
        if self.puck.y < 0 or self.puck.y > self.height:
            self.puck.velocity_y *= -1

        #puck collisions
        player1difference = self.vector_between(self.player1)
        player2difference = self.vector_between(self.player2)

        if player1difference <= (self.player2.width/2)**2 + (self.puck.width/2)**2:
            puckvector = Vector(self.puck.center[0], self.puck.center[1])
            player1vector = Vector(self.player1.center[0], self.player1.center[1])
            self.puck.velocity[0] *= -1.1
            self.puck.velocity[1] *= -1.1
            if self.puck.velocity[0] == 0 and self.puck.velocity[1] == 0:
                self.puck.velocity[1] = 3
                if self.puck.center[0] > self.player1.center[0]:
                    self.puck.velocity[0] = (-self.puck.center[0]+self.player1.center[0])/2
                else:
                    self.puck.velocity[0] = (self.puck.center[0]-self.player1.center[0])/2
        
        if player2difference <= (self.player2.width/2)**2 + (self.puck.width/2)**2:
            puckvector = Vector(self.puck.center[0], self.puck.center[1])
            player2vector = Vector(self.player2.center[0], self.player2.center[1])
            self.puck.velocity[0] *= -1.1
            self.puck.velocity[1] *= -1.1
            if self.puck.velocity[0] == 0 and self.puck.velocity[1] == 0:
                self.puck.velocity[1] = 3
                if self.puck.center[0] > self.player1.center[0]:
                    self.puck.velocity[0] = (-self.puck.center[0]+self.player2.center[0])/15
                else:
                    self.puck.velocity[0] = (self.puck.center[0]-self.player2.center[0])/15

    
    def vector_between(self, player):
        x = player.center[0] - self.puck.center[0]
        y = player.center[1] - self.puck.center[1]
        vector = x**2 + y**2
        return vector

    def keyboardclosed(self):
        print("Keyboard Lost")
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
    
    def on_keyboard_up(self, keyboard, keycode):
        if keycode[1] == "w":
            self.player1_up = False

        if keycode[1] == "s":
            self.player1_down = False

        if keycode[1] == "a":
            self.player1_left = False

        if keycode[1] == "d":
            self.player1_right = False

        return True
    
    def on_keyboard_down(self, keyboard, keycode, text, modifieds):
        if keycode[1] == "w":
            self.player1_up = True

        if keycode[1] == "s":
            self.player1_down = True

        if keycode[1] == "a":
            self.player1_left = True

        if keycode[1] == "d":
            self.player1_right = True

        return True
    
    def giveinputstatus(self):
        return self.player1_down, self.player1_up, self.player1_left, self.player1_right

class Players(Widget):
    score = NumericProperty(0)
    Color = ListProperty((1,1,1,1))

    def moveplayer(self):
        self.getinputstatus()
        if self.isplayer1 == True:
            if self.player1_up == True:
                if self.y+3 < self.parent.height/2 - self.height:
                    self.y += 2

            if self.player1_down == True:
                if self.y-3 > 0:
                    self.y -= 2

            if self.player1_left == True:
                if self.x-3 > 0:
                    self.x -= 3

            if self.player1_right == True:
                if self.x+3 < self.parent.width - self.width:
                    self.x += 3
    
    def getinputstatus(self):
        self.player1_down, self.player1_up, self.player1_left, self.player1_right = self.parent.giveinputstatus()

class HockeyPuck(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    Color = ListProperty((1, 1, 1, 1))

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos
    
    def reset(self):
        self.pos = self.parent.width/2 - self.width/2 ,self.parent.height/2 - self.height/2

#class HockeyRoot(FloatLayout):
#    hockeygame = ObjectProperty(None)
#    DifficultyScreen = ObjectProperty(None)
#    def __init__(self, **kwargs):
#        super(HockeyRoot, self).__init__(**kwargs)
#        self.add_widget(DifficultyScreen())
#        self.changescreenbool = False
#    
#    def changescreen(self, num):
#        self.changescreenbool = True
#        # need to hide/ show widgets?
#        pass
#
#    def update(self, dt):
#        if self.changescreenbool == True:
#            self.hockeygame.update(dt)
#            pass
#        pass

class HockeyApp(App):
    def build(self):
        Game = HockeyGame()
        #Window = HockeyRoot()
        Game.init()
        Clock.schedule_interval(Game.update, 1.0 / 60.0)
        return Game
    
if __name__ == '__main__':
    HockeyApp().run()