#!/usr/bin/env python3
"""
Скрипт для обновления путей в HTML файлах после реорганизации структуры проекта
"""

import os
import re

def update_html_paths(file_path, is_root=False):
    """Обновляет пути в HTML файле"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    if is_root:
        # Для корневого index.html
        content = content.replace('href="styles.css"', 'href="assets/css/styles.css"')
        content = content.replace('src="script.js"', 'src="assets/js/script.js"')
        content = content.replace('src="logo/logo_dada_2.svg"', 'src="assets/images/logo_dada_2.svg"')
        content = content.replace('src="logo/logo_dada.svg"', 'src="assets/images/logo_dada.svg"')
        content = content.replace('src="logo/Wikipedia-logo-v2.svg.png"', 'src="assets/images/Wikipedia-logo-v2.svg.png"')
        content = content.replace('src="img/', 'src="assets/images/')
        content = content.replace('src="img_2_pages/', 'src="assets/images/')
        
        # Ссылки на другие HTML страницы
        content = re.sub(r'href="([^"]+\.html)"', r'href="html/\1"', content)
        # Но не трогаем index.html
        content = content.replace('href="html/index.html"', 'href="index.html"')
    else:
        # Для HTML файлов в папке html/
        content = content.replace('href="styles.css"', 'href="../assets/css/styles.css"')
        content = content.replace('src="script.js"', 'src="../assets/js/script.js"')
        content = content.replace('src="logo/logo_dada_2.svg"', 'src="../assets/images/logo_dada_2.svg"')
        content = content.replace('src="logo/logo_dada.svg"', 'src="../assets/images/logo_dada.svg"')
        content = content.replace('src="logo/Wikipedia-logo-v2.svg.png"', 'src="../assets/images/Wikipedia-logo-v2.svg.png"')
        content = content.replace('src="img/', 'src="../assets/images/')
        content = content.replace('src="img_2_pages/', 'src="../assets/images/')
        
        # Ссылки на другие HTML страницы (остаются в той же папке)
        content = content.replace('href="index.html"', 'href="../index.html"')
        
    # Обновляем wiki_Mangistau пути
    if not is_root:
        content = content.replace('href="wiki_Mangistau/', 'href="../wiki_Mangistau/')
        content = content.replace('target="_blank">wiki_Mangistau/', 'target="_blank">../wiki_Mangistau/')
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"+ Updated: {file_path}")
        return True
    else:
        print(f"- No changes: {file_path}")
        return False

def main():
    """Главная функция"""
    print("Updating paths in HTML files...\n")
    
    updated_count = 0
    
    # Обновляем корневой index.html
    if os.path.exists('index.html'):
        if update_html_paths('index.html', is_root=True):
            updated_count += 1
    
    # Обновляем HTML файлы в папке html/
    html_dir = 'html'
    if os.path.exists(html_dir):
        for filename in os.listdir(html_dir):
            if filename.endswith('.html'):
                filepath = os.path.join(html_dir, filename)
                if update_html_paths(filepath, is_root=False):
                    updated_count += 1
    
    print(f"\n=== Files updated: {updated_count} ===")

if __name__ == '__main__':
    main()
