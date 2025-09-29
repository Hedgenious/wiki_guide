# Структура проекта DaDa School Wiki Guide

Этот документ описывает организацию файлов и папок в проекте после реорганизации.

## 📂 Корневая директория

```
wiki_guide/
├── index.html              ← Главная страница (копия из html/)
├── README.md               ← Описание проекта
├── STRUCTURE.md            ← Этот файл
├── _config.yml             ← Конфигурация Jekyll для GitHub Pages
│
├── html/                   ← Все HTML страницы
├── assets/                 ← Все ресурсы (CSS, JS, изображения)
├── docs/                   ← Документация в Markdown
├── wiki_Mangistau/         ← Контент о природе Мангистау
└── screenshots/            ← Скриншоты для документации
```

## 🗂️ Детальная структура

### `/html/` - HTML страницы

Все HTML-страницы сайта находятся в этой папке:

- `index.html` - Главная страница (также скопирована в корень)
- `registration.html` - Руководство по регистрации
- `editing.html` - Руководство по редактированию
- `nickname.html` - Выбор никнейма
- `best-practices.html` - Лучшие практики
- `faq.html` - Часто задаваемые вопросы
- `image-quality.html` - Требования к изображениям
- `citation-format.html` - Форматирование цитат (ГОСТ)
- `language-style.html` - Языковой стиль Википедии
- `sources-guide.html` - Работа с источниками
- `fun-facts.html` - Интересные факты о Википедии
- `mangistau.html` - Путеводитель по природе Мангистау

**Пути в HTML файлах:**
- CSS: `../assets/css/styles.css`
- JS: `../assets/js/script.js`
- Images: `../assets/images/`
- Другие HTML: `./filename.html`
- Главная: `../index.html`

### `/assets/` - Ресурсы сайта

#### `/assets/css/`
- `styles.css` - Основной файл стилей

#### `/assets/js/`
- `script.js` - JavaScript функционал

#### `/assets/images/`
Все изображения проекта:
- `logo_dada_2.svg` - Основной логотип DaDa School
- `logo_dada.svg` - Альтернативный логотип
- `Wikipedia-logo-v2.svg.png` - Логотип Википедии
- `wiki_*.png` - Скриншоты для руководств
- `google_*.png` - Скриншоты поиска Google

### `/docs/` - Документация

Markdown-файлы с исходными текстами:
- `README_GITHUB_PAGES.md` - Инструкция по GitHub Pages
- `PUBLISHING.md` - Руководство по публикации
- `registration_guide.md` - Регистрация (Markdown)
- `editing_guide.md` - Редактирование (Markdown)
- `nickname_guide.md` - Никнейм (Markdown)
- `best_practices.md` - Лучшие практики (Markdown)
- `faq.md` - FAQ (Markdown)
- `image_quality_requirements.md` - Качество изображений (Markdown)
- `citation_format_gost.md` - ГОСТ (Markdown)
- `information_sources_guide.md` - Источники (Markdown)
- `wikipedia_language_style.md` - Языковой стиль (Markdown)

### `/wiki_Mangistau/` - Контент о природе

Материалы образовательного проекта о природе Мангистау:

```
wiki_Mangistau/
├── 0_оглавление/          ← Оглавление проекта
├── 1_Введение/            ← Введение и цели
├── 2_Справочные_главы/    ← Теоретические материалы
├── 3_Местности/           ← Описания локаций (Устюрт, Бозжыра, и т.д.)
├── 4_Виды/                ← Описания животных и растений
├── 6_Дополнительно/       ← Словарь, ресурсы
├── photos/                ← Фотографии из экспедиции
└── README.md              ← Описание структуры Мангистау
```

### `/screenshots/` - Скриншоты

Технические скриншоты для документации.

## 🔗 Система ссылок

### Корневой index.html
```html
<link rel="stylesheet" href="assets/css/styles.css">
<script src="assets/js/script.js"></script>
<img src="assets/images/logo_dada_2.svg">
<a href="html/registration.html">Регистрация</a>
```

### HTML страницы в /html/
```html
<link rel="stylesheet" href="../assets/css/styles.css">
<script src="../assets/js/script.js"></script>
<img src="../assets/images/logo_dada_2.svg">
<a href="../index.html">Главная</a>
<a href="./editing.html">Редактирование</a>
```

## 🎯 Преимущества новой структуры

1. **Чистота корня** - Только основные файлы в корневой директории
2. **Логичная организация** - Ресурсы сгруппированы по типу
3. **Масштабируемость** - Легко добавлять новые файлы
4. **Стандарты** - Структура соответствует best practices веб-разработки
5. **GitHub Pages** - Совместимость с автоматическим деплоем

## 🚀 Деплой

Проект автоматически деплоится на GitHub Pages:
- **URL:** https://hedgenious.github.io/wiki_guide/
- **Ветка:** main
- **Источник:** корень репозитория

## 📝 Примечания

- `index.html` дублируется в корне для GitHub Pages
- Все пути обновлены автоматически через `update_paths.py`
- Старые папки `img/`, `img_2_pages/`, `logo/` удалены
- Markdown файлы перемещены в `docs/`

---

**Дата обновления:** 29 сентября 2025  
**Версия:** 2.0  
**Автор:** Hedgenious
