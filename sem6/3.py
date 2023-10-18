import pandas as pd
import random
from tkinter import *
from tkinter import ttk

films = pd.read_csv('imdb_top_250.csv')
film_genres_list = list(films['Genre'])
complex_genres = []
for fg in film_genres_list:
    genres = fg.split(' | ')
    if len(genres) > 1:
        for genre in genres:
            film_genres_list.append(genre)
        complex_genres.append(fg)
for genre in complex_genres:
    film_genres_list.remove(genre)

genres_list = list(set(film_genres_list))
films_dict = {f: list(g.split(' | ')) for f, g in zip(films['Title'], films['Genre'])}
dict_gf = dict()
for i in genres_list:
    dict_gf[i] = []
for j in films_dict:
    for i1 in genres_list:
        if i1 in films_dict[j]:
            dict_gf[i1].append(j)

def show(sv):
    win = Tk()
    win.title('Фильм')
    win.geometry('150x150')
    gen = sv.get()
    sv.set('')
    random_film = random.choice(dict_gf[gen])
    lab = ttk.Label(win, text=f'{random_film}')
    lab.pack(expand=True)

def main():
    gui = Tk()
    gui.geometry('400x400')
    gui.title('Фильмотека')
    gui.columnconfigure(0, weight=1)
    gui.rowconfigure(0, weight=2)
    gui.rowconfigure(1, weight=1)
    
    strvar = StringVar()
    combobox = ttk.Combobox(values=genres_list, textvariable = strvar)
    combobox.grid(row = 0)
    button = ttk.Button(gui, text = 'Вывести случайный фильм', command = lambda: show(strvar))
    button.grid(row = 1)

    gui.mainloop()
if __name__ == '__main__':
    main()
