import subprocess
report = open('wifi.txt', 'w')
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
wifis = [line.split(':')[1][1:-1] for line in data if "All User Profile" in line]
for wifi in wifis:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('utf-8').split('\n')
    results = [line.split(':')[1][1:-1] for line in results if "Key Content" in line]
    try:
        report.write(f'Name: {wifi}, Password: {results[0]}')
    except IndexError:
        report.write(f'Name: {wifi}, Password: Cannot be read!')

report.write(wifis)
report.close()