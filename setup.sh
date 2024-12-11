#!/bin/bash

# Проверка на root права
if [ "$EUID" -ne 0 ]; then 
    echo "❌ Этот скрипт должен быть запущен с правами root"
    echo "Используйте: sudo bash setup.sh"
    exit 1
fi

echo "🚀 Начинаем установку..."

# Устанавливаем необходимые пакеты
echo "📦 Установка необходимых пакетов..."
apt update
apt install -y software-properties-common

# Добавляем репозиторий deadsnakes
echo "📥 Добавление репозитория Python..."
add-apt-repository -y ppa:deadsnakes/ppa
apt update

# Устанавливаем Python 3.11
echo "🐍 Установка Python 3.11..."
apt install -y python3.11 python3.11-venv

# Получаем имя пользователя, от которого был выполнен sudo
SUDO_USER=${SUDO_USER:-$(whoami)}
USER_HOME=$(eval echo ~$SUDO_USER)

# Переходим в директорию проекта
cd NIVEAbot

# Проверяем текущую директорию на наличие venv
if [ -d "venv" ]; then
    echo "🗑️ Удаление старого виртуального окружения..."
    rm -rf venv
fi

# Создаем новое виртуальное окружение
echo "🌟 Создание нового виртуального окружения..."
python3.11 -m venv venv

# Устанавливаем правильные права на директорию venv
chown -R $SUDO_USER:$SUDO_USER venv

# Активируем виртуальное окружение и устанавливаем зависимости
echo "📚 Установка зависимостей..."
su - $SUDO_USER -c "cd $(pwd) && source venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt"

# Создаем скрипт для запуска бота
echo "📝 Создание скрипта запуска..."
cat > start_bot.sh << 'EOF'
#!/bin/bash
source venv/bin/activate
python nevie.py
EOF

# Делаем скрипт запуска исполняемым и устанавливаем правильные права
chmod +x start_bot.sh
chown $SUDO_USER:$SUDO_USER start_bot.sh

pip install -r requirements.txt

echo "✅ Установка завершена!"
echo "🤖 Чтобы запустить бота, выполните: ./start_bot.sh" 
