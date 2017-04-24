from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import  serial  as s
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
import time
if sys.version_info[0] < 3:
    import Tkinter as tk
    from Tkinter import *
else:
    import tkinter as tk
    from tkinter import *
    from tkinter import ttk, font
#---------End of imports

#----------Empieza la clase que alberga la Interfaz
class InterfazShield():
    def __init__(self):
        #------Atributos

        #Declarar Ventana
        self.raiz = Tk()
        self.raiz.resizable(0,0)
        self.raiz.title('Generador y lector')
        self.raiz.geometry("+350+50")
        self.fig = plt.Figure()
        self.fig1 = plt.Figure()

        #Declaracion de variables
        self.variable_voltaje = DoubleVar(value=0.0)
        self.variable_menu = IntVar()
        self.variable_senal = IntVar(value=1)
        self.canal=IntVar()
        self.aux = IntVar()
        self.auxi=IntVar()
        self.h=IntVar(value=0)
        self.xvalues = []
        self.yvalues = []
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.x = np.arange(0, 2*np.pi, 0.01)
        self.variable_canal = IntVar(value=0)
        self.ser = s.Serial('/dev/ttyACM0',9600)
        #Empieza las variables codigo del generador
        self.ax1 = self.fig1.add_subplot(1, 1, 1)
        self.ax1.set_ylim(-15,15)
        self.line1, = self.ax1.plot(self.xvalues, self.yvalues, 'g')

        #Fuentes
        self.helv50=font.Font(family="Helvetica",size=75)
        self.helv30=font.Font(family="Helvetica",size=30)

        #escritos(et_)
        self.et_titulo = "Generador y lector \n       ( voltajes )"
        self.et_menu1 = "Entrada"
        self.et_menu2 = "Salida"
        self.et_entrada1 = "Ingrese el voltaje deseado : "
        self.et_entrada2 = "Grafico del voltaje de entrada : "

        #Widgets
        self.cuerpo = ttk.Frame(self.raiz, borderwidth=2,relief="ridge",)
        self.titulo = ttk.Label(self.cuerpo, text=self.et_titulo,font=self.helv50,)
        self.cuerpo_menu_principal = ttk.Frame(self.raiz, borderwidth=2,relief="ridge")
        self.menu1 = Radiobutton(self.cuerpo_menu_principal,text=self.et_menu1,font=self.helv30,variable=self.variable_menu,value=1)
        self.menu2 = Radiobutton(self.cuerpo_menu_principal,text=self.et_menu2,font=self.helv30,variable=self.variable_menu,value=2)
        self.bmenu1 = Button(self.cuerpo_menu_principal,text="Seleccionar",command=self.comprobar)
        self.cuerpo_principal1 = ttk.Frame(self.raiz, borderwidth=2,relief="ridge")
        self.panel_principal2 = PanedWindow(self.cuerpo_principal1,width=690,height=400)
        self.panel_principal3 = PanedWindow(self.cuerpo_principal1,width=690,height=400)
        self.panel_principal1 = PanedWindow(self.cuerpo_principal1,width=690,height=400)
        self.logo = PhotoImage(file='dass.png')
        self.creditos_pn1 = ttk.Label(self.panel_principal1,font = self.helv30,text = "Creado por :\nDeimer Andres Morales\nJuan Camilo Montilla")
        self.logo_pn1 = ttk.Label(self.panel_principal1,image=self.logo)
        self.msnvoltaje = ttk.Label(self.panel_principal3,text=self.et_entrada1,font=self.helv30)
        self.entrada = ttk.Entry(self.panel_principal3,textvariable=self.variable_voltaje)
        self.submenu1 = LabelFrame(self.panel_principal3, text="Tipo de senal")
        self.subm1_opcion1 = Radiobutton(self.submenu1,text="Senoidal",padx = 20,variable=self.variable_senal,value=1)
        self.subm1_opcion2 = Radiobutton(self.submenu1,text="Cuadrada",padx= 20,variable=self.variable_senal,value=2)
        self.subm1_opcion3 = Radiobutton(self.submenu1,text="Triangular",padx=20,variable=self.variable_senal,value=3)
        self.bmenu2 = Button(self.panel_principal3,text="Aceptar",command=self.leer)
        self.bmenu3 = Button(self.panel_principal2,text="Aceptar",command=self.cambiar_canal)
        self.msnvoltaje2 = ttk.Label(self.panel_principal2,text=self.et_entrada2,font=self.helv30)
        self.canvas2 = FigureCanvasTkAgg(self.fig1,master=self.panel_principal2)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.panel_principal3)
        self.submenu2 = LabelFrame(self.panel_principal2, text="Canales")
        self.subm2_opcion1 = Radiobutton(self.submenu2,text="Canal 1",padx = 20,variable=self.variable_canal,value=1)
        self.subm2_opcion2 = Radiobutton(self.submenu2,text="Canal 2",padx= 20,variable=self.variable_canal,value=2)

        #propiedades Widgets
        self.cuerpo.grid(column=0,row=0)
        self.titulo.grid(column=0,row=0,columnspan=2,rowspan=2,sticky=W+E+N+S,padx=128,pady=20)
        self.cuerpo_menu_principal.grid(column=0,row=1,sticky="w")
        self.menu1.grid(sticky="W",columnspan=2,padx=100)
        self.menu2.grid(row=0,column=2)
        self.bmenu1.grid(row=0,column=3,padx=89)
        self.cuerpo_principal1.grid(column=0,row=2,sticky="w")
        self.panel_principal2.grid(column=0,row=0)
        self.panel_principal3.grid(column=0,row=0)
        self.panel_principal1.grid(column=0,row=0)
        self.creditos_pn1.place(x=200,y=139)
        self.logo_pn1.place(x=425,y=150)
        self.msnvoltaje.place(x=40,y=15)
        self.entrada.place(x=300,y=20,width=100)
        self.canvas.get_tk_widget().place(height=300,width=400,x=40,y=75)
        self.submenu1.place(width=150,height=100,x=480,y=75)
        self.subm1_opcion1.pack(anchor=W)
        self.subm1_opcion2.pack(anchor=W)
        self.subm1_opcion3.pack(anchor=W)
        self.msnvoltaje2.place(x=40,y=15)
        self.bmenu2.place(x=555,y=190)
        self.canvas2.get_tk_widget().place(height=300,width=400,x=40,y=75)
        self.submenu2.place(width=150,height=60,x=480,y=75)
        self.subm2_opcion1.pack(anchor=W)
        self.subm2_opcion2.pack(anchor=W)
        self.bmenu3.place(x=555,y=150)

        #termina el bucle de la interfaz y actualiza los datos de la grafica
        self.h=0
        self.ani_widget()
        self.ani_widget1()
        self.raiz.mainloop()

        #Metodos

    def comprobar(self):
        if  self.variable_menu.get()==1:

            self.auxi=1
            self.panel_principal2.lift()
        else:

            self.auxi=0
            self.panel_principal3.lift()


    def leer(self):

        if  self.variable_senal.get()==1:
            print("senoidal")
            self.fig.clear()
            self.ani_widget()

        elif    self.variable_senal.get()==2:
                print("cuadrada")
                self.fig.clear()

        elif    self.variable_senal.get()==3:
                print("triangular")
                self.fig.clear()


    def cambiar_canal(self):

        if  self.variable_canal.get()==1:
            self.canal=1

        else:
            self.canal=0


    def animate(self,i):
        if self.auxi==0:
            self.xdata=self.am*np.sin(self.x+i/10.0)
            self.ser.write(b'self.data')
            self.line.set_ydata(self.xdata)  # update the data
            return self.line,
        else:
            self.h=self.h+1
            print(self.h)

    def ani_widget(self):

        self.am=self.variable_voltaje.get()
        self.ax = self.fig.add_subplot(111)
        self.line, = self.ax.plot(self.x,self.am*np.sin(self.x))
        self.ani = animation.FuncAnimation(self.fig,self.animate,np.arange(1, 200), interval=25, blit=False)


    def animate1(self,a):
        self.ser.reset_input_buffer()
        if self.auxi==1:
            try:
                if  self.canal==1:
                    self.ser.write(b'6')
                elif    self.canal==0:
                        self.ser.write(b'7')
                self.data = self.ser.readline()
                self.yvalue = float(self.data)
                self.yvalue = (4.8*self.yvalue)-12
                self.yvalues.append(self.yvalue)
                self.xvalues.append(a)
                self.line1.set_data(self.xvalues, self.yvalues)
                self.ax1.set_xlim(0, a+1)
            except ValueError:
                pass
        else:
            pass
    def ani_widget1(self):

        self.ani1 = animation.FuncAnimation(self.fig1, self.animate1, interval=100, blit=False)
        self.canvas2.show()
        self.ser.reset_input_buffer()



#----------Finaliza la clase que alberga la Interfaz
if __name__ == '__main__':
   mi_interfaz = InterfazShield()
