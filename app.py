import psutil

def check_health(cpu, memory, disk):
    if cpu > 80 or memory > 80 or disk > 80:
        return "WARNING"
    return "HEALTHY"

def main():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    status = check_health(cpu, memory, disk)

    print("System Health")
    print("-------------")
    print(f"CPU Usage    : {cpu}%")
    print(f"Memory Usage : {memory}%")
    print(f"Disk Usage   : {disk}%")
    print(f"\nStatus       : {status}")

if __name__ == "__main__":
    main()