#!/usr/bin/env python3
"""
Скрипт для исправления всех страниц вики Мангистау
"""

import os
import re
from pathlib import Path

def get_page_order():
    """Возвращает порядок страниц для навигации"""
    return [
        # Справочники
        'index.html', 'about.html', 'adaptation.html', 'iucn-status.html', 'resources.html', 'glossary.html',
        # Местности
        'ustyurt.html', 'bozzhyra.html', 'zhygylgan.html', 'kyzylkup.html', 'kapamsai.html', 'tuyesu.html', 'karagie.html', 'torysh.html',
        # Животные
        'species-guide.html', 'testudo-horsfieldii.html', 'tenuidactylus-caspius.html', 'neophron-percnopterus.html', 'bufotes-viridis.html', 'alectoris-chukar.html', 'solifugae-spp.html', 'phrynocephalus-mystaceus.html', 'trapelus-sanguinolentus.html', 'natrix-natrix.html',
        # Ископаемые
        'crinoidea-fossilis.html', 'echinoidea-fossilis.html', 'elasmobranchii-fossilis.html'
    ]

def get_page_title(filename):
    """Возвращает заголовок страницы"""
    titles = {
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
    return titles.get(filename, 'Страница')

def create_sidebar_nav(filename):
    """Создает боковое меню"""
    active_text = get_page_title(filename)
    
    return f'''   <aside class="sidebar">
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
   </aside>'''

def create_navigation_links(filename):
    """Создает ссылки на предыдущую и следующую страницы"""
    page_order = get_page_order()
    current_index = page_order.index(filename) if filename in page_order else 0
    
    prev_link = ""
    next_link = ""
    
    if current_index > 0:
        prev_file = page_order[current_index - 1]
        prev_title = get_page_title(prev_file)
        prev_link = f'<a href="{prev_file}" class="nav-button prev"><i class="fas fa-arrow-left"></i> {prev_title}</a>'
    
    if current_index < len(page_order) - 1:
        next_file = page_order[current_index + 1]
        next_title = get_page_title(next_file)
        next_link = f'<a href="{next_file}" class="nav-button next">{next_title} <i class="fas fa-arrow-right"></i></a>'
    
    if prev_link or next_link:
        return f'''<div class="page-navigation">
  <div class="nav-buttons">
   {prev_link}
   {next_link}
  </div>
 </div>'''
    return ""

def fix_page(filepath):
    """Исправляет одну страницу"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        filename = filepath.name
        page_title = get_page_title(filename)
        
        print(f"[ОБРАБОТКА] {filename}")

        # Создаем правильную структуру
        new_content = f'''<!DOCTYPE html>
<html lang="ru">
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>{page_title} - Мангистау 2024 - DaDa School</title>
 <link rel="stylesheet" href="../../assets/css/styles.css">
 <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
 <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</head>
<body>
 <header class="header">
 <div class="container">
 <div class="header-content">
 <h1 class="logo">
 <a href="../../index.html" style="color: white; text-decoration: none; display: flex; align-items: center; gap: 0.5rem;">
 <img src="../../assets/images/logo_dada_2.svg" alt="DaDa School" class="logo-image">
 DaDa School Wiki Guide
 </a>
 </h1>
                <nav class="nav">
                    <a href="../../index.html" class="nav-link">🏠 Главная</a>
                    <a href="index.html" class="nav-link active">🌍 Мангистау 2024</a>
                </nav>
 </div>
 </div>
 </header>

 <main class="main">
  <div class="wiki-container">
{create_sidebar_nav(filename)}

   <div class="content-area">
    <div class="breadcrumb">
     <a href="../../index.html">Главная</a> / <a href="index.html">Мангистау 2024</a> / <span>{page_title}</span>
    </div>
    <h1 class="page-title">
     <i class="fas fa-mountain"></i>
     {page_title}
    </h1>'''

        # Извлекаем основной контент (между <main> и </main>)
        main_match = re.search(r'<main[^>]*>(.*?)</main>', content, re.DOTALL)
        if main_match:
            main_content = main_match.group(1)
            
            # Ищем контент статьи
            article_match = re.search(r'<div class="wiki-article">(.*?)</div>', main_content, re.DOTALL)
            if article_match:
                article_content = article_match.group(1)
                new_content += f'''
    <div class="wiki-article">
{article_content}
    </div>'''
            else:
                # Если не найдена статья, ищем любой контент
                content_match = re.search(r'<div[^>]*class="[^"]*content[^"]*"[^>]*>(.*?)</div>', main_content, re.DOTALL)
                if content_match:
                    article_content = content_match.group(1)
                    new_content += f'''
    <div class="wiki-article">
{article_content}
    </div>'''

        # Добавляем навигацию
        nav_links = create_navigation_links(filename)
        if nav_links:
            new_content += f'''
{nav_links}'''

        # Добавляем футер
        footer_match = re.search(r'<footer[^>]*>(.*?)</footer>', content, re.DOTALL)
        if footer_match:
            footer_content = footer_match.group(1)
            new_content += f'''
   </div>
  </div>
 </main>

 <footer class="footer">
{footer_content}
 </footer>

 <script src="../../assets/js/script.js"></script>

</body>
</html>'''

        # Сохраняем файл
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"[УСПЕХ] Исправлен файл: {filename}")
        return True

    except Exception as e:
        print(f"[ОШИБКА] Не удалось исправить файл {filepath}: {e}")
        return False

def main():
    """Главная функция"""
    print("Исправление всех страниц вики Мангистау...")
    print("=" * 50)

    mangistau_dir = Path('html/mangistau')
    fixed_count = 0
    total_count = 0

    # Обрабатываем все HTML файлы в папке mangistau
    for filepath in mangistau_dir.glob('*.html'):
        total_count += 1
        if fix_page(filepath):
            fixed_count += 1

    print("=" * 50)
    print(f"[РЕЗУЛЬТАТ] Исправлено {fixed_count} из {total_count} файлов")
    print("[ГОТОВО] Все страницы исправлены!")

if __name__ == "__main__":
    main()
