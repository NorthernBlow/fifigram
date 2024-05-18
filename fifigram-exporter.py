from prometheus_client import start_http_server, Gauge
from systemd import journal
import time
import subprocess
import os

# Создаем метрики
unit_status = Gauge('bot_unit_status', 'Status of bot systemd unit')
cpu_usage = Gauge('bot_cpu_usage', 'CPU usage of bot')

def get_unit_status(unit_name):
    # Проверяем статус юнита
    output = subprocess.check_output(['systemctl', 'is-active', unit_name])
    return output.decode('utf-8').strip()

def get_cpu_usage(pid):
    # Получаем использование CPU процессом
    output = subprocess.check_output(['ps', '-p', str(pid), '-o', '%cpu'])
    return float(output.decode('utf-8').split('n')[1])

def get_bot_pid(unit_name):
    # Получаем PID процесса
    output = subprocess.check_output(['systemctl', 'show', unit_name, '-p', 'MainPID'])
    return int(output.decode('utf-8').split('=')[1])

if __name__ == '__main__':
    # Запускаем HTTP сервер
    start_http_server(8000)
    
    while True:
        # Запрашиваем статус юнита и обновляем метрику
        status = get_unit_status('fifigram.service')
        unit_status.set(1 if status == 'active' else 0)
        
        # Получаем PID бота
        pid = get_bot_pid('fifigram.service')
        
        # Если бот активен, запрашиваем использование CPU и обновляем метрику
        if pid != 0:
            cpu = get_cpu_usage(pid)
            cpu_usage.set(cpu)
        
        time.sleep(1)
