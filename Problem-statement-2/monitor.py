import psutil
import datetime

# --- Thresholds ---
CPU_THRESHOLD = 80.0  # percent
MEMORY_THRESHOLD = 80.0 # percent
DISK_THRESHOLD = 90.0   # percent

def check_system_health():
    """Monitors CPU, memory, and disk usage and prints alerts if thresholds are exceeded."""
    
    print("-" * 40)
    print(f"System Health Report at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 40)
    
    # 1. Check CPU Usage
    # interval=1 means it's a non-blocking comparison over 1 second
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")
    if cpu_usage > CPU_THRESHOLD:
        print(f"  🚨 ALERT: CPU usage ({cpu_usage}%) exceeds threshold of {CPU_THRESHOLD}%.")

    # 2. Check Memory Usage
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    print(f"Memory Usage: {memory_usage}%")
    if memory_usage > MEMORY_THRESHOLD:
        print(f"  🚨 ALERT: Memory usage ({memory_usage}%) exceeds threshold of {MEMORY_THRESHOLD}%.")

    # 3. Check Disk Usage
    disk = psutil.disk_usage('/') # '/' for the root partition
    disk_usage = disk.percent
    print(f"Disk Usage (Root): {disk_usage}%")
    if disk_usage > DISK_THRESHOLD:
        print(f"  🚨 ALERT: Disk space usage ({disk_usage}%) exceeds threshold of {DISK_THRESHOLD}%.")

    # 4. Count Running Processes
    process_count = len(psutil.pids())
    print(f"Running Processes: {process_count}")

    print("-" * 40)


if __name__ == "__main__":
    check_system_health()