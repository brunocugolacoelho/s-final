
import kivy
import matplotlib.pyplot as plt
import numpy as np
from kivy.lang.builder import Builder
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import socket, time, matplotlib.pyplot as plt, numpy as np

HOST = "localhost"  # The server's hostname or IP address
PORT_spa = 6789  # The port used by the server
PORT_spb = 6790  # The port used by the server
PORT_MF_Vn = 20002 # The port used by the server
va_n = 0
va_n_vect = []
va_n_tmp = []
x = []
cont_x = 0
plot_window = 99
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_spb:
    s_spb.connect((HOST, PORT_MF_Vn))
    
    plt.ion()
    while(1):
        s_spb.sendall(b"(request \n \
               :sender  ( agent-identifier :name spb@Microrede-UFJF:1099 ) \n \
                   :RECEIVER  (SET ( agent-identifier :name MF_Vn@Microrede-UFJF:1099 ) ) \n \
                       :content '23/08/2022_10:41:48.40601,4118,20000,0,0'  )\r\n")
   
        data2 = s_spb.recv(4096)
        data2_decd = data2.decode()
        # data2_spl = data2_decd.split(":content  ")
        # data2_cnt = data2_spl[1].split('"')
        # data2_cnt_f = data2_cnt[1].split(";")
        print(f"recebi content SPB -> {data2_decd!r}")
        # print(f"recebi split SPB -> {data2_cnt_f[0]!r}")
        
        
                   
            
        t = 0
        # if len(va_n_vect) > plot_window:
        #     va_n_vect.append(int(data2_cnt_f[0]))
        #     va_n_vect.pop(0)
                
                
        # else:
        #     va_n_vect.append(int(data2_cnt_f[0]))
        #     x.append(cont_x)
        #     cont_x += 1
        # # fig, ax = plt.subplots()
        # plt.plot(x, va_n_vect, linewidth=2.0)
        # plt.draw()
        # plt.pause(0.0001)
        # plt.clf()
        # ax.plot(x, va_n_vect, linewidth=2.0)
        # ax.set(xlim=(0,plot_window)   , xticks=np.arange(1,plot_window), 
        #        ylim=(0,40000), yticks=np.arange(1,40000))
        
        time.sleep(0.166)

class Matty(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        box = self.ids.box
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))

    def save_it(self):
        pass

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        # self.theme_cls.primary_palette = 'Bluegray'
        Builder.load_file('Matty.kv')
        return Matty()
    
MainApp().run()
