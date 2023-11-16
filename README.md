# Инструкция по использованию скрипта

Этот скрипт создает JSON и CSV файлы, содержащие адреса кошельков Ethereum на основе списка приватных ключей. Вот пошаговая инструкция:

## Шаг 1: Установка Python

Убедитесь, что на вашем компьютере установлен [Python](https://www.python.org/downloads/). Если нет, [скачайте и установите Python](https://www.python.org/downloads/). При установке выберите опцию "Add Python to PATH".

## Шаг 2: Скачивание скрипта

1. Нажмите на кнопку "Code" в репозитории на [GitHub](https://github.com/oblakov0372/From_PrivateKey_To_Address).
2. Выберите "Download ZIP".
3. Распакуйте архив в удобное место на вашем компьютере.

## Шаг 3: Подготовка списка приватных ключей

1. Создайте файл `private_keys.txt`.
2. Внесите в него приватные ключи кошельков, каждый ключ на отдельной строке.

**Пример файла `private_keys.txt`:**

```plaintext
0x1a2b3c...
0x4d5e6f...
...
```

## Шаг 4: Подготовка и запуск скрипта

1. Откройте командную строку (Command Prompt на Windows, Terminal на macOS/Linux).
2. Перейдите в папку со скриптом: cd путь*к*папке.
3. Введите команду: pip install -r requirements.txt.
4. Запустите скрипт: python main.py.

## Шаг 5: Получение результатов

После выполнения скрипта будут созданы два файла:

all_data.json содержит информацию в формате JSON.
all_data.csv представляет собой CSV файл с колонками "private_key" и "wallet_address".

# Рекомендация: Импортируйте all_data.csv в Google Таблицы для удобства работы с данными
