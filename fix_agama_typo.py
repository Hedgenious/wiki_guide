#!/usr/bin/env python3
"""
Скрипт для исправления опечатки "Арама" на "Агама"
"""

import os
import re
from pathlib import Path

def fix_agama_typo(filepath):
    """Исправляет опечатку в одном файле"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        filename = filepath.name
        print(f"[ОБРАБОТКА] {filename}")

        # Исправляем "Арама" на "Агама" в ссылках
        content = content.replace('>Арама<', '>Агама<')
        content = content.replace('"Арама"', '"Агама"')
        content = content.replace('Арама</a>', 'Агама</a>')
        
        # Исправляем в навигационных кнопках
        content = content.replace('>Арама <', '>Агама <')
        content = content.replace('>Арама</', '>Агама</')

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
    print("Исправление опечатки 'Арама' на 'Агама'...")
    print("=" * 50)

    mangistau_dir = Path('html/mangistau')
    fixed_count = 0
    total_count = 0

    # Обрабатываем все HTML файлы в папке mangistau
    for filepath in mangistau_dir.glob('*.html'):
        total_count += 1
        if fix_agama_typo(filepath):
            fixed_count += 1

    print("=" * 50)
    print(f"[РЕЗУЛЬТАТ] Исправлено {fixed_count} из {total_count} файлов")
    print("[ГОТОВО] Опечатка 'Арама' исправлена на 'Агама'!")

if __name__ == "__main__":
    main()
