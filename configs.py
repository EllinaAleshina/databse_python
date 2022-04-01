# -*- coding: utf-8 -*-
# pylint: disable=C0103

"""
Модуль, содержащий необходимые атрибуты
------------
Автор: Алёшина Эллина
"""
import os
path = os.path.abspath(os.path.join(os.getcwd(), '..', 'Data'))
path_to_csv = path + '/data_spotify.csv'
path_to_new_csv = path + '/new_data_spotify.csv'

width_window = 1200
height_window = 750

columns_eng = ['', "genre", "artist_name", "track_name",
            'popularity', 'acousticness', 'danceability',
             'energy', 'key',
            'loudness', 'mode', 'tempo']

columns_eng_1 = ['Выбрать', "genre",
            'popularity', 'acousticness', 'danceability',
             'energy', 'key', 'loudness', 'mode', 'tempo']

columns_eng_2 = ['Выбрать', 'popularity', 'acousticness', 'danceability',
                'energy', 'loudness', 'tempo']

columns_rus = ["Жанр", "Исполнитель", "Название трека",
            'Популярность', 'Акустичность', 'Танцевальность',
             'Энергия', 'Тональность',
            'Громкость', 'Лад', 'Темп']

columns_choose = ['Выбрать', "Жанр", "Исполнитель", "Название трека",
            'Популярность', 'Акустичность', 'Танцевальность',
             'Энергия', 'Тональность',
            'Громкость', 'Лад', 'Темп']


genres = ['Movie', 'R&B', 'A Capella', 'Alternative', 'Country', 'Dance',
          'Jazz', 'Comedy', 'Soul', 'Soundtrack']

graphics = ['Выбрать', 'Диаграмма рассеивания', 'Столбчатая диаграмма', 'Гистограмма', 'Диаграмма Бокса-Виксера']
