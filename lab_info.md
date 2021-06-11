# Сдача лабораторных
## Загрузка решений
Ваше **решение добавляется** в папку с заданием **в формате .py файла с названием solution.py**. Оно должно работать при запуске из командной строки:
```sh
python3 solution.py <arguments>
```

**В добавляемом модуле solution.py обязательно должна содержаться функция solve, которая будет использоваться при автотестировании.**

**Скелет файла solution.py:**
```python
...
def solve(args):  # args соответствуют имена аргументов класса LabXTaskYData из модуля cases.py (см. раздел об автотестах)
    ...

if __name__ == "__main__":  # Обязательно, чтобы избежать исполнения кода при импортировании
    ...  # обработка аргументов
    res = solve(args)
    ...  # вывод результата
```

**Также не забываем использовать [.gitignore](https://git-scm.com/docs/gitignore) файл для игнорирования файлов конфигурации и .pyc файлов**

*Пример структуры директории для варианта по первой лабораторной [1, 3, 4, 7, 9, 12], по второй - [1, 2, 6, 9, 11] (в директориях с заданиями, которые не входят в вариант, файл с решениями отсутствует):*
```
.
├── Labs
│     ├── Lab1
│     │   ├── 1
|     |   |   ├── samples
|     |   |   ├── test_cases
|     |   |   ├── test_solution_1.py
│     │   |   └── solution.py
│     │   ├── 2
|     |   |   ├── samples
|     |   |   └── test_cases
│     │   ├── 3
|     |   |   ├── samples
|     |   |   ├── test_cases
|     |   |   ├── test_solution_3.py
│     │   |   └── solution.py
│     │   ├── 4
|     |   |   ├── samples
|     |   |   ├── test_cases
|     |   |   ├── test_solution_4.py
│     │   |   └── solution.py
│     │   ├── 5
|     |   |   ├── samples
|     |   |   └── test_cases
│     │   ├── 6
|     |   |   ├── samples
|     |   |   └── test_cases
│     │   ├── 7
|     |   |   ├── test_cases
|     |   |   ├── test_solution_7.py
│     │   |   └── solution.py
│     │   ├── 8
|     |   |   ├── samples
|     |   |   └── test_cases
│     │   ├── 9
|     |   |   ├── test_cases
|     |   |   ├── test_solution_9.py
│     │   |   └── solution.py
│     │   ├── 10
|     |   |   ├── samples
|     |   |   └── test_cases
│     │   ├── 11
|     |   |   ├── samples
|     |   |   └── test_cases
│     │   └── 12
|     |       ├── test_cases
|     |       ├── test_solution_12.py
│     │       └── solution.py
│     │
│     └── Lab2
│         ├── 1
|         |   ├── test_cases
|         |   ├── test_solution_1.py
|         |   └── solution.py
│         ├── 2
|         |   ├── test_cases
|         |   ├── test_solution_2.py
|         |   └── solution.py
│         ├── 3
|         |   └── test_cases
│         ├── 4
|         |   └── test_cases
│         ├── 5
|         |   └── test_cases
│         ├── 6
|         |   ├── test_cases
|         |   ├── test_solution_6.py
|         |   └── solution.py
│         ├── 7
|         |   └── test_cases
│         ├── 8
|         |   └── test_cases
│         ├── 9
|         |   ├── test_cases
|         |   ├── test_solution_9.py
|         |   └── solution.py
│         ├── 10
|         |   └── test_cases
│         └── 11
|             ├── test_cases
|             ├── tester.py
|             └── test_solution_11.py
│
├── lab_info.md
└── test_solution_X.py
```

## Автоматическое тестирование
Для автоматической проверки вашей программы был создан модуль **test_solution_X.py**, который можно найти в корне проекта.

Его следует скопировать в папку с заданием для проведения автотестирования. **Его название необходимо изменить с соответствии с номером задания (см. пример структуры директории).**

Для проведение тестирования используется внешний модуль **pytest**, который необходимо установить одной из следующих команд:
```bash
pip3 install pytest
or
python3 -m pip install pytest
```

Модуль **test_solution_X.py** берет тестовые данные из модуля **cases.py**, который расположен в папке **test_cases**. 

**Также он импортирует функцию solve из файла solution.py, который студенты добавляют самостоятельно.**

**Для успешного прохождения тестов необходимо, чтобы имена аргументов функции solve совпадали с полями класса LabXTaskYData, который находится в модуле cases.py в папке test_cases соответствующего задания**

Пример:
```python
# Модуль cases.py
...
@dataclass
class Lab1Task1Data:
    directory: str
    file: str
    is_recursive: bool
    depth: int
...

# Модуль solution.py
...
def solve(directory, file, is_recursive, depth):
    ...
...
```
**Можно увидеть, что имена аргументов функции solve соответствуют полям датакласса Lab1Task1Data**

Запуск тестов осуществляется из директории задания следующей командой:
```sh
pytest
```

Также можно запускать тесты из директории с лабораторной работой. Pytest рекурсивно найдет все файлы с тестами и проведет тестирование.

**Найти информацию об определенном тесте можно в переменной cases, которая находится в модуле cases.py в папке test_cases.**
