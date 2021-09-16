from tkinter import*
root =Tk()
root.title('Mouse Button Binding')
root.iconbitmap('python_logo_icon.ico')
root.geometry("400x400")
def clicker(event):
    myLabel=Label(root,fg='red',font="Arial 16 bold",text="You Pressed the Enter Key ")
    myLabel.pack()
myButton=Button(root,font="Arial 16 bold",text="Clicl Me")
#myButton.bind("<Button-1>",clicker)# Left Mouse Button
#myButton.bind("<Button-2>",clicker)# Middle Mouse Button
myButton.bind("<Return>",clicker)# Press Tab key then press Enter Button
myButton.pack(pady=20)

root.mainloop()
