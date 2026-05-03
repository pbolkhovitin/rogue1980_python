# Rogue 1980 Python

Клон классической игры Rogue 1980, написанный на Python 3.10 с использованием библиотеки `curses`.

## О проекте

- **Язык:** Python 3.10
- **Интерфейс:** Консольный (curses)
- **Архитектура:** Чистая архитектура (domain/presentation/data)

## Установка

```bash
git clone git@github.com:pbolkhovitin/rouge1980_python.git
cd rouge1980_python
make setup
```

## Запуск

```bash
make run
```

## Проверки

```bash
make check    # Все проверки (mypy, lint, test)
make lint     # Проверка линтером (ruff)
make format   # Форматирование кода
make test     # Запуск тестов
```
