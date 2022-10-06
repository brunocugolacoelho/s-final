from kivy.uix.boxlayout import BoxLayout
from popups import ModbusPopup, ScanPopup, RegPopup
from pyModbusTCP.client import ModbusClient
from kivy.core.window import Window
from threading import Thread
from time import sleep


class MainWidget(BoxLayout):
    """
    Widget principal da aplicação
    """
    _updateThread = None
    _updateWidgets = True
   
    def __init__(self, **kwargs):
        """
        construtor do widget principla
        """
        super().__init__()
        self._scan_time = kwargs.get('scan_time')
        self._scan_reg = kwargs.get('scan_reg')
        self._serverIP=kwargs.get('server_ip')
        self._serverPort = kwargs.get('server_port')
        self._modbusPopup = ModbusPopup(self._serverIP,self._serverPort)
        self._scanPopup = ScanPopup(self._scan_time)
        self._modbusClient = ModbusClient(host=self._serverIP, port=self._serverPort)
        self._regPopup = RegPopup(self._scan_reg)

    def startDataRead(self, ip, port):
        """
        método utilizado para a configuração do IP e porta MODBUS e inicia 
        thread para leitura e atualização da inteface grafica
        """

        self._serverIP = ip
        self._serverPort= port
        self._modbusClient.host = self._serverIP
        self._modbusClient.port = self._serverPort
        try:
            Window.set_system_cursor("wait")
            self._modbusClient.open()
            Window.set_system_cursor("arrow")
            if self._modbusClient.is_open():
                self._updateThread = Thread(target=self.updater)
                self._updateThread.start()
                self.ids.img_con.source='imgs/conectado.png'
                self._modbusPopup.dismiss()
            else:
                self._modbusPopup.setInfo("Falha na conexão com o servidor")
        except Exception as e:
            print("Erro: ",e.args)
    
    def updater(self):
        """
        Método que invoca as rotinas de leitura de dados, atualização da interface e inserção de dados no banco de dados
        """
        try:
            while self._updateWidgets:
                #ler os dados modbus
                #atualizar a interface
                #inserir os dados no banco de dados
                sleep(self._scan_time/1000)
        except Exception as e:
            self._modbusClient.close()
            print("Erro: ",e.args)