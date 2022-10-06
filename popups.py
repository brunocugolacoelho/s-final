from kivy.uix.popup import Popup
from kivy.uix.label import Label

class ModbusPopup(Popup):
    """
    popup da config modbuss
    """
    _info_lb = None
    def __init__(self, server_ip, server_port, **Kwargs):
        """
        construtor da classe modbusspopup
        """
        super().__init__(**Kwargs)
        self.ids.txt_ip.text = str(server_ip)
        self.ids.txt_porta.text = str(server_port)

    def setInfo(self,message):
        self._info_lb = Label(text=message)
        self.ids.layout.add_widget(self._info_lb)

    def clearInfo(self):
        if self._info_lb is not None:
            self.ids.layout.remove_widget(self._info_lb)

class ScanPopup(Popup):
    """
    popup da config do temp de varredura
    """
    def __init__(self, scantime, **Kwargs):
        """
        construtor da classe scanPopup
        """
        super().__init__(**Kwargs)
        self.ids.txt_st.text = str(scantime)

class RegPopup(Popup):
    """
    popup da config do temp de varredura
    """
    def __init__(self, scantime, **Kwargs):
        """
        construtor da classe scanPopup
        """
        super().__init__(**Kwargs)
        self.ids.txt_st.text = str(scantime)