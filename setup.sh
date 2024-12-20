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
dnf update -y
dnf install -y python3 python3-pip git screen

# Получаем имя пользователя, от которого был выполнен sudo
SUDO_USER=${SUDO_USER:-$(whoami)}
USER_HOME=$(eval echo ~$SUDO_USER)

# Создаем необходимые директории
echo "📁 Создание директорий..."
mkdir -p db
chown -R $SUDO_USER:$SUDO_USER db

# Проверяем текущую директорию на наличие venv
if [ -d "venv" ]; then
    echo "🗑️ Удаление старого виртуального окружения..."
    rm -rf venv
fi

# Создаем новое виртуальное окружение
echo "🌟 Создание нового виртуального окружения..."
python3 -m venv venv

# Устанавливаем правильные права на директорию venv
chown -R $SUDO_USER:$SUDO_USER venv

# Активируем виртуальное окружение и устанавливаем зависимости
echo "📚 Установка зависимостей..."
su - $SUDO_USER -c "cd $(pwd) && source venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt"

# Копируем базы данных если они существуют
if [ -f "../db/honey.db" ]; then
    echo "📦 Копирование существующей базы данных..."
    cp ../db/honey.db db/
    chown $SUDO_USER:$SUDO_USER db/honey.db
fi

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

echo "✅ Установка завершена!"
echo "🔧 Не забудьте настроить токен бота в файле nevie.py"
echo "🤖 Чтобы запустить бота, выполните: ./start_bot.sh" 