import tkinter as tk

def calc_col(col):
    col_a = format(255 - int(col[1:3], 16), 'x')
    if len(col_a) != 2:
        col_a = '0' + col_a
    col_b = format(255 - int(col[3:5], 16), 'x')
    if len(col_b) != 2:
        col_b = '0' + col_b
    col_c = format(255 - int(col[5:7], 16), 'x')
    if len(col_c) != 2:
        col_c = '0' + col_c
    return f'#{col_a}{col_b}{col_c}'

def butc(f, res, sv):
    col = sv.get()
    f.config(bg=col)
    res.config(text = calc_col(col), bg=calc_col(col))

def main():
    root = tk.Tk()
    root.title('Калькулятор цветов')
    root.geometry('400x200')
    root.columnconfigure(0, weight=1)
    for i in range(4):
        root.rowconfigure(i, weight=1)

    strvar = tk.StringVar()
    field = tk.Entry(root, textvariable=strvar)
    field.grid(row=0, sticky = 'NSEW')
    
    lab_expl = tk.Label(root, text='Введите цвет в формате #XXYYZZ')
    lab_expl.grid(row=1, sticky='N')

    lab_res = tk.Label(root, text='')
    lab_res.grid(row=3, sticky='NSEW')

    but = tk.Button(root, text='Показать сочетаемый цвет', command=lambda: butc(field, lab_res, strvar))
    but.grid(row=2, sticky='NSEW')

    root.mainloop()
if __name__ == '__main__':
    main()
