#!/usr/bin/env python3
"""
Скрипт для обновления всех страниц вики с новой структурой
"""

import os
import re
from pathlib import Path

def update_navigation_menu(content):
    """Обновляет навигационное меню в шапке"""
    # Заменяем старое меню на новое
    old_nav = re.search(
        r'<nav class="nav">.*?</nav>',
        content,
        re.DOTALL
    )

    if old_nav:
        new_nav = '''                <nav class="nav">
                    <a href="../../index.html" class="nav-link">🏠 Главная</a>
                    <a href="index.html" class="nav-link active">🌍 Мангистау 2024</a>
                </nav>'''
        return content.replace(old_nav.group(), new_nav)

    return content

def add_sidebar_structure(content, filename):
    """Добавляет структуру с боковым меню"""
    # Определяем активную страницу
    active_links = {
        'index.html': 'Мангистау 2024',
        'about.html': 'О книге',
        'adaptation.html': 'Адаптация',
        'iucn-status.html': 'IUCN статусы',
        'resources.html': 'Полезные ресурсы',
        'glossary.html': 'Словарь терминов',
        'ustyurt.html': 'Устюрт',
        'bozzhyra.html': 'Бозжыра',
        'zhygylgan.html': 'Жыгылган',
        'kyzylkup.html': 'Кызылкуп',
        'kapamsai.html': 'Капамсай',
        'tuyesu.html': 'Туйесу',
        'karagie.html': 'Карагие',
        'torysh.html': 'Торыш',
        'species-guide.html': 'Путеводитель',
        'testudo-horsfieldii.html': 'Черепаха',
        'tenuidactylus-caspius.html': 'Геккон',
        'neophron-percnopterus.html': 'Стервятник',
        'bufotes-viridis.html': 'Жаба',
        'alectoris-chukar.html': 'Кеклик',
        'solifugae-spp.html': 'Солыпуга',
        'phrynocephalus-mystaceus.html': 'Круглоголовка',
        'trapelus-sanguinolentus.html': 'Арама',
        'natrix-natrix.html': 'Уж',
        'crinoidea-fossilis.html': 'Морские лилии',
        'echinoidea-fossilis.html': 'Морские ежи',
        'elasmobranchii-fossilis.html': 'Зубы акул'
    }

    active_text = active_links.get(filename, 'Мангистау 2024')

    # Создаем новую структуру для замены
    new_structure = f''' <main class="main">
  <div class="wiki-container">
   <aside class="sidebar">
    <nav class="sidebar-nav">
     <div class="nav-section">
      <h3 class="nav-section-title">
       <i class="fas fa-book"></i> Справочники
      </h3>
      <ul class="nav-list">
       <li><a href="index.html" class="nav-link{' active' if active_text == 'Мангистау 2024' else ''}">Мангистау 2024</a></li>
       <li><a href="about.html" class="nav-link{' active' if active_text == 'О книге' else ''}">О книге</a></li>
       <li><a href="adaptation.html" class="nav-link{' active' if active_text == 'Адаптация' else ''}">Адаптация</a></li>
       <li><a href="iucn-status.html" class="nav-link{' active' if active_text == 'IUCN статусы' else ''}">IUCN статусы</a></li>
       <li><a href="resources.html" class="nav-link{' active' if active_text == 'Полезные ресурсы' else ''}">Полезные ресурсы</a></li>
       <li><a href="glossary.html" class="nav-link{' active' if active_text == 'Словарь терминов' else ''}">Словарь терминов</a></li>
      </ul>
     </div>

     <div class="nav-section">
      <h3 class="nav-section-title">
       <i class="fas fa-mountain"></i> Местности
      </h3>
      <ul class="nav-list">
       <li><a href="ustyurt.html" class="nav-link{' active' if active_text == 'Устюрт' else ''}">Устюрт</a></li>
       <li><a href="bozzhyra.html" class="nav-link{' active' if active_text == 'Бозжыра' else ''}">Бозжыра</a></li>
       <li><a href="zhygylgan.html" class="nav-link{' active' if active_text == 'Жыгылган' else ''}">Жыгылган</a></li>
       <li><a href="kyzylkup.html" class="nav-link{' active' if active_text == 'Кызылкуп' else ''}">Кызылкуп</a></li>
       <li><a href="kapamsai.html" class="nav-link{' active' if active_text == 'Капамсай' else ''}">Капамсай</a></li>
       <li><a href="tuyesu.html" class="nav-link{' active' if active_text == 'Туйесу' else ''}">Туйесу</a></li>
       <li><a href="karagie.html" class="nav-link{' active' if active_text == 'Карагие' else ''}">Карагие</a></li>
       <li><a href="torysh.html" class="nav-link{' active' if active_text == 'Торыш' else ''}">Торыш</a></li>
      </ul>
     </div>

     <div class="nav-section">
      <h3 class="nav-section-title">
       <i class="fas fa-paw"></i> Животные
      </h3>
      <ul class="nav-list">
       <li><a href="species-guide.html" class="nav-link{' active' if active_text == 'Путеводитель' else ''}">Путеводитель</a></li>
       <li><a href="testudo-horsfieldii.html" class="nav-link{' active' if active_text == 'Черепаха' else ''}">Черепаха</a></li>
       <li><a href="tenuidactylus-caspius.html" class="nav-link{' active' if active_text == 'Геккон' else ''}">Геккон</a></li>
       <li><a href="neophron-percnopterus.html" class="nav-link{' active' if active_text == 'Стервятник' else ''}">Стервятник</a></li>
       <li><a href="bufotes-viridis.html" class="nav-link{' active' if active_text == 'Жаба' else ''}">Жаба</a></li>
       <li><a href="alectoris-chukar.html" class="nav-link{' active' if active_text == 'Кеклик' else ''}">Кеклик</a></li>
       <li><a href="solifugae-spp.html" class="nav-link{' active' if active_text == 'Солыпуга' else ''}">Солыпуга</a></li>
       <li><a href="phrynocephalus-mystaceus.html" class="nav-link{' active' if active_text == 'Круглоголовка' else ''}">Круглоголовка</a></li>
       <li><a href="trapelus-sanguinolentus.html" class="nav-link{' active' if active_text == 'Арама' else ''}">Арама</a></li>
       <li><a href="natrix-natrix.html" class="nav-link{' active' if active_text == 'Уж' else ''}">Уж</a></li>
      </ul>
     </div>

     <div class="nav-section">
      <h3 class="nav-section-title">
       <i class="fas fa-fossil"></i> Ископаемые
      </h3>
      <ul class="nav-list">
       <li><a href="crinoidea-fossilis.html" class="nav-link{' active' if active_text == 'Морские лилии' else ''}">Морские лилии</a></li>
       <li><a href="echinoidea-fossilis.html" class="nav-link{' active' if active_text == 'Морские ежи' else ''}">Морские ежи</a></li>
       <li><a href="elasmobranchii-fossilis.html" class="nav-link{' active' if active_text == 'Зубы акул' else ''}">Зубы акул</a></li>
      </ul>
     </div>
    </nav>
   </aside>

   <div class="content-area">
    <div class="breadcrumb">
     <a href="../../index.html">Главная</a> / <a href="index.html">Мангистау 2024</a> / <span>{active_text}</span>
    </div>'''

    # Заменяем начало main на новую структуру
    content = re.sub(r'<main class="main">', new_structure, content)

    # Находим и удаляем старые заголовки и контент
    content = re.sub(r'<section class="page-hero">.*?</section>', '', content, flags=re.DOTALL)

    return content

