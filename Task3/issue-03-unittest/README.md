# Задание 3: Тестирование с `unittest`

Проект содержит функцию `fit_transform` и набор тестов для нее с использованием стандартного модуля `unittest`.

## Запуск тестов

1.  Выполните в терминале следующую команду:
    ```bash
    python -m unittest test_one_hot_encoder_unittest.py
    ```

## Проверка стиля кода (flake8)

1.  Установите `flake8`: `pip install flake8`
2.  Запустите проверку:
    ```bash
    flake8 one_hot_encoder.py test_one_hot_encoder_unittest.py
    ```