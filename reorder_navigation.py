#!/usr/bin/env python3
"""
Скрипт для изменения порядка кнопок навигации
"""

import os
import re
from pathlib import Path

def reorder_navigation(filepath):
    """Изменяет порядок кнопок навигации в одном файле"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        filename = filepath.name
        print(f"[ОБРАБОТКА] {filename}")

        # Новый порядок навигации
        new_nav = '''                <nav class="nav">
                    <a href="../../index.html" class="nav-link">🏠 Главная</a>
                    <a href="nickname.html" class="nav-link">👤 Никнейм</a>
                    <a href="registration.html" class="nav-link">📝 Регистрация</a>
                    <a href="test-registration.html" class="nav-link">🎓 Тест</a>
                    <a href="assignment.html" class="nav-link">❓ Задание</a>
                    <a href="mangistau/index.html" class="nav-link">🌍 Мангистау 2024</a>
                    <a href="hall-of-fame.html" class="nav-link">‼️ Зал славы</a>
                    <a href="faq.html" class="nav-link">❓ Вопросы</a>
                </nav>'''

        # Заменяем старую навигацию на новую
        content = re.sub(
            r'<nav class="nav">.*?</nav>',
            new_nav,
            content,
            flags=re.DOTALL
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
    print("Изменение порядка кнопок навигации...")
    print("=" * 50)

    # Обрабатываем все HTML файлы в папке html
    html_dir = Path('html')
    fixed_count = 0
    total_count = 0

    for filepath in html_dir.rglob('*.html'):
        total_count += 1
        if reorder_navigation(filepath):
            fixed_count += 1

    print("=" * 50)
    print(f"[РЕЗУЛЬТАТ] Исправлено {fixed_count} из {total_count} файлов")
    print("[ГОТОВО] Порядок кнопок навигации изменен!")

if __name__ == "__main__":
    main()
