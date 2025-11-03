import psutil
import os

def get_temp():
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            temp = int(f.read()) / 1000
            return f"{temp:.1f}°C"
    except FileNotFoundError:
        return "N/A"

def get_info():
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    temp = get_temp()

    return (
        f"CPU Temp: {temp}   |  CPU Usage: {cpu}%\n"
        f"RAM: {mem.used // (1024*1024)}MB / {mem.total // (1024*1024)}MB   "
        f"|  Disk: {disk.used // (1024*1024*1024)}GB / {disk.total // (1024*1024*1024)}GB"
    )
