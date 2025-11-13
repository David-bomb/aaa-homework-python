# Задание 5: Тестирование с `unittest.mock` и измерением покрытия

Этот проект содержит тесты для функции `what_is_year_now`, которая обращается к внешнему API. Для изоляции от сети используется `unittest.mock`.

## Установка зависимостей

1.  Установите `coverage` для измерения покрытия кода тестами:
    ```bash
    pip install coverage
    ```

## Запуск тестов и получение отчета о покрытии

1.  Запустите тесты под управлением `coverage`:
    ```bash
    coverage run -m unittest test_what_is_year_now.py
    ```
2.  Выведите отчет о покрытии в консоль, чтобы убедиться в 100% результате:
    ```bash
    coverage report -m
    ```
3.  Сгенерируйте детальный HTML-отчет. Он будет создан в новой директории `htmlcov/`:
    ```bash
    coverage html
    ```
    Откройте файл `htmlcov/index.html` в браузере, чтобы посмотреть отчет.

## Проверка стиля кода (flake8)
1. Установите `flake8`: `pip install flake8`
2. Запустите проверку:
    ```bash
    flake8 what_is_year_now.py test_what_is_year_now.py
    ```