def update_page(filepath):
    """Обновляет одну страницу"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        filename = filepath.name
        print(f"[ОБРАБОТКА] {filename}")

        # Обновляем навигационное меню
        content = update_navigation_menu(content)

        # Добавляем боковую структуру
        content = add_sidebar_structure(content, filename)

        # Удаляем старую навигацию если она есть
        content = re.sub(r'<!-- Навигация с 4 группами -->.*?<!-- Конец навигации -->', '', content, flags=re.DOTALL)
        content = re.sub(r'<section class="mangistau-nav">.*?</section>', '', content, flags=re.DOTALL)

        # Находим конец контента и добавляем закрывающие теги
        footer_match = re.search(r'(</div>\s*</div>\s*</footer>)', content)
        if footer_match:
            content = content.replace(
                footer_match.group(),
                '   </div>\n  </div>\n </footer>'
            )

        # Сохраняем файл
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"[УСПЕХ] Обновлен файл: {filename}")
        return True

    except Exception as e:
        print(f"[ОШИБКА] Не удалось обновить файл {filepath}: {e}")
        return False

def main():
    """Главная функция"""
    print("Обновление всех страниц вики...")
    print("=" * 50)

    mangistau_dir = Path('html/mangistau')
    updated_count = 0
    total_count = 0

    # Обрабатываем все HTML файлы в папке mangistau
    for filepath in mangistau_dir.glob('*.html'):
        total_count += 1
        if update_page(filepath):
            updated_count += 1

    print("=" * 50)
    print(f"[РЕЗУЛЬТАТ] Обновлено {updated_count} из {total_count} файлов")
    print("[ГОТОВО] Все страницы обновлены с новой структурой!")

if __name__ == "__main__":
    main()
