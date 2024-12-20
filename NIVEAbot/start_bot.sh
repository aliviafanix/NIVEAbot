#!/bin/bash

# Цвета для вывода
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Функция очистки экрана
clear_screen() {
    printf "\033[2J\033[H"
}

# Функция анимации сердца
animate_heart() {
    local colors=("$RED" "$YELLOW" "$GREEN" "$BLUE" "$PURPLE" "$CYAN")
    local heart=(
        " .d88b.d88b. "
        "88888888888 "
        " 'Y8888888Y' "
        "   'Y888Y'   "
        "     'Y'     "
    )
    
    for ((j=0; j<3; j++)); do
        for ((i=0; i<${#colors[@]}; i++)); do
            clear_screen
            for line in "${heart[@]}"; do
                echo -e "${colors[$i]}$line${NC}"
            done
            sleep 0.2
        done
    done
}

# Функция анимации логотипа
animate_logo() {
    local logos=(
        "███╗   ██╗███████╗██╗   ██╗██╗███████╗"
        "████╗  ██║██╔════╝██║   ██║██║██╔════╝"
        "██╔██╗ ██║█████╗  ██║   ██║██║█████╗  "
        "██║╚██╗██║██╔══╝  ╚██╗ ██╔╝██║██╔══╝  "
        "██║ ╚████║███████╗ ╚████╔╝ ██║███████╗"
        "╚═╝  ╚═══╝╚══════╝  ╚═══╝  ╚═╝╚══════╝"
    )
    
    clear_screen
    # Первая анимация - появление построчно
    for ((i=0; i<${#logos[@]}; i++)); do
        case $i in
            0) color=$BLUE;;
            1) color=$CYAN;;
            2) color=$GREEN;;
            3) color=$YELLOW;;
            4) color=$PURPLE;;
            5) color=$RED;;
        esac
        echo -e "${color}${logos[$i]}${NC}"
        sleep 0.1
    done
    
    # Бесконечная анимация с эффектом бегущей волны
    while true; do
        for ((wave=0; wave<${#logos[@]}*2; wave++)); do
            clear_screen
            for ((i=0; i<${#logos[@]}; i++)); do
                if [ $((wave-i)) -ge 0 ] && [ $((wave-i)) -lt 6 ]; then
                    case $((wave-i)) in
                        0) color=$BLUE;;
                        1) color=$CYAN;;
                        2) color=$GREEN;;
                        3) color=$YELLOW;;
                        4) color=$PURPLE;;
                        5) color=$RED;;
                    esac
                else
                    color=$BLUE
                fi
                echo -e "${color}${logos[$i]}${NC}"
            done
            sleep 0.1
        done
        # Анимация в обратном направлении
        for ((wave=${#logos[@]}*2; wave>=0; wave--)); do
            clear_screen
            for ((i=0; i<${#logos[@]}; i++)); do
                if [ $((wave-i)) -ge 0 ] && [ $((wave-i)) -lt 6 ]; then
                    case $((wave-i)) in
                        0) color=$BLUE;;
                        1) color=$CYAN;;
                        2) color=$GREEN;;
                        3) color=$YELLOW;;
                        4) color=$PURPLE;;
                        5) color=$RED;;
                    esac
                else
                    color=$BLUE
                fi
                echo -e "${color}${logos[$i]}${NC}"
            done
            sleep 0.1
        done
    done
}

# Функция проверки и убийства старого процесса
kill_old_process() {
    local old_pid=$(pgrep -f "python3.*nevie.py")
    if [ ! -z "$old_pid" ]; then
        echo -e "${YELLOW}[!] Обнаружен запущенный бот (PID: $old_pid)${NC}"
        echo -e "${YELLOW}[*] Останавливаю старый процесс...${NC}"
        kill $old_pid 2>/dev/null
        sleep 2
        # Проверяем, точно ли процесс остановлен
        if ps -p $old_pid > /dev/null; then
            echo -e "${RED}[!] Не удалось остановить старый процесс. Использую force-kill...${NC}"
            kill -9 $old_pid 2>/dev/null
            sleep 1
        fi
        echo -e "${GREEN}[*] Старый процесс успешно остановлен${NC}"
    fi
}

# Основной скрипт
clear_screen

# Убиваем старый процесс, если он существует
kill_old_process

# Запускаем анимацию логотипа в фоне
animate_logo &
LOGO_PID=$!

# Перемещаем курсор ниже логотипа для вывода информации
printf "\033[8;0H"

# Информация о запуске
echo -e "${YELLOW}[*] Инициализация бота...${NC}"
echo -e "${GREEN}[*] Активация виртуального окружения...${NC}"
source /home/aliwka/nevia/NIVEAbot/venv_new/bin/activate

echo -e "${CYAN}[*] Запуск бота...${NC}"
# Перемещаем курсор ниже для вывода логов Python
printf "\033[12;0H"
python3 /home/aliwka/nevia/NIVEAbot/nevie.py

# Обработка выхода
trap 'echo -e "${YELLOW}[*] Завершение работы бота...${NC}"; kill $(jobs -p)' EXIT