#!/usr/bin/env python3
"""
Скрипт для удаления ссылки с имени Hedgenious
"""

import os
import re
from pathlib import Path

def remove_hedgenious_link(filepath):
    """Удаляет ссылку с имени Hedgenious в одном файле"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        filename = filepath.name
        print(f"[ОБРАБОТКА] {filename}")

        # Удаляем ссылку с Hedgenious, оставляя только текст
        content = re.sub(
            r'<a href="https://ru\.wikipedia\.org/wiki/User:Hedgenious" target="_blank" style="color: #BFE0F7;">Hedgenious</a>',
            'Hedgenious',
            content
        )

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
    print("Удаление ссылки с имени Hedgenious...")
    print("=" * 50)

    mangistau_dir = Path('html/mangistau')
    fixed_count = 0
    total_count = 0

    # Обрабатываем все HTML файлы в папке mangistau
    for filepath in mangistau_dir.glob('*.html'):
        total_count += 1
        if remove_hedgenious_link(filepath):
            fixed_count += 1

    print("=" * 50)
    print(f"[РЕЗУЛЬТАТ] Исправлено {fixed_count} из {total_count} файлов")
    print("[ГОТОВО] Ссылка с имени Hedgenious удалена!")

if __name__ == "__main__":
    main()
