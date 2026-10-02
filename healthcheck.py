import psutil
import platform
import socket
import logging
import smtplib
import subprocess
from datetime import datetime
from email.message import EmailMessage

# CONFIGURATION


CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 85
DISK_THRESHOLD = 90

SENDER_EMAIL = "your_email@gmail.com"
RECEIVER_EMAIL = "your_email@gmail.com"
EMAIL_PASSWORD = "YOUR_APP_PASSWORD"



# LOGGING CONFIGURATION

logging.basicConfig(
    filename="health_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)



# EMAIL FUNCTION

def send_email(subject, body):

    message = EmailMessage()

    message["Subject"] = subject
    message["From"] = SENDER_EMAIL
    message["To"] = RECEIVER_EMAIL

    message.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

        smtp.login(
            SENDER_EMAIL,
            EMAIL_PASSWORD
        )

        smtp.send_message(message)


# SERVER INFORMATION

hostname = socket.gethostname()

os_name = platform.system()
os_version = platform.release()

current_time = datetime.now()

boot_time = datetime.fromtimestamp(
    psutil.boot_time()
)


# RESOURCE MONITORING

cpu_usage = psutil.cpu_percent(interval=1)

memory = psutil.virtual_memory()
memory_usage = memory.percent

disk = psutil.disk_usage("/")
disk_usage = disk.percent

# DISPLAY REPORT

print("=" * 50)
print("SERVER HEALTH CHECK REPORT")
print("=" * 50)

print(f"Hostname: {hostname}")
print(f"OS: {os_name} {os_version}")
print(f"Time: {current_time}")
print(f"CPU Usage: {cpu_usage}%")
print(f"Memory Usage: {memory_usage}%")
print(f"Disk Usage: {disk_usage}%")
print(f"Boot Time: {boot_time}")

print("=" * 50)

# ALERT HANDLING

if cpu_usage > CPU_THRESHOLD:

    message = (
        f"Server: {hostname}\n"
        f"CPU Usage: {cpu_usage}%\n"
        f"Threshold: {CPU_THRESHOLD}%\n"
        f"Time: {current_time}\n\n"
        "Action: Investigate high CPU consuming processes."
    )

    print(" ALERT: High CPU Usage!")

    logging.critical(
        f"High CPU Usage: {cpu_usage}%"
    )

    send_email(
        " CRITICAL: High CPU Usage",
        message
    )


if memory_usage > MEMORY_THRESHOLD:

    message = (
        f"Server: {hostname}\n"
        f"Memory Usage: {memory_usage}%\n"
        f"Threshold: {MEMORY_THRESHOLD}%\n"
        f"Time: {current_time}\n\n"
        "Action: Investigate memory-consuming processes."
    )

    print(" ALERT: High Memory Usage!")

    logging.critical(
        f"High Memory Usage: {memory_usage}%"
    )

    send_email(
        " CRITICAL: High Memory Usage",
        message
    )


if disk_usage > DISK_THRESHOLD:

    message = (
        f"Server: {hostname}\n"
        f"Disk Usage: {disk_usage}%\n"
        f"Threshold: {DISK_THRESHOLD}%\n"
        f"Time: {current_time}\n\n"
        "Action: Check disk usage and remove unnecessary files."
    )

    print(" ALERT: Disk Almost Full!")

    logging.critical(
        f"High Disk Usage: {disk_usage}%"
    )

    send_email(
        " CRITICAL: Disk Usage High",
        message
    )


logging.info(
    f"Health check completed | "
    f"CPU={cpu_usage}% | "
    f"Memory={memory_usage}% | "
    f"Disk={disk_usage}%"
)

def check_apache():

    result = subprocess.run(
        ["systemctl", "is-active", "--quiet", "apache2"]
    )

    if result.returncode != 0:
        print("CRITICAL: Apache is down")
        logging.critical("Apache service is down")

        send_email(
            "CRITICAL: Apache Down",
            "Apache service is not running."
        )
