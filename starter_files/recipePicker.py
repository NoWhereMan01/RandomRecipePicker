import tkinter as tk
from PIL import ImageTk


# initiallize app
root = tk.Tk()

#Esta blece el nombre de la ventana
root.title('Recipe Picker')

bg_color = '#3d6466'

def load_frame1():
        frame1.pack_propagate(False)
        #logo widget
        logo_img = ImageTk.PhotoImage(file="starter_files/assets/RRecipe_logo.png")
        logo_widget = tk.Label(frame1, image=logo_img, bg=bg_color)
        logo_widget.image = logo_img
        logo_widget.pack()

        tk.Label(frame1,
          text='listos para la receta random?',
          bg=bg_color,
          fg='white',
          font=('TkMenuFont', 14)
          ).pack()

        #boton widget

        tk.Button(
                 frame1,
                 text='BUSCAR',
                 font=('TkheadingFont', 20),
                 bg='#28393a',
                 fg='white',
                 cursor='hand2',
                 activebackground='#badee2',
                 activeforeground='black',
                 command=lambda:load_frame2()
                ).pack(pady=20)   

def load_frame2():
    print('holis carmelo')

#root.eval('tk::PlaceWindow . center') 
#centra la ventana en el centro de la pantalla

x= root.winfo_screenmmwidth() // 2
y= int(root.winfo_screenheight() * 0.05)
root.geometry('500x600+' + str(x) + '+' + str(y))

#crea un marco widgets
frame1 = tk.Frame(root, width=500, height=600, bg=bg_color)
frame2 = tk.Frame(root, bg=bg_color)
frame1.grid(row=0,column=0)


#frame1 wingets




load_frame1()

# run app
root.mainloop()