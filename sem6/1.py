import tkinter as tk

def push(a, sv):
    old_sv = sv.get()
    new_sv = old_sv + a
    sv.set(new_sv)

def eq(sv1):
    res = str(eval(sv1.get()))
    sv1.set(res)

def cl(sv2):
    sv2.set('')

def main():
    gui = tk.Tk()
    gui.title('Калькулятор целых чисел')
    gui.geometry('400x400')

    strvar = tk.StringVar()
    field = tk.Entry(gui, textvariable=strvar)
    field.grid(row=0, columnspan=6, sticky = 'NSEW')
    for j1 in range(6):
        gui.columnconfigure(j1, weight=1)
        gui.rowconfigure(j1, weight=1)

    Buttons = [tk.Button(gui, text=f'{i}', command = lambda x=i: push(str(x), strvar)) for i in range(1,10)]
    for i1 in range(len(Buttons)):
        Buttons[i1].grid(row=(i1)//3+1, column=((i1)%3)*2, columnspan=2, sticky='NSEW')

    Oper = ['+', '-', '*', '//', '%']
    But_oper = [tk.Button(gui, text=Oper[i2], command = lambda x2=i2: push(Oper[x2], strvar)) for i2 in range(5)]
    for i3 in range(len(But_oper)):
        But_oper[i3].grid(row=4, column=i3, sticky='NSEW')

    Button_eq = tk.Button(gui, text='=', command = lambda: eq(strvar))
    Button_eq.grid(row=4, column=5, sticky='NSEW')

    Button_clear = tk.Button(gui, text='C', command = lambda: cl(strvar))
    Button_clear.grid(row=5, column=2, columnspan=2, sticky='NSEW')

    gui.mainloop()
if __name__ == '__main__':
    main()
