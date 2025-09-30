#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Конвертер Markdown файлов вики Мангистау в HTML страницы
"""

import os
import re
from pathlib import Path

# HTML шаблон для страниц
HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Мангистау 2024 - DaDa School</title>
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
                    <a href="../../index.html" class="nav-link">Главная</a>
                    <a href="../registration.html" class="nav-link">Регистрация</a>
                    <a href="../editing.html" class="nav-link">Редактирование</a>
                    <a href="../nickname.html" class="nav-link">Никнейм</a>
                    <a href="../best-practices.html" class="nav-link">Практики</a>
                    <a href="index.html" class="nav-link active">Мангистау 2024</a>
                    <a href="../fun-facts.html" class="nav-link">Факты</a>
                </nav>
            </div>
        </div>
    </header>

    <main class="main">
        <section class="page-hero" style="padding: 2rem 0;">
            <div class="container">
                <div class="breadcrumb">
                    <a href="../../index.html">Главная</a> / <a href="index.html">Мангистау 2024</a> / <span>{title}</span>
                </div>
                <h1 class="page-title">
                    {icon}
                    {title}
                </h1>
            </div>
        </section>

        <section class="content-section">
            <div class="container">
                <div class="content-wrapper">
                    <div class="content-main">
                        <div class="wiki-article">
                            {content}
                        </div>
                        
                        <div style="margin-top: 3rem; padding-top: 2rem; border-top: 2px solid #BFE0F7;">
                            <a href="index.html" class="cta-button primary">
                                <i class="fas fa-arrow-left"></i> Вернуться к оглавлению
                            </a>
                        </div>
                    </div>

                    <div class="content-sidebar">
                        <div class="sidebar-card">
                            <h3><i class="fas fa-list"></i> Навигация</h3>
                            <ul>
                                <li><a href="index.html">Оглавление</a></li>
                                <li><a href="about.html">О книге</a></li>
                                <li><a href="adaptation.html">Адаптация</a></li>
                                <li><a href="iucn-status.html">Статусы МСОП</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>О проекте</h3>
                    <p>DaDa School Wiki Guide — образовательный проект о работе с Википедией</p>
                </div>
                <div class="footer-section">
                    <h3>Ссылки</h3>
                    <ul>
                        <li><a href="../../index.html">Главная</a></li>
                        <li><a href="../registration.html">Регистрация</a></li>
                        <li><a href="../editing.html">Редактирование</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h3>Поддержка</h3>
                    <ul>
                        <li><a href="../faq.html">Вопросы</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-wikipedia-logo">
                <img src="../../assets/images/Wikipedia-logo-v2.svg.png" alt="Логотип Википедии" class="footer-wikipedia-logo-img">
                <span>Википедия</span>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2025 DaDa School Wiki Guide. Created and edited by <a href="https://ru.wikipedia.org/wiki/User:Hedgenious" target="_blank" style="color: #BFE0F7;">Hedgenious</a>. Распространяется под лицензией MIT.</p>
                <p><a href="https://schooldada.com/project" target="_blank" style="color: #BFE0F7;">DaDa School Official Website</a></p>
            </div>
        </div>
    </footer>

    <script src="../../assets/js/script.js"></script>
</body>
</html>'''

def markdown_to_html(md_text):
    """Конвертирует простой Markdown в HTML"""
    html = md_text
    
    # Заголовки
    html = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2><i class="fas fa-bookmark"></i> \1</h2>', html, flags=re.MULTILINE)
    
    # Жирный текст
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    
    # Курсив
    html = re.sub(r'\*([^*]+?)\*', r'<em>\1</em>', html)
    
    # Изображения
    html = re.sub(r'!\[([^\]]+)\]\(([^)]+)\)', r'<img src="\2" alt="\1" class="wiki-image" style="max-width: 800px; border-radius: 12px; margin: 2rem auto; display: block;">', html)
    
    # Ссылки
    html = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank">\1</a>', html)
    
    # Списки (простая версия)
    html = re.sub(r'^- (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    html = re.sub(r'(<li>.*</li>)', r'<ul>\n\1\n</ul>', html, flags=re.DOTALL)
    
    # Blockquotes
    html = re.sub(r'^> (.+)$', r'<blockquote>\1</blockquote>', html, flags=re.MULTILINE)
    
    # Параграфы
    lines = html.split('\n\n')
    processed_lines = []
    for line in lines:
        line = line.strip()
        if line and not line.startswith('<'):
            processed_lines.append(f'<p>{line}</p>')
        else:
            processed_lines.append(line)
    html = '\n\n'.join(processed_lines)
    
    # Специальные блоки
    html = html.replace('**Знаешь ли ты?**', '<div class="did-you-know"><strong><i class="fas fa-lightbulb"></i> Знаешь ли ты?</strong>')
    html = html.replace('**Попробуй сам!**', '</div><div class="try-it"><strong><i class="fas fa-tasks"></i> Попробуй сам!</strong>')
    html = html.replace('*А ты бы смог', '</div><div class="try-it"><em>А ты бы смог')
    
    return html

def get_icon_for_category(filename):
    """Возвращает иконку в зависимости от типа статьи"""
    if 'about' in filename or 'О_книге' in filename:
        return '<i class="fas fa-book-open"></i>'
    elif 'adaptation' in filename or 'адаптация' in filename.lower():
        return '<i class="fas fa-seedling"></i>'
    elif 'iucn' in filename or 'статус' in filename.lower():
        return '<i class="fas fa-shield-alt"></i>'
    elif 'species' in filename or 'Как_описывать' in filename:
        return '<i class="fas fa-search"></i>'
    elif any(x in filename.lower() for x in ['testudo', 'черепах']):
        return '<i class="fas fa-turtle"></i>'
    elif any(x in filename.lower() for x in ['neophron', 'птиц', 'alectoris']):
        return '<i class="fas fa-dove"></i>'
    elif any(x in filename.lower() for x in ['bufotes', 'жаб']):
        return '<i class="fas fa-frog"></i>'
    elif 'fossilis' in filename.lower() or 'ископаем' in filename.lower():
        return '<i class="fas fa-bone"></i>'
    else:
        return '<i class="fas fa-mountain"></i>'

def create_html_page(md_file, output_dir):
    """Создает HTML страницу из Markdown файла"""
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Извлекаем заголовок
    title_match = re.search(r'^# (.+)$', md_content, re.MULTILINE)
    title = title_match.group(1) if title_match else "Статья"
    
    # Удаляем первый заголовок из контента
    md_content = re.sub(r'^# .+\n', '', md_content, count=1)
    
    # Конвертируем Markdown в HTML
    html_content = markdown_to_html(md_content)
    
    # Определяем имя файла
    filename = os.path.basename(md_file).replace('.md', '.html')
    filename = filename.lower()
    filename = filename.replace('_', '-')
    filename = filename.replace('testudo-horsfieldii', 'testudo-horsfieldii')
    filename = filename.replace('1-0-о-книге', 'about')
    filename = filename.replace('5-0-что-такое-адаптация', 'adaptation')
    filename = filename.replace('5-1-iucn-статусы', 'iucn-status')
    filename = filename.replace('4-0-как-описывать-вид', 'species-guide')
    filename = filename.replace('3-1-устюрт', 'ustyurt')
    filename = filename.replace('3-2-бозжыра', 'bozzhyra')
    filename = filename.replace('3-3-жыгылган', 'zhygylgan')
    filename = filename.replace('3-4-кызылкуп', 'kyzylkup')
    filename = filename.replace('3-5-капамсай', 'kapamsai')
    filename = filename.replace('3-6-туйесу', 'tuyesu')
    filename = filename.replace('3-7-карагие', 'karagie')
    filename = filename.replace('3-8-торыш', 'torysh')
    
    # Получаем иконку
    icon = get_icon_for_category(filename)
    
    # Создаем HTML из шаблона
    html_page = HTML_TEMPLATE.format(
        title=title,
        icon=icon,
        content=html_content
    )
    
    # Сохраняем файл
    output_file = os.path.join(output_dir, filename)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_page)
    
    print(f"Created: {output_file}")

def main():
    """Главная функция"""
    wiki_dir = Path("wiki_Mangistau")
    output_dir = Path("html/mangistau")
    
    # Создаем выходную директорию если её нет
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Обрабатываем все .md файлы
    md_files = list(wiki_dir.rglob("*.md"))
    
    print(f"Found {len(md_files)} Markdown files")
    print("Converting...")
    
    for md_file in md_files:
        if md_file.name != "README.md" and md_file.name != "0_1_Оглавление.md":
            try:
                create_html_page(md_file, output_dir)
            except Exception as e:
                print(f"Error processing {md_file}: {e}")
    
    print("\nConversion completed!")

if __name__ == "__main__":
    main()
