import tkinter as tk

def show(sv1, sv2):
    mass = int(sv1.get())
    height = int(sv2.get())/100

    window = tk.Tk()
    window.geometry('200x200')
    window.title('Результат расчёта')
    IMT = round(mass/height**2, 1)

    if IMT <= 16:
        verdict = 'Выраженный дефицит массы тела'
    elif IMT > 16 and IMT <= 18.5:
        verdict = 'Недостаточная (дефицит) масса тела'
    elif IMT > 18.5 and IMT <=25:
        verdict = 'Норма'
    elif IMT > 25 and IMT <=30:
        verdict = 'Избыточная масса тела (предожирение)'
    elif IMT > 30 and IMT <= 35:
        verdict = 'Ожирение 1 степени'
    elif IMT > 35 and IMT <= 40:
        verdict = 'Ожирение 2 степени'
    else:
        verdict = 'Ожирение 3 степени'
    label_res = tk.Label(window, text = f'Ваш ИМТ {IMT}\n{verdict}')
    label_res.pack()
    sv1.set('')
    sv2.set('')

def main():
    gui = tk.Tk()
    gui.geometry('400x200')
    gui.resizable(False, False)
    gui.title('Калькулятор индекса массы тела')
    for i in range(2):
        gui.columnconfigure(i, weight=1)
        gui.rowconfigure(0, weight=1)
    gui.rowconfigure(2, weight=6)

    strvar_m = tk.StringVar()
    m_f = tk.Entry(gui, textvariable = strvar_m)
    m_f.grid(row = 0, column = 0, sticky = 'nsew')
    label_m = tk.Label(gui, text = 'Введите массу (кг)')
    label_m.grid(row = 1, column = 0)

    strvar_h = tk.StringVar()
    h_f = tk.Entry(gui, textvariable = strvar_h)
    h_f.grid(row = 0, column = 1, sticky = 'nsew')
    label_h = tk.Label(gui, text = 'Введите рост (см)')
    label_h.grid(row = 1, column = 1)

    button = tk.Button(gui, text='Вывести результат', command=lambda: show(strvar_m, strvar_h))
    button.grid(row = 2, columnspan=2)
    
    tk.mainloop()
if __name__ == '__main__':
    main()
