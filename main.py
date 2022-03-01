from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform
from kivy.clock import Clock
from applayout import AppLayout

if platform == 'android':
    from jnius import autoclass
    from android.permissions import request_permissions, check_permission, \
        Permission
    from android import api_version
    from android.runnable import run_on_ui_thread
    from android import mActivity
    View = autoclass('android.view.View')

    @run_on_ui_thread
    def hide_landscape_status_bar(instance, width, height):
        # width,height gives false layout events, on pinch/spread 
        # so use Window.width and Window.height
        if Window.width > Window.height: 
            # Hide status bar
            option = View.SYSTEM_UI_FLAG_FULLSCREEN
        else:
            # Show status bar 
            option = View.SYSTEM_UI_FLAG_VISIBLE
        mActivity.getWindow().getDecorView().setSystemUiVisibility(option)
else:
    # Dispose of that nasty red dot, required for gestures4kivy.
    from kivy.config import Config 
    Config.set('input', 'mouse', 'mouse, disable_multitouch')

class MyApp(App):
    
    def build(self):
        self.started = False
        if platform == 'android':
            Window.bind(on_resize=hide_landscape_status_bar)
            request_permissions([Permission.CAMERA], self.connect_camera)

        self.layout = AppLayout()
        return self.layout

    def connect_camera(self,permissions = [],grants = []):
        if platform == 'android':
            permission = check_permission(Permission.CAMERA)
        else:
            permission = True
        if permission:
            self.layout.detect.connect_camera(enable_analyze_pixels = True)

    def on_start(self):
        Clock.schedule_once(self.connect_camera)

    def on_stop(self):
        self.layout.detect.disconnect_camera()

MyApp().run()

