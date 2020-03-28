import tkinter as tk
import tkinter.ttk as ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Practica GUI senseHat")

        self.labelframe1=ttk.LabelFrame(self.ventana1, text="Monotorización")        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)        

        self.label1=tk.Label(self.labelframe1, text="Control")
        self.label1.grid(column=0, row=2)
        self.boton1=tk.Button(self.labelframe1, text="PARAR", command=self.convertir)
        self.boton1.grid(column=1, row=2)
        self.label2=tk.Label(self.labelframe1, text="Periodo:")
        self.label2.grid(column=1, row=3)
        
        self.label1=tk.Label(self.labelframe1, text="Medidas")
        self.label1.grid(column=0, row=6)
        
        self.dato=tk.StringVar(value="0.0")        
        self.entryCantidad=tk.Entry(self.labelframe1, width=10, textvariable=self.dato)
        self.entryCantidad.grid(column=1, row=7)

        self.seleccion=tk.IntVar()
        self.seleccion.set(2)


        self.labelframe2=ttk.LabelFrame(self.ventana1, text="Medidas")        
        self.labelframe2.grid(column=0, row=1, padx=5, pady=10)        


        self.radio1=tk.Radiobutton(self.labelframe1,text="Temperatura", variable=self.seleccion, value=1)
        self.radio1.grid(column=1, row=9)
        self.radio2=tk.Radiobutton(self.labelframe1,text="Preción", variable=self.seleccion, value=2)
        self.radio2.grid(column=2, row=9)
        self.radio3=tk.Radiobutton(self.labelframe1,text="Humedad", variable=self.seleccion, value=3)
        self.radio3.grid(column=3, row=9)

        self.labelframe3=ttk.LabelFrame(self.ventana1, text="Historico")        
        self.labelframe3.grid(column=0, row=2, padx=5, pady=10, sticky="WE")        

        self.labelResKelvin1=tk.Label(self.labelframe3, text="Num")
        self.labelResKelvin1.grid(column=0, row=8)

        self.labelResKelvin2=tk.Label(self.labelframe3, )
        self.labelResKelvin2.grid(column=1, row=8)

        self.labelResCelsius1=tk.Label(self.labelframe3, text="Valor")
        self.labelResCelsius1.grid(column=10, row=8)

        self.labelResCelsius2=tk.Label(self.labelframe3, )
        self.labelResCelsius2.grid(column=1, row=8)

        self.labelResFahrenheit1=tk.Label(self.labelframe3, text="Fecha/hora")
        self.labelResFahrenheit1.grid(column=20, row=8)

        self.labelResFahrenheit2=tk.Label(self.labelframe3, )
        self.labelResFahrenheit2.grid(column=1, row=8)

        self.labelResFahrenheit1=tk.Label(self.labelframe3, text="Tipo")
        self.labelResFahrenheit1.grid(column=30, row=8)

        self.labelResFahrenheit2=tk.Label(self.labelframe3, )
        self.labelResFahrenheit2.grid(column=1, row=8)

        self.ventana1.mainloop()

    def convertir(self):
        if self.seleccion.get()==1:
            self.convertir_desde_kelvin()        
        pass        


aplicacion1=Aplicacion()