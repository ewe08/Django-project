# Django-project

## To Do

#### Для запуска проекта в dev режиме:

(Если у вас linux/macOS, то комманды `python` и `pip` меняются на `python3` и `pip3` соответсвенно)

1. Убедитесь, что на компьютере установлены python и git
2. Заходим в терминал и переходим в папку, куда должен загрузится проект
3. `git clone https://github.com/ewe08/Django-project`
4. `cd Django-project`
5. `python -m venv venv`
6. `venv/Scripts/activate.bat`/`venv/Scripts/activate.ps1` <br> Если
   linux/macOS: `source 'venv/Scripts/activate'`
7. `pip install -r requirements.txt`
8. `cd scrum_board`
9. Создаём файл .env в папке scrum_board (Необходимые поля находятся ниже)
10. `python manage.py migrate`
11. `python manage.py runserver`
12. ~~Profit!~~

#### Необходимые поля:

- SECRET_KEY=(Никак на должно попасть в публичный доступ)
- DEBUG=True
- ALLOWED_HOSTS='*'
- INTERNAL_IPS=['127.0.0.1', 'localhost']
- DEFAULT_FROM_EMAIL='scrum_board@support.com'

#### Использованные технологии:

- Python
- Django
- Bootstrap

#### Разработчики
- [ewe08](https://github.com/ewe08)
- [Sus-arch](https://github.com/Sus-arch)
- [Sergey207](https://github.com/Sergey207)
