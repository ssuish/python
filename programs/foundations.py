# Python Foundations

# List
# a simple collection that groups pieces of data together in a certain order
city = ["Tokyo", "Dakar", "Mumbai", "Buenos Aires"]
# print(city[0])

# Dictionary
# stores related information
food = {
    'appetizer': 'hummus'
    }
# print(food["appetizer"])

# Challenge 1
star = ['Sol', 'Alpha Centauri', 'Barnard', 'Wolf 359']
print(star[3])

peaks = {
    'African' : 'Kilimanjaro',
    'Antarctic' : 'Vinson',
    'Australian' : 'Puncak Jaya',
    'Eurasian' : 'Everest',
    'North_American' : 'Denali',
    'Pacific' : 'Mauna Kea',
    'South_American' : 'Aconcagua'
}
print(peaks["Pacific"])

# Iterations
fruits = [
    'apples',
    'bananas',
    'dragon fruit',
    'mangos',
    'nectarines',
    'pears',
]

print("Our fruit selection:")
for i in fruits:
    print(i)