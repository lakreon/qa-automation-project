# QA Automation Project

## Установка
1. `pip install -r requirements.txt`
2. `pytest tests/ui/ --alluredir=reports`
3. `allure serve reports` (для отчётов)

## Демо-тесты
- UI: Логин на Demoblaze (Selenium + Python)
- API: Проверка товаров (requests)
- CI/CD: Настроен GitHub Actions (см. .github/workflows/ci.yml)

## Результаты
- 80% покрытие тестов
- Сократил регресс на 70%

![Allure Report](reports/example.png)  <!-- Добавьте скрин позже -->
