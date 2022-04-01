#-*- coding: utf-8 -*-
# pylint: disable=C0103
import sys
sys.path.append('../')
from tkinter import *
from configs import width_window, height_window, genres, graphics, columns_eng_1, columns_eng_2
import tkinter.ttk as ttk
from Library.functions import *

"""
    Главный модуль
    Его функционал: изображает все виджеты, таблицу с данными и заголовки на главном окне
    ------------------
    Автор: Солдатов Семен
"""



window = Tk()
window.title("Анализ треков из Spotify")

frame_sca = Frame(window, width=600, height=350)
frame_btn = Frame(window, width=600)
frame_listbox = Frame(window, width=600, height=100)
frame_plot = Frame(window, width=600, height=100)
frame_table = Frame(window, width=1200, height=300)

frame_sca.place(x=610, y=30)
frame_btn.place(x=610, y=290)
frame_listbox.place(x=100, y=240)
frame_plot.place(x=100, y=40)
frame_table.place(x=10, y=410)


genres_listbox = Listbox(frame_listbox, selectmode=EXTENDED)
selected = Listbox(frame_listbox, selectmode=EXTENDED)

for genre in genres:
    genres_listbox.insert(END, genre)

genres_listbox.pack(side=LEFT, padx=5)
next_btn = Button(frame_listbox, text=">>>", relief=RAISED, command=lambda: add_item(genres_listbox, selected))
next_btn.pack(side=LEFT, padx=5)
Button(frame_listbox, text="Удалить", relief=RAISED, command=lambda: delete_item(selected))\
    .pack(side=LEFT, padx=5)
selected.pack(side=LEFT, padx=5)

comboExample1 = ttk.Combobox(frame_plot, state="readonly",
                            values=graphics, font="Arial 10")
comboExample2 = ttk.Combobox(frame_plot, state="readonly",
                            values=columns_eng_1, font="Arial 10")
comboExample3 = ttk.Combobox(frame_plot, state="readonly",
                            values=columns_eng_2, font="Arial 10")
comboExample1.grid(column=0, row=1, columnspan=2, padx=15)
comboExample1.current(0)
comboExample2.grid(column=0, row=2, padx=15, pady=15)
comboExample2.current(0)
comboExample3.grid(column=1, row=2, padx=15, pady=15)
comboExample3.current(0)


Button(frame_plot, text="Построить", width=20, relief=RAISED,
       command=lambda: show_plot(comboExample1, comboExample2, comboExample3)).grid(column=0, row=3, columnspan=2)
labelTop = Label(frame_plot, text="Выберите тип графика", font="Arial 12")
labelTop.grid(column=0, row=0, columnspan=2)

plot_lbl = Label(window, text='Построение графиков')
plot_lbl.config(font=("Calibri Light", 18, "bold"))
plot_lbl.place(x=170, y=0)

listbox_lbl = Label(window, text='Отбор по жанрам')
listbox_lbl.config(font=("Calibri Light", 18, "bold"))
listbox_lbl.place(x=190, y=200)

gen_lbl1 = Label(window, text='Отбор колличественных значений')
gen_lbl1.config(font=("Calibri Light", 18, "bold"))
gen_lbl1.place(x=700, y=0)

empty_lbl = Label(frame_sca)
empty_lbl.grid(row=1, column=0)

var_pop_from = DoubleVar()
var_pop_to = DoubleVar()
var_dance_from = DoubleVar()
var_dance_to = DoubleVar()
var_temp_from = DoubleVar()
var_temp_to = DoubleVar()
var_energy_from = DoubleVar()
var_energy_to = DoubleVar()

lbl_popul = Label(frame_sca, text="Популярность:")
lbl_popul.grid(row=1, column=0, padx=3)
lbl1_from = Label(frame_sca, text="от")
lbl1_from.grid(row=1, column=1, padx=3)
sca_popul_from = Scale(frame_sca, variable=var_pop_from, orient=HORIZONTAL,
                      length=160, from_=0, to=100, tickinterval=20, resolution=1)
sca_popul_from.grid(row=1, column=2, padx=3)

