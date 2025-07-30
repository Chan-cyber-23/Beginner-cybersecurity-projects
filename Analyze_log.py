import csv

with open('logins.csv', 'r') as file:
    reader = csv.DictReader(file)
    failed_count = 0
    for row in reader:
        if row['status'] == 'failed':
            failed_count += 1
    print(f"Failed logins: {failed_count}")
