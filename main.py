from kivy.app import App
from mainwidget import MainWidget
from kivy.lang.builder import Builder


class MainApp(App):
    """
    classe do aplicativo
    """
    def build(self):
        """
        método que gera o aplicativo no widget principal
        """
        self._widget = MainWidget(scan_time=1000, server_ip="localhost", server_port=20002, scan_reg=50)
        return self._widget

if __name__=='__main__':
    Builder.load_string(open("MainWidget.kv", encoding="utf-8").read(),rulesonly=True)
    Builder.load_string(open("popups.kv", encoding="utf-8").read(),rulesonly=True)
    MainApp().run()