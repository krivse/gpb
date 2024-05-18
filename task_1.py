# Задание 1
# 1. Реализовать сбор уникальных записей
# 2. Случается, что под одиннаковым id присутствуют разные данные - собрать отдельно такие записи

import csv

# Open the CSV file
with open('file.csv', 'r') as file:
    # Create a dictionary to store unique records
    unique_records = {}
    # Create a dictionary to store records with duplicate IDs
    duplicate_records = {}

    # Read the CSV file
    reader = csv.DictReader(file, delimiter='|')
    for row in reader:
        id = row['id']
        if id in unique_records:
            # If the ID already exists, add the record to duplicate_records
            if id not in duplicate_records:
                duplicate_records[id] = []
            duplicate_records[id].append(row)
        else:
            # If the ID is unique, add the record to unique_records
            unique_records[id] = row
    # Close the CSV file
    file.close()

    # Remove first duplicate record from unique_records
    for key in duplicate_records:
        if key in unique_records:
            record = unique_records.pop(key)
            duplicate_records[key].append(record)


# Print the unique records
print("Unique Records:")
for id, record in unique_records.items():
    print(id, record)

# Print the duplicate records
print("\nDuplicate Records:")
for id, records in duplicate_records.items():
    print(id)
    for record in records:
        print(record)
