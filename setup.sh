#!/bin/bash

echo "🚀 Начинаем установку..."

# Проверяем и устанавливаем необходимые пакеты
echo "📦 Установка необходимых пакетов..."
sudo apt update
sudo apt install -y software-properties-common

# Добавляем репозиторий deadsnakes
echo "📥 Добавление репозитория Python..."
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt update

# Устанавливаем Python 3.11
echo "🐍 Установка Python 3.11..."
sudo apt install -y python3.11 python3.11-venv

# Проверяем текущую директорию на наличие venv
if [ -d "venv" ]; then
    echo "🗑️ Удаление старого виртуального окружения..."
    rm -rf venv
fi

# Создаем новое виртуальное окружение
echo "🌟 Создание нового виртуального окружения..."
python3.11 -m venv venv

# Активируем виртуальное окружение и устанавливаем зависимости
echo "📚 Установка зависимостей..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Создаем скрипт для запуска бота
echo "📝 Создани�� скрипта запуска..."
cat > start_bot.sh << 'EOF'
#!/bin/bash
source venv/bin/activate
python nevie.py
EOF

# Делаем скрипт запуска исполняемым
chmod +x start_bot.sh

echo "✅ Установка завершена!"
echo "🤖 Чтобы запустить бота, выполните: ./start_bot.sh" 