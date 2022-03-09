from tkinter import *
from tkinter import ttk, messagebox
import xml.etree.ElementTree as ET

class AppXmlInPy(ttk.Frame):

    def __init__(self, main_window):#Constructor
        "Se crea la pantalla de visualizacion"
        super().__init__(main_window)
        main_window.title("XML viewer")
        main_window.geometry("500x350")
        self.treeview = ttk.Treeview(self)
        "invocamos la raiz con el ET parse y el getroot()"
        self.tree = ET.parse('./xml/materias.xml')
        self.raiz = self.tree.getroot()
        "esa raiz se la pasamo a la funcion que dibujara el arbol"
        self.insert_treeview(self.raiz)
        "opciones para desplegar el arbol"
        self.treeview.pack(fill = BOTH, expand = True)
        self.pack(fill = BOTH, expand = True)
    
    def insert_treeview(self, raiz, parent=""):
        "recorremos la raiz"
        for child in raiz:
            node_name = child.tag
            item = self.treeview.insert(parent, END, None, text=node_name)
            if len(child) > 0:
                "si tiene hijos volvemos a invocar"
                self.insert_treeview(child, parent=item)
            else:
                "si no tiene hijos solo insertamos pero con el text"
                if(child.text != None):
                    self.treeview.insert(item, END, None, text=child.text)

root = Tk()
app = AppXmlInPy(root)
app.mainloop()