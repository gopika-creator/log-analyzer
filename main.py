from collections import Counter

print("=" * 50)
print("LOG ANALYZER")
print("=" * 50)

log_file = input("Enter log file name: ")

try:
    with open(log_file, "r") as file:
        logs = file.readlines()

    total_logs = len(logs)

    failed_logins = sum(
        1 for line in logs if "FAILED LOGIN" in line.upper()
    )

    errors = sum(
        1 for line in logs if "ERROR" in line.upper()
    )

    ips = []

    for line in logs:
        words = line.split()
        for word in words:
            if word.count(".") == 3:
                ips.append(word)

    ip_count = Counter(ips)

    print("\nAnalysis Results")
    print("-" * 30)
    print(f"Total Log Entries: {total_logs}")
    print(f"Failed Logins: {failed_logins}")
    print(f"Errors Found: {errors}")

    print("\nTop IP Addresses:")
    for ip, count in ip_count.most_common(5):
        print(f"{ip} -> {count} entries")

except FileNotFoundError:
    print("Log file not found.")
