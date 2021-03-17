import random

shows = {'Секретные материалы': 'фантастика', 'Ведьмак': 'фэнтази', 'Клан Сопрано': 'криминал', '24': 'драма',
         'Черное зеркало': 'фантастика', 'Во все тяжкие': 'криминал', 'Игра престолов': 'фэнтази',
         'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
ratings = {'Секретные материалы': 0.9, 'Ведьмак': 0.95, 'Клан Сопрано': 0.8, '24': 0.75, 'Черное зеркало': 0.98,
           'Во все тяжкие': 0.85, 'Игра престолов': 0.87, 'Карточный домик': 0.82, 'Рик и Морти': 1}
# узнаём жанр у пользователя
chose = str(input('Уажите жанр для исключения из поиска\n:')).strip().lower()
top = float(input('Уажите минимальный приемливый для вас рейтинг\n:'))
# создаём список для сериалов подходящих по жанру
search = shows.items()
# создаём список для рейтингов
outputs = []
# узнаём какие сериалы не попадают в исключенный жанр, полученный от пользователя
for show, genre in search:
    if genre != chose:
        # наполняем список для рейтинга сериалов
        outputs.append(show)
        random.shuffle(outputs)
# узнаём рейтинг сериалов из списка и выводим результаты для каждого из них в отдельности.
series = list(set(outputs))
while len(series) > 0:
    serial = str(series[0])
    print(type(serial), ' ', type(ratings.keys()), ' ', type(ratings[serial]), ' ', type(top), ' ', type(shows.keys()),
          ' ')
    result = serial
    for result in ratings.keys() and ratings[result] >= top and result in shows.keys():
        print(type(result), ' ', type(ratings.keys()), ' ', type(ratings[result]), ' ', type(top), ' ',
              type(shows.keys()), ' ')
        print(f'Исходя из Ваших предпочтений, мы рекомендуем вам к просмотру сериал "{result}" в жанре'
              f' {shows[result]}.\nНа Metacritic рейтинг сериала составляет: {ratings[result] * 10}/ 10.')
        series.remove(result)
        answer = str(input('Если не хотите останавливаться на этом сериале введите "Далее"\n:')).strip().lower()
        while answer != 'далее':
            print(f'Вы остановилиси свой выбор на сериале {result} в жанре {shows[result]} рейтинг на '
                  f'Metacritic {ratings[result] * 10} / 10.')
            break
        if len(series) == 0 and answer == 'далее':
            print('Сожалем, но нам нечего Вам предложть.')
        if answer == 'далее':
            continue
