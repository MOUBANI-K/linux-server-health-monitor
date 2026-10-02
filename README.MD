# Linux Server Health Monitor

I built this project to practice Linux server monitoring and Python automation.

The idea is simple: instead of manually checking CPU, memory and disk usage, the script checks the server automatically and generates an alert when a resource crosses a defined limit.

I also configured the script to run automatically using a cron job.

## What it checks

The script currently collects:

* Server hostname
* Operating system
* Current date and time
* CPU usage
* Memory usage
* Disk usage
* System boot time

It checks the resource usage against predefined thresholds.

For example:

```text
CPU > 80%       → High CPU alert
Memory > 85%    → High Memory alert
Disk > 90%      → Disk space alert
```

## Alerting

When a threshold is exceeded, the script:

1. Displays an alert on the terminal
2. Records the event in the log file
3. Sends an email notification

Example:

```text
CRITICAL: High CPU Usage

Server: web-server
CPU Usage: 92%
Threshold: 80%

Action: Check processes consuming high CPU.
```

## How I automated it

I used a Linux cron job to run the script every 10 minutes.

My cron configuration:

```bash
*/10 * * * * /usr/bin/python3 /home/zion/server_health_monitor/healthcheck.py
```

I also redirect the script output to a separate cron log so that I can troubleshoot the scheduled execution if something goes wrong.

## Logging

The monitoring results and alerts are stored in a log file.

Example:

```text
2026-10-02 10:30:15 - INFO - Health check completed
2026-10-02 10:40:15 - CRITICAL - High CPU Usage: 91%
```

This makes it easier to look back at previous alerts instead of relying only on the terminal output.

## Technologies used

* Python
* Linux
* psutil
* SMTP
* Cron
* Git/GitHub

## Project files

```text
server_health_monitor/
│
├── healthcheck.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Running the project

Clone the repository:

```bash
git clone <repository-url>
cd server_health_monitor
```

Install the required package:

```bash
pip3 install -r requirements.txt
```

Run the monitoring script:

```bash
python3 healthcheck.py
```

## Current status

The basic monitoring and alerting functionality is working.

### Completed

* [x] CPU monitoring
* [x] Memory monitoring
* [x] Disk monitoring
* [x] Threshold-based alerts
* [x] Log file generation
* [x] Email notification
* [x] Cron automation

### Planned improvements

I plan to extend this project further with:

* [ ] Apache/Nginx service monitoring
* [ ] Recovery alerts when usage returns to normal
* [ ] Warning and critical alert levels
* [ ] AWS CloudWatch integration
* [ ] SNS notifications
* [ ] Prometheus/Grafana monitoring
* [ ] AI-based log analysis

## Why I built this

I started this project as a small Linux health-check script and gradually added automation and alerting.

My next goal is to connect this type of monitoring with AWS and build more DevOps-focused automation around it.
