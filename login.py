import tkinter as tk


ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("Login")
user = tk.StringVar()
passw = tk.StringVar()



usuario = tk.Label(ventana,text = "Usuario", font = ("Helvetica",15))
caja_usuario = tk.Entry(ventana, textvar = user, font = ("Helvetica",18),width = "14")
caja_password =tk.Entry(ventana, textvar = passw, font = ("Helvetica",18),width = "14")
password = tk.Label(ventana,text = "Contraseña", font = ("Helvetica",15))
login_button = tk.Button(ventana,text = "Ingresar",font = ("Helvetica",15))
newacc_button = tk.Button(ventana,text = "Ingresar",font = ("Helvetica",15))

usuario.pack()
usuario.place(x = 100, y = 100)
caja_usuario.pack()
caja_usuario.place(x=250, y = 95)
password.pack()
password.place(x = 100, y = 150)
caja_password.pack()
caja_password.place(x = 250, y = 145)
login_button.pack()
login_button.place(x = 400,y = 400)
newacc_button.place(x= 300, y = 300)
ventana.mainloop()