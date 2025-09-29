# Публикация на GitHub (Windows PowerShell)

## Предварительно
- Зарегистрируйте аккаунт на GitHub
- Установите Git for Windows
- Создайте пустой репозиторий на GitHub, например: `wiki-instruction`

## Команды (выполните в папке проекта)
```powershell
# 1) Инициализация репозитория
git init

# 2) Конфигурация имени и почты (один раз на компьютере)
# Замените на свои данные
git config --global user.name "Ваше Имя"
git config --global user.email "you@example.com"

# 3) Добавление файлов и первый коммит
git add .
git commit -m "Initial commit: wiki instruction"

# 4) Привязка к удалённому репозиторию
# Замените USERNAME на ваш логин
# Если у вас main не по умолчанию, создайте: git branch -M main
git branch -M main
git remote add origin https://github.com/USERNAME/wiki-instruction.git

# 5) Публикация
git push -u origin main
```

## Советы
- Если включена двухфакторная аутентификация, используйте Personal Access Token вместо пароля.
- Проверьте, что `README.md` корректно отображается на странице репозитория.
- Добавляйте скриншоты в папку `screenshots/` (PNG/JPG). Исходники редакторов игнорируются.
- Для совместной работы смотрите `CONTRIBUTING.md`.

## Обновления
```powershell
# После новых изменений
git add .
git commit -m "Update guides"
git push
```
