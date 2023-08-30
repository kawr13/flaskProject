from flask import Flask, render_template, url_for, request, redirect
from markupsafe import escape


app = Flask(__name__)

CATEGORY_LIST = [
    {
        'id': 0,
        'id_button': 'btn-all',
        'title': 'техника',
    },
    {
        'id': 1,
        'id_button': 'btn-tech',
        'title': 'техника',
    },
    {
        'id_button': 'btn-bags',
        'title': 'сумки',
    },
]


NEWS_LIST = [
    {
        'id': 1,
        'title': 'Смартфон "TechMaster X1"',
        'content': 'Новейший смартфон "TechMaster X1" с высококачественным дисплеем, мощным процессором и камерой высокого разрешения. Отличное сочетание стиля и функциональности.',
        'image': 'static/assets/img/image.jpg'
    },
    {
        'id': 1,
        'title': 'Ноутбук "EcoBook Pro"',
        'content': 'Ультратонкий ноутбук "EcoBook Pro" с длительным временем работы батареи и высокой производительностью. Идеальный выбор для работы и развлечений в движении.',
        'image': 'static/assets/img/1_8_.png'
    },
    {
        'id': 1,
        'title': 'Кофемашина "CaffeineJoy"',
        'content': 'Приготовьте свой идеальный напиток с кофемашиной "CaffeineJoy". Большой выбор напитков и настраиваемых параметров для настоящих кофеманов.',
        'image': 'static/assets/img/c742446d28b8288cbc181000717e310d.jpg'
    },
    {
        'id': 1,
        'title': 'Спортивные наушники "BeatPulse"',
        'content': 'Откройте для себя новый уровень звука с наушниками "BeatPulse". Они обеспечивают отличное качество звука и плотную посадку для комфорта во время тренировок.',
        'image': 'static/assets/img/1-23.jpg'
    },
    {
        'id': 1,
        'title': 'Портативная колонка "SoundWave Mini"',
        'content': 'Взрывная звуковая мощь в миниатюрном корпусе – это портативная колонка "SoundWave Mini". Водонепроницаемый дизайн и долгое время работы делают ее идеальным спутником для любых мероприятий.',
        'image': 'static/assets/img/jbl1-photoroom.png-photoroom.png'
    },
    {
        'id': 1,
        'title': 'Умные часы "TimeMaster Plus"',
        'content': 'Следите за временем и своими достижениями с умными часами "TimeMaster Plus". Они отслеживают вашу активность, пульс и даже погоду.',
        'image': 'static/assets/img/8e96495ce827c1dd2ed079e7f305c200.jpg'
    },
    {
        'id': 1,
        'title': 'Фитнес-трекер "ActiveLife Pro"',
        'content': 'Оставайтесь в форме с фитнес-трекером "ActiveLife Pro". Он отслеживает ваши шаги, калории, сон и многое другое, помогая поддерживать здоровый образ жизни.',
        'image': 'static/assets/img/z28xjx8kccymfy5mu8nbwvpc708ti12m.png'
    },
    {
        'id': 1,
        'title': 'Камера "PixelShot 4K"',
        'content': 'Захватывайте моменты в высоком разрешении с камерой "PixelShot 4K". Она подходит для фотографий и видеозаписей, обеспечивая отличное качество изображения.',
        'image': 'static/assets/img/07.jpg'
    },
    {
        'id': 2,
        'title': 'Портфель "BusinessElite"',
        'content': 'Профессиональный портфель "BusinessElite" для тех, кто ценит стиль и функциональность. Множество отделений и вместительность делают его идеальным для рабочих встреч и поездок.',
        'image': 'static/assets/img/Без названия (2).jfif'
    },
    {
        'id': 1,
        'title': 'Планшет "InfinityTab Pro"',
        'content': 'Наслаждайтесь яркими изображениями и высокой производительностью с планшетом "InfinityTab Pro". Он подходит для работы, развлечений и обучения.',
        'image': 'static/assets/img/Без названия (1).jfif'
    },
]





@app.route('/', methods=['GET', 'POST'])
def index():
    pages = []
    page = 1  # Инициализация переменной page
    slicer = NEWS_LIST[0:5]
    for i in range(1, (len(NEWS_LIST) // 5) + 1):
        pages.append(str(i))
    if request.method == 'POST':
        num1 = request.form.get('page')
        page = int(num1)  # Обновление значения page
        slicer = NEWS_LIST[5 * (int(num1) - 1): 5 * int(num1)]
        context = {
            'news_list': slicer,
            'pages': pages,
            'page': page  # Передача значения page в контекст
        }
        return render_template('index.html', **context)
    context = {
        'news_list': slicer,
        'pages': pages,
        'page': page  # Передача значения page в контекст
    }
    return render_template(escape('index.html'), **context)




@app.route('/about/')
def about():
    return render_template(escape('about.html'))


@app.route('/contacts/')
def contacts():
    personals = [
        {'title': 'Коммерческий директор',
         'content': 'Иванов Иван Иванович',
         'image': 'static/assets/img/kommercheskij-direktor-1-640x427.jpg'},
        {'title': 'Лучший продавец',
         'content': 'Продаван Продавач Продажевич',
         'image': 'static/assets/img/_.jpg'},
        {'title': 'Кофемашина Кофемоящая',
         'content': 'Баба Глаша',
         'image': 'static/assets/img/a_69bf3e22.jpg'},
    ]
    return render_template(escape('contacts.html'), personals=personals)



@app.route('/news/')
def news():
    news_lists = [
        {'title': 'Новость 1', 'content': 'Краткое описание новости 1'},
        {'title': 'Новость 2', 'content': 'Краткое описание новости 2'},
    ]
    return render_template(escape('news.html'), news_lists=news_lists)



@app.route('/catalog/', methods=['GET', 'POST'])
def catalog_get():
    if request.method == 'POST':
        name = request.form.get('category')
        return redirect(url_for('catalog_get', category=name))
    context = {
        'new_list': NEWS_LIST,
        'catalog_url': url_for('catalog_get'),
        'tech_url': url_for('tech'),
        'bags_url': url_for('bags'),
    }
    return render_template('catalog.html', **context)



@app.route('/catalog/tech/', methods=['GET', 'POST'])
def tech():
    lst = []
    for prod in NEWS_LIST:
        if prod['id'] == 1:
            lst.append(prod)
        else:
            continue
    context = {
        'product': lst,
        'catalog_url': url_for('catalog_get'),  # Генерация URL для маршрута catalog
        'tech_url': url_for('tech'),  # Генерация URL для маршрута tech
    }
    return render_template('category.html', **context, name='tech')

#
@app.route('/catalog/bags/', methods=['GET', 'POST'])
def bags():
    lst = []
    for prod in NEWS_LIST:
        if prod['id'] == 2:
            lst.append(prod)
    context = {
        'product': lst,
        'catalog_url': url_for('catalog_get'),  # Генерация URL для маршрута catalog
        'bags_url': url_for('bags'),  # Генерация URL для маршрута tech
    }
    return render_template('category.html', **context, name='bags')



if __name__ == '__main__':
    app.run()
