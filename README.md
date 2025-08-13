# UI Test Automation Framework

[![CI][ci-badge]][ci-url] 
[![Python][py-badge]][py-url] 
[![Allure Report][allure-report-badge]][allure-report-url]
[![Coverage][cov-badge]][cov-url]
[![Pytest][pytest-badge]][pytest-url] 
[![Allure][allure-badge]][allure-url]
[![Pydantic][pydantic-badge]][pydantic-url]
[![Playwright][playwright-bage]][playwright-url]

[pydantic-badge]: https://img.shields.io/badge/Pydantic-2.11.7-0C4B33?logo=pydantic
[pydantic-url]: https://pypi.org/project/pydantic/
[ci-badge]:https://github.com/Pankirbor/autotests-ui/actions/workflows/tests.yml/badge.svg
[ci-url]:https://github.com/Pankirbor/autotests-ui/actions
[cov-badge]: https://img.shields.io/badge/UI_Coverage-95%25-green
[cov-url]: https://github.com/Pankirbor/autotests-ui/actions/runs/16933308440/artifacts/3753381098
[allure-report-badge]: https://img.shields.io/badge/Allure_Report-Latest-blueviolet?logo=allure
[allure-report-url]: https://pankirbor.github.io/autotests-ui/
[py-badge]: https://img.shields.io/badge/Python-3.11%2B-blue?logo=python
[py-url]: https://www.python.org/
[pytest-badge]: https://img.shields.io/badge/Pytest-8.4.1-0A9EDC?logo=pytest&logoColor=white
[pytest-url]: https://pypi.org/project/pytest/
[allure-badge]: https://img.shields.io/badge/allure--pytest-2.15.0-red
[allure-url]: https://pypi.org/project/allure-pytest/
[playwright-bage]: https://img.shields.io/badge/Playwright-1.53.0-2EAD33?logo=playwright
[playwright-url]: https://playwright.dev

## 🔧 Технологии

- **Python** - *язык программирования*
- **Playwright** - *кросс-браузерное тестирование*
- **Pytest** - *тестовый фреймворк*
- **Allure-pytest** - *визуализация отчётов*
- **UI Coverage Tool** - *анализ покрытия элементов интерфейса*
- **Pydantic** - *валидация данных*

## 🔍 Обзор проекта
Этот проект представляет собой автоматизированную систему тестирования веб-интерфейса [UI Course Test Application](https://nikita-filonov.github.io/qa-automation-engineer-ui-course/).
Основная цель - комплексная проверка пользовательского интерфейса и функциональности приложения с использованием современных практик автоматизации.

### 🔧 Ключевые особенности реализации

В проекте применяются передовые технологии и подходы:

- **Паттерны Page Object/Page Component/Page Factory** для структурированного взаимодействия с элементами UI
- **Playwright** для кросс-браузерного тестирования с авто-ожиданиями
- **Pytest-фикстуры** для создания гибких тестовых окружений
- **UI Coverage Tool** для визуализации покрытия тестами элементов интерфейса
- **Allure Report** с прикреплёнными скриншотами для наглядных отчётов

### 🏗 Архитектурные принципы

Проект построен с учётом лучших практик автоматизации:

- **Модульная структура** (страницы/компоненты/элементы/тесты)
- **Поддержка мультибраузерного тестирования** (Chromium, Firefox, WebKit)
- **Интеграция с CI/CD** для непрерывного тестирования
- **Визуальное отслеживание действий** через ui-coverage-tool

### 🧪 Что проверяем

Автотесты покрывают все ключественные разделы приложения:

| Маршрут | Описание | Тестовые сценарии |
|---------|----------|-------------------|
| `/#/auth/login` | Страница входа | Валидация полей, успешная авторизация |
| `/#/auth/registration` | Регистрация | Создание нового пользователя |
| `/#/dashboard` | Личный кабинет | Отображение персональных данных |
| `/#/courses` | Список курсов | Отображение, удаление |
| `/#/courses/create` | Создание курса | Валидация формы |

## ⚙️ Установка
```bash
git clone https://github.com/Pankirbor/autotests-ui.git
cd autotests-ui
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
playwright install
```
## 🚀 Запуск тестов
### 1. Запуск всех тестов с генерацией Allure-отчёта
```bash
pytest --alluredir=./allure-results
allure serve allure-results
```

### 2. Запуск только регрессионных тестов
```bash
pytest -m "regression" --alluredir=./allure-results
```

## 📬 Контакты
- Автор: [Pankirbor](https://github.com/Pankirbor)
- Тестируемый сайт: [UI Course Test Application](https://nikita-filonov.github.io/qa-automation-engineer-ui-course/).
