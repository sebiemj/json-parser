import json
import csv

with open('output.json', 'r') as file:
    data = json.load(file)
    
print('Raw data:', data)


for person in data:
    print(f"Name: {person['name']}, Age: {person['age']}, City: {person['city']}")
    
filtered = [p for p in data if p['age'] > 25]

for person in filtered:
    print(f"{person['name']} is older than 25")
    
for person in data:
    city = person.get('city', 'Unknown')
    print(f"{person['name']} lives in {city}")


with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['name', 'age', 'city'])
    writer.writeheader()
    writer.writerows(data)

print("Data exported to output.csv")