#!/usr/bin/env python3
"""
Скрипт для проверки идентичности шапок всех HTML файлов в папке html/
"""

import os
import re
from pathlib import Path

def read_file_content(filepath):
    """Читает содержимое файла и возвращает строки с номерами"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        return lines
    except Exception as e:
        return f"Ошибка чтения файла {filepath}: {e}"

def extract_header_section(lines):
    """Извлекает секцию header из HTML файла"""
    header_start = None
    header_end = None

    for i, line in enumerate(lines):
        if '<header class="header">' in line:
            header_start = i
        elif header_start is not None and '</header>' in line:
            header_end = i
            break

    if header_start is not None and header_end is not None:
        return ''.join(lines[header_start:header_end + 1])
    return None

def normalize_paths(header_content, file_path):
    """Нормализует относительные пути в header для корректного сравнения"""
    # Нормализуем пути к логотипу и изображениям
    normalized = header_content

    # Нормализуем пути к ресурсам (CSS, изображениям)
    normalized = re.sub(r'src="([^"]*logo_dada_2\.svg)"', 'src="logo_dada_2.svg"', normalized)
    normalized = re.sub(r'href="([^"]*styles\.css)"', 'href="styles.css"', normalized)

    # Нормализуем все вариации путей к страницам
    normalized = re.sub(r'href="([^"]*index\.html)"', 'href="index.html"', normalized)
    normalized = re.sub(r'href="([^"]*registration\.html)"', 'href="registration.html"', normalized)
    normalized = re.sub(r'href="([^"]*test-registration\.html)"', 'href="test-registration.html"', normalized)
    normalized = re.sub(r'href="([^"]*nickname\.html)"', 'href="nickname.html"', normalized)
    normalized = re.sub(r'href="([^"]*mangistau/index\.html)"', 'href="mangistau/index.html"', normalized)
    normalized = re.sub(r'href="([^"]*assignment\.html)"', 'href="assignment.html"', normalized)
    normalized = re.sub(r'href="([^"]*hall-of-fame\.html)"', 'href="hall-of-fame.html"', normalized)
    normalized = re.sub(r'href="([^"]*faq\.html)"', 'href="faq.html"', normalized)

    return normalized

def check_headers_consistency():
    """Проверяет все HTML файлы на идентичность шапок"""
    html_dir = Path('html')
    files = []

    # Собираем все HTML файлы
    for file_path in html_dir.rglob('*.html'):
        files.append(file_path)

    print(f"Найдено {len(files)} HTML файлов")

    headers = {}
    inconsistencies = []

    for file_path in files:
        lines = read_file_content(file_path)
        if isinstance(lines, str):  # Ошибка чтения
            print(f"[ОШИБКА] Не удалось прочитать файл {file_path}")
            continue

        header = extract_header_section(lines)
        if header is None:
            print(f"[ОШИБКА] Не найдена секция header в файле {file_path}")
            continue

        # Создаем ключ для сравнения (относительный путь)
        rel_path = file_path.relative_to(html_dir)
        normalized_header = normalize_paths(header, file_path)
        headers[str(rel_path)] = normalized_header

        print(f"[ОК] Обработан файл: {rel_path}")

    # Проверяем идентичность
    first_header = None
    first_file = None

    for file_path, header in headers.items():
        if first_header is None:
            first_header = header
            first_file = file_path
            continue

        if header != first_header:
            print(f"\n[ДЕТАЛЬНО] Различия в файле {file_path}:")
            print("Эталонная шапка:")
            print(first_header[:200] + "..." if len(first_header) > 200 else first_header)
            print("\nШапка файла:")
            print(header[:200] + "..." if len(header) > 200 else header)
            print("-" * 60)
            inconsistencies.append((file_path, first_file))

    if inconsistencies:
        print(f"\n[ОШИБКА] Найдены различия в шапках ({len(inconsistencies)} файлов):")
        for inconsistent_file, reference_file in inconsistencies:
            print(f"  Различия в файле: {inconsistent_file}")
            print(f"  Сравнивать с: {reference_file}")
    else:
        print(f"\n[УСПЕХ] Все шапки идентичны! Проведено {len(headers)} файлов.")

    return len(inconsistencies) == 0

if __name__ == "__main__":
    print("Проверка идентичности шапок HTML файлов...")
    print("=" * 60)

    success = check_headers_consistency()

    print("=" * 60)
    if success:
        print("[УСПЕХ] Проверка завершена успешно - все шапки одинаковые!")
    else:
        print("[ВНИМАНИЕ] Проверка выявила различия в шапках файлов.")
        print("Необходимо исправить различия для единообразия.")
