#!/usr/bin/env python3
"""
Скрипт для удаления логотипа Википедии и плашки с ней из футера
"""

import os
import re
from pathlib import Path

def remove_wikipedia_elements(filepath):
    """Удаляет элементы Википедии из одного файла"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        filename = filepath.name
        print(f"[ОБРАБОТКА] {filename}")

        # Удаляем логотип Википедии и плашку
        content = re.sub(r'<div class="footer-wikipedia-logo">.*?</div>', '', content, flags=re.DOTALL)
        
        # Удаляем пустые строки, которые могли остаться
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)

        # Сохраняем файл
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"[УСПЕХ] Исправлен файл: {filename}")
        return True

    except Exception as e:
        print(f"[ОШИБКА] Не удалось исправить файл {filepath}: {e}")
        return False

def main():
    """Главная функция"""
    print("Удаление логотипа Википедии и плашки...")
    print("=" * 50)

    mangistau_dir = Path('html/mangistau')
    fixed_count = 0
    total_count = 0

    # Обрабатываем все HTML файлы в папке mangistau
    for filepath in mangistau_dir.glob('*.html'):
        total_count += 1
        if remove_wikipedia_elements(filepath):
            fixed_count += 1

    print("=" * 50)
    print(f"[РЕЗУЛЬТАТ] Исправлено {fixed_count} из {total_count} файлов")
    print("[ГОТОВО] Логотип Википедии и плашка удалены!")

if __name__ == "__main__":
    main()
