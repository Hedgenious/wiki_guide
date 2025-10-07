#!/usr/bin/env python3
"""
Скрипт для замены "FAQ" на "Вопросы"
"""

import os
import re
from pathlib import Path

def replace_faq(filepath):
    """Заменяет FAQ на Вопросы в одном файле"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        filename = filepath.name
        print(f"[ОБРАБОТКА] {filename}")

        # Заменяем FAQ на Вопросы
        content = content.replace('FAQ', 'Вопросы')
        content = content.replace('faq', 'вопросы')
        content = content.replace('Faq', 'Вопросы')

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
    print("Замена 'FAQ' на 'Вопросы'...")
    print("=" * 50)

    mangistau_dir = Path('html/mangistau')
    fixed_count = 0
    total_count = 0

    # Обрабатываем все HTML файлы в папке mangistau
    for filepath in mangistau_dir.glob('*.html'):
        total_count += 1
        if replace_faq(filepath):
            fixed_count += 1

    print("=" * 50)
    print(f"[РЕЗУЛЬТАТ] Исправлено {fixed_count} из {total_count} файлов")
    print("[ГОТОВО] 'FAQ' заменено на 'Вопросы'!")

if __name__ == "__main__":
    main()
