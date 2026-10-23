from flask import Flask, render_template, abort, request

app = Flask(__name__)

TASKS = [
    (1, "Hello, World!", "Начальный", "Выведи на экран текст Hello, World!", "Входные данные не требуются.", "Hello, World!", "Используй функцию print().", 'print("Hello, World!")'),
    (2, "Сумма двух чисел", "Начальный", "Найди сумму чисел 5 и 7.", "Входные данные не требуются.", "12", "Оператор + складывает числа.", "a = 5\nb = 7\nprint(a + b)"),
    (3, "Чётное или нечётное", "Начальный", "Определи, является ли число 8 чётным. Выведи Even или Odd.", "n = 8", "Even", "Остаток от деления проверяется оператором %.", 'n = 8\nif n % 2 == 0:\n    print("Even")\nelse:\n    print("Odd")'),
    (4, "Квадрат числа", "Начальный", "Найди квадрат числа 6.", "Входные данные не требуются.", "36", "Используй оператор **.", "n = 6\nprint(n ** 2)"),
    (5, "Наибольшее число", "Начальный", "Найди наибольшее из чисел 12, 19 и 4.", "Входные данные не требуются.", "19", "В Python есть функция max().", "print(max(12, 19, 4))"),
    (6, "Длина строки", "Начальный", "Посчитай количество символов в строке Python.", "Входные данные не требуются.", "6", "Используй len().", 'word = "Python"\nprint(len(word))'),
    (7, "Переворот строки", "Начальный", "Выведи слово Python в обратном порядке.", "Входные данные не требуются.", "nohtyP", "Срез [::-1] разворачивает строку.", 'word = "Python"\nprint(word[::-1])'),
    (8, "Сумма списка", "Начальный", "Найди сумму элементов списка [1, 2, 3, 4].", "Входные данные не требуются.", "10", "Используй sum().", "numbers = [1, 2, 3, 4]\nprint(sum(numbers))"),
    (9, "Среднее арифметическое", "Начальный", "Найди среднее арифметическое чисел 10, 20 и 30.", "Входные данные не требуются.", "20.0", "Сложи числа и раздели на их количество.", "numbers = [10, 20, 30]\nprint(sum(numbers) / len(numbers))"),
    (10, "Сумма от 1 до 10", "Начальный", "Вычисли сумму целых чисел от 1 до 10 включительно.", "Входные данные не требуются.", "55", "Используй range(1, 11).", "print(sum(range(1, 11)))"),
    (11, "Факториал", "Средний", "Вычисли факториал числа 5 — произведение чисел от 1 до 5.", "n = 5", "120", "Можно использовать math.factorial().", "import math\nprint(math.factorial(5))"),
    (12, "Таблица умножения", "Начальный", "Выведи результаты умножения 7 на числа от 1 до 5, каждый результат с новой строки.", "Входные данные не требуются.", "7\n14\n21\n28\n35", "Используй цикл for.", "for i in range(1, 6):\n    print(7 * i)"),
    (13, "Тип числа", "Начальный", "Определи, является ли число 15 положительным, отрицательным или нулём. Выведи Positive, Negative или Zero.", "n = 15", "Positive", "Используй if, elif и else.", 'n = 15\nif n > 0:\n    print("Positive")\nelif n < 0:\n    print("Negative")\nelse:\n    print("Zero")'),
    (14, "Проверка возраста", "Начальный", "Если возраст равен 20, выведи Yes, если человеку не меньше 18 лет, иначе No.", "age = 20", "Yes", "Условие: age >= 18.", 'age = 20\nprint("Yes" if age >= 18 else "No")'),
    (15, "Количество гласных", "Средний", "Посчитай английские гласные (a, e, i, o, u) в слове banana.", "Входные данные не требуются.", "3", "Перебери буквы и проверь их наличие в строке гласных.", 'word = "banana"\nvowels = "aeiou"\ncount = sum(1 for char in word if char in vowels)\nprint(count)'),
    (16, "Удаление пробелов", "Начальный", "Удали пробелы в начале и конце строки, не меняя пробелы внутри.", 'text = "  hello  "', "hello", "Используй метод strip().", 'text = "  hello  "\nprint(text.strip())'),
    (17, "Сортировка списка", "Начальный", "Выведи числа списка [5, 2, 8, 1] по возрастанию.", "Входные данные не требуются.", "[1, 2, 5, 8]", "Функция sorted() сортирует элементы.", "numbers = [5, 2, 8, 1]\nprint(sorted(numbers))"),
    (18, "Уникальные элементы", "Средний", "Удали повторы из списка [1, 2, 2, 3] и выведи результат по возрастанию.", "Входные данные не требуются.", "[1, 2, 3]", "set() оставляет уникальные значения.", "numbers = [1, 2, 2, 3]\nprint(sorted(set(numbers)))"),
    (19, "Числа Фибоначчи", "Средний", "Выведи первые 7 чисел Фибоначчи, начиная с 0 и 1, через пробел.", "Входные данные не требуются.", "0 1 1 2 3 5 8", "Следующее число — сумма двух предыдущих.", "a, b = 0, 1\nresult = []\nfor _ in range(7):\n    result.append(a)\n    a, b = b, a + b\nprint(*result)"),
    (20, "Палиндром", "Средний", "Проверь, читается ли слово level одинаково слева направо и справа налево. Выведи Yes или No.", "word = level", "Yes", "Сравни строку с её перевёрнутой версией.", 'word = "level"\nprint("Yes" if word == word[::-1] else "No")'),
]

TASKS = [
    {"id": i, "title": title, "level": level, "description": desc,
     "input": inp, "output": out, "hint": hint, "solution": solution}
    for i, title, level, desc, inp, out, hint, solution in TASKS
]

@app.route("/")
def index():
    query = request.args.get("q", "").strip()
    level = request.args.get("level", "Все")
    filtered = TASKS
    if query:
        filtered = [t for t in filtered if query.lower() in t["title"].lower()
                    or query.lower() in t["description"].lower()]
    if level in ("Начальный", "Средний"):
        filtered = [t for t in filtered if t["level"] == level]
    return render_template("index.html", tasks=filtered, query=query,
                           level=level, total=len(TASKS))

@app.route("/task/<int:task_id>")
def task_detail(task_id):
    task = next((t for t in TASKS if t["id"] == task_id), None)
    if task is None:
        abort(404)
    return render_template("task.html", task=task, total=len(TASKS))

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
