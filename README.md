# CodePractice — учебный сайт с заданиями по Python

CodePractice — простой сайт на Flask с 20 учебными задачами по основам Python. Каждая задача содержит условие, входные данные, ожидаемый результат, подсказку и пример решения.

## Возможности
- 20 задач по Python;
- отдельная страница каждой задачи;
- подсказки и раскрывающиеся примеры решений;
- поиск по названию и условию;
- фильтр по уровню сложности;
- адаптивный дизайн для телефона и компьютера;
- страница 404 для неизвестного номера задания.

## Требования
- Python 3.10 или новее;
- pip;
- браузер.

## Запуск на macOS или Linux
Открой Terminal в папке проекта и выполни команды:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

Затем открой http://127.0.0.1:5000 в браузере. Чтобы остановить сервер, нажми `Control + C` в терминале.

## Запуск на Windows
```powershell
py -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python app.py
```

## Структура проекта
```text
CodePractice/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   ├── index.html
│   ├── task.html
│   └── 404.html
└── static/
    └── style.css
```

## Загрузка на GitHub
1. Создай на GitHub новый публичный репозиторий `CodePractice`. Не добавляй автоматически README, если README уже есть в этом проекте.
2. В терминале, открытом в папке проекта, выполни:

```bash
git init
git add .
git commit -m "Create CodePractice website"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/CodePractice.git
git push -u origin main
```

Замени `YOUR-USERNAME` на свой GitHub username. Если GitHub попросит авторизацию, следуй подсказкам браузера.

## Важно
Это учебный проект: примеры решений отображаются на сайте, но пользовательский Python-код в браузере не запускается и автоматически не проверяется. Не добавляй на публичный сервер запуск произвольного кода без отдельной безопасной изоляции.
