import tkinter

main_window = tkinter.Tk()

label1 = tkinter.Label(main_window, text='rafi')
label2 = tkinter.Label(main_window, text='Cahya')

tombol1 = tkinter.Button(main_window, text='butt1')
tombol2 = tkinter.Button(main_window, text='butt2')

# method positioning
label1.pack()
label2.pack()
tombol1.pack()
tombol2.pack()

# method show GUI
main_window.mainloop()
