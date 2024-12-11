#!/bin/bash

# Цвета для вывода
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${GREEN}🚀 Запускаем NIVEAbot в Termux...${NC}"

# Проверка наличия Ubuntu
if ! command -v ./start-ubuntu22.sh &> /dev/null; then
    echo -e "${RED}❌ Ошибка: start-ubuntu22.sh не найден!${NC}"
    echo -e "${YELLOW}ℹ️ Убедитесь, что скрипт находится в текущей директории${NC}"
    exit 1
fi

# Проверка наличия директории бота
if [ ! -d "NIVEAbot" ]; then
    echo -e "${RED}❌ Ошибка: Директория NIVEAbot не найдена!${NC}"
    echo -e "${YELLOW}ℹ️ Убедитесь, что бот установлен корректно${NC}"
    exit 1
fi

echo -e "${YELLOW}⏳ Запуск Ubuntu...${NC}"
sleep 3
./start-ubuntu22.sh

echo -e "${YELLOW}⏳ Ожидание инициализации системы...${NC}"
sleep 5

echo -e "${YELLOW}📂 Переход в директорию бота...${NC}"
cd NIVEAbot || {
    echo -e "${RED}❌ Ошибка: Не удалось перейти в директорию NIVEAbot${NC}"
    exit 1
}
sleep 2

# Проверка и создание start_bot.sh если его нет
if [ ! -f "start_bot.sh" ]; then
    echo -e "${BLUE}📝 Создаю start_bot.sh...${NC}"
    cat > start_bot.sh << 'EOF'
#!/bin/bash

# Активация виртуального окружения
if [ -d "venv" ]; then
    source venv/bin/activate
else
    echo "❌ Виртуальное окружение не найдено!"
    echo "🔄 Запускаю setup.sh для настройки..."
    ./setup.sh
    source venv/bin/activate
fi

# Запуск бота
echo "🤖 Запуск NIVEAbot..."
nevie.py
EOF
    
    # Делаем скрипт исполняемым
    chmod +x start_bot.sh
    echo -e "${GREEN}✅ start_bot.sh успешно создан!${NC}"
fi

echo -e "${GREEN}🤖 Запуск бота...${NC}"
./start_bot.sh