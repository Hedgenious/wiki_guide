# DaDa School Wiki Guide

Полное руководство по работе с Википедией для детей и начинающих.

## 📁 Структура проекта

```
wiki_guide/
├── index.html              # Главная страница сайта
├── html/                   # HTML страницы
│   ├── registration.html   # Регистрация в Википедии
│   ├── editing.html        # Редактирование статей
│   ├── nickname.html       # Выбор никнейма
│   ├── best-practices.html # Лучшие практики
│   ├── faq.html           # Часто задаваемые вопросы
│   ├── image-quality.html  # Требования к изображениям
│   ├── citation-format.html # Форматирование цитат
│   ├── language-style.html # Языковой стиль
│   ├── sources-guide.html  # Работа с источниками
│   ├── fun-facts.html      # Интересные факты о Википедии
│   └── mangistau.html      # Путеводитель по природе Мангистау
├── assets/                 # Ресурсы сайта
│   ├── css/
│   │   └── styles.css      # Основные стили
│   ├── js/
│   │   └── script.js       # JavaScript функционал
│   ├── images/             # Все изображения
│   │   ├── logo_dada_2.svg
│   │   ├── wiki_*.png      # Скриншоты для руководств
│   │   └── Wikipedia-logo-v2.svg.png
│   └── fonts/              # Шрифты (если нужны)
├── docs/                   # Документация в Markdown
│   ├── README_GITHUB_PAGES.md
│   ├── PUBLISHING.md
│   ├── best_practices.md
│   ├── editing_guide.md
│   ├── registration_guide.md
│   ├── nickname_guide.md
│   ├── faq.md
│   └── ...                 # Другие .md файлы
├── wiki_Mangistau/         # Контент о природе Мангистау
│   ├── 0_оглавление/
│   ├── 1_Введение/
│   ├── 2_Справочные_главы/
│   ├── 3_Местности/
│   ├── 4_Виды/
│   ├── 6_Дополнительно/
│   ├── photos/
│   └── README.md
└── _config.yml             # Конфигурация Jekyll

```

## 🚀 Быстрый старт

### Локальная разработка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/hedgenious/wiki_guide.git
cd wiki_guide
```

2. Откройте `index.html` в браузере

### GitHub Pages

Сайт автоматически деплоится через GitHub Pages. После push в ветку `main`, изменения появятся на:
- https://hedgenious.github.io/wiki_guide/

## 📖 Содержание

### Основные руководства

1. **[Регистрация](html/registration.html)** - Как создать аккаунт в Википедии
2. **[Редактирование](html/editing.html)** - Основы редактирования статей
3. **[Выбор никнейма](html/nickname.html)** - Как выбрать безопасный никнейм
4. **[Лучшие практики](html/best-practices.html)** - Правила хорошего тона
5. **[FAQ](html/faq.html)** - Ответы на частые вопросы

### Специальные темы

- **[Качество изображений](html/image-quality.html)** - Требования к фотографиям
- **[Формат цитирования](html/citation-format.html)** - ГОСТ и другие стандарты
- **[Языковой стиль](html/language-style.html)** - Правила написания текстов
- **[Источники информации](html/sources-guide.html)** - Как работать с источниками

### Дополнительно

- **[Интересные факты](html/fun-facts.html)** - Удивительные факты о Википедии
- **[Мангистау 2024](html/mangistau.html)** - Путеводитель по природе Мангистау

## 🎨 Дизайн

Сайт использует современный дизайн с:
- Цветовая палитра DaDa School (синий #1E4EBD, желтый #F7E080)
- Адаптивный дизайн для всех устройств
- Плавные анимации и переходы
- Фиксированная шапка при скроллинге

## 🛠️ Технологии

- HTML5
- CSS3 (с переменными и grid/flexbox)
- Vanilla JavaScript
- Font Awesome иконки
- Google Fonts

## 👥 Авторы

- **Created and edited by:** [Hedgenious](https://ru.wikipedia.org/wiki/User:Hedgenious)
- **Organization:** [DaDa School](https://schooldada.com/project)

## 📄 Лицензия

Проект распространяется под лицензией MIT.

---

© 2025 DaDa School Wiki Guide. All rights reserved.