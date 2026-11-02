
from kivymd.app import MDApp

from kivy_garden.mapview import MapView


class MapViewApp(MDApp):

    def build(self):
        mapview = MapView(zoom=20, lat=48.73949640938191, lon=30.255105752307085,)
        return mapview

MapViewApp().run()        

