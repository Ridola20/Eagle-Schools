import os
os.environ["KIVY_NO_ARGS"] = "1"
os.environ['KIVY_IMAGE'] = "pil,sdl2"
os.environ['PATH'] += ';' + os.path.expandvars('%AppData%\\Python\\share\\glew\\bin')
os.environ['PATH'] += ';' + os.path.expandvars('%AppData%\\Python\\share\\sdl2\\bin')


from kaki.app import App 
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.factory import Factory
from kivy.core.text import LabelBase

class MainApp(App, MDApp):    
    KV_FILES = [
        os.path.join(os.getcwd(), 'splash_screen.kv'),
    ]

    CLASSES = {
        "MainScreen": "mainscreen",
    }

    AUTORELOADER_PATHS = [(os.getcwd(), {"recursive": True})]

    def build_app(self):
        Window.size = [370, 750]

        self.trending_vid_source = "tt.mp4"

        return Factory.MainScreen()

# LabelBase.register(name='Lemonada', fn_regular='Lemonada-VariableFont_wght.ttf')

if __name__ == '__main__':
    MainApp().run()