lbl1_to = Label(frame_sca, text="до")
lbl1_to.grid(row=1, column=3, padx=3)
sca_popul_to = Scale(frame_sca, variable=var_pop_to, orient=HORIZONTAL, length=160,
                    from_=0, to=100, tickinterval=20, resolution=1)
sca_popul_to.set(100)
sca_popul_to.grid(row=1, column=4, padx=3)

lbl_dance = Label(frame_sca, text="Танцевальность:")
lbl_dance.grid(row=2, column=0, padx=3)
lbl2_from = Label(frame_sca, text='от')
lbl2_from.grid(row=2, column=1, padx=3)
sca_dance_from = Scale(frame_sca, variable=var_dance_from, orient=HORIZONTAL, length=160,
             from_=0, to=1, tickinterval=0.2, resolution=0.05)
sca_dance_from.grid(row=2, column=2, padx=3)
lbl2_to = Label(frame_sca, text="до")
lbl2_to.grid(row=2, column=3, padx=3)
sca_dance_to = Scale(frame_sca, variable=var_dance_to, orient=HORIZONTAL, length=160,
             from_=0, to=1, tickinterval=0.2, resolution=0.05)
sca_dance_to.set(1)
sca_dance_to.grid(row=2, column=4, padx=3)

lbl_tempo = Label(frame_sca, text="Темп трека:")
lbl_tempo.grid(row=3, column=0, padx=3)
lbl3_from = Label(frame_sca, text='от')
lbl3_from.grid(row=3, column=1, padx=3)
sca_tempo_from = Scale(frame_sca, variable=var_temp_from, orient=HORIZONTAL, length=160,
                      from_=0, to=250, tickinterval=50, resolution=2)
sca_tempo_from.grid(row=3, column=2, padx=3)
lbl3_to = Label(frame_sca, text="до")
lbl3_to.grid(row=3, column=3, padx=3)
sca_tempo_to = Scale(frame_sca, variable=var_temp_to, orient=HORIZONTAL, length=160,
             from_=0, to=250, tickinterval=50, resolution=2)
sca_tempo_to.set(250)
sca_tempo_to.grid(row=3, column=4)


lbl_energy = Label(frame_sca, text="Энергичность:")
lbl_energy.grid(row=4, column=0, padx=3)

lbl4_from = Label(frame_sca, text='от')
lbl4_from.grid(row=4, column=1, padx=3)

sca_energy_from = Scale(frame_sca, variable=var_energy_from, orient=HORIZONTAL, length=160,
             from_=0, to=1, tickinterval=0.2, resolution=0.02)
sca_energy_from.grid(row=4, column=2, padx=3)

lbl4_to = Label(frame_sca, text="до")
lbl4_to.grid(row=4, column=3, padx=3)
sca_energy_to = Scale(frame_sca, variable=var_energy_to, orient=HORIZONTAL, length=160,
                    from_=0, to=1, tickinterval=0.2, resolution=0.02)
sca_energy_to.set(1)
sca_energy_to.grid(row=4, column=4, padx=3)


download_init_data_base = Button(frame_btn, text='Обновить данные',
                                 relief=RAISED, command=lambda: update_table(frame_table, var_pop_from,
                                var_pop_to, var_dance_from, var_dance_to, var_temp_from,
                                var_temp_to, var_energy_from, var_energy_to, selected))

download_init_data_base.grid(row=5, column=0, padx=10)
reload_data_base = Button(frame_btn, text='Скачать ', relief=RAISED,
                         command=lambda: download())
reload_data_base.grid(row=5, column=2, padx=10)

add_info = Button(frame_btn, text='Добавить трек', relief=RAISED, command=lambda: show_adding())
add_info.grid(row=5, column=3, padx=10)

del_track = Button(frame_btn, text='Удалить трек', relief=RAISED, command=lambda: delete_track())
del_track.grid(row=5, column=4, padx=10)

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width / 2) - (width_window / 2)
y = (screen_height / 2) - (height_window / 2) - 30
window.geometry("%dx%d+%d+%d" % (width_window, height_window, x, y))

window.resizable(False, False)


window.mainloop()
