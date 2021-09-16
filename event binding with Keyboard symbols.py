from tkinter import*
root =Tk()
root.title('Keyboard Binding-Symbols')
root.iconbitmap('python_logo_icon.ico')
root.geometry("400x400")

def clicker(event):
    myLabel=Label(root,fg='red',font="Arial 16 bold",text="Pressed ---"+event.keysym+"--Key")
    myLabel.pack()
myButton=Button(root,font="Arial 16 bold",text="Click Button")
myButton.bind("<Key>",clicker)# Keyboard symbols
myButton.pack(pady=20)

root.mainloop()