# Быстрый старт

## 1. Установка зависимостей (Подготовка окружения)
1. Создаем виртуальное окружение в корне проекта

Открываем терминал, находясь в корневой папке проекта создаем .venv

**MacOS**
```shell
python3 -m venv .venv
source .venv/bin/activate
```

**Windows**
```shell
python -m venv .venv
.venv\Scripts\activate
```

2. Активируйте виртуальное окружение (если еще не активировано)

**MacOS**
```shell
source .venv/bin/activate
```

**Windows**
```shell
.venv\Scripts\activate
```

3. Устанавливаем зависимости

**MacOS и Windows**
```shell
pip install -r requirements.txt
```

Если файла requirements.txt нет, установите необходимые библиотеки:
```shell
pip install langchain langchain-openai tavily langchain-community langgraph && pip install 'langgraph-cli[inmem]'
```

## 2. Настройка API-ключей

1. Создайте файл .env в корне проекта по образу .env.example

```shell
cp .env.example .env
```

2. Добавьте API-ключи в файл .env:
```
OPENAI_API_KEY=ваш_ключ_openai
TAVILY_API_KEY=ваш_ключ_tavily
```

## 3. Запуск проекта


1. Запуск LangGraph Dev Server

```shell
langgraph dev
```

## 4. Устранение проблем

Если возникает ошибка "module not found", убедитесь что:
1. Виртуальное окружение активировано
2. Все зависимости установлены
3. Вы запускаете команды из корневой директории проекта
