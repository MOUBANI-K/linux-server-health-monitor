import psutil
import platform
import socket
from datetime import datetime

print("=" * 50)
print("SERVER HEALTH CHECK REPORT")
print("=" * 50)
# Hostname
hostname = socket.gethostname()
print(f"Hostname: {hostname}")
# Operating System
os_name = platform.system()
os_version = platform.release()
print(f"OS: {os_name} {os_version}")
# Current Time
print(f"Time: {datetime.now()}")
# CPU Usage
cpu_usage = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu_usage}%")
# Memory Usage
memory = psutil.virtual_memory()
print(f"Memory Usage: {memory.percent}%")
# Disk Usage
disk = psutil.disk_usage('/')
print(f"Disk Usage: {disk.percent}%")
# System Boot Time
boot_time = datetime.fromtimestamp(psutil.boot_time())
print(f"Boot Time: {boot_time}")
print("=" * 50)
# Alert Conditions
if cpu_usage > 80:
 print("ALERT: High CPU Usage!")
if memory.percent > 85:
 print("ALERT: High Memory Usage!")
if disk.percent > 90:
 print("ALERT: Disk Almost Full!")
# Log File Storage
with open("health_log.txt", "a") as file:
 file.write(f"\nTime: {datetime.now()}\n")
 file.write(f"CPU: {cpu_usage}%\n")
 file.write(f"Memory: {memory.percent}%\n")
 file.write(f"Disk: {disk.percent}%\n")

