#1 VARIABLES
#task 1.1 -Value of pi and data type

pi = 22 / 7
print(type(pi))

#task 1.2 -Using reserved word as variable
for_ = 4 
print(for_)

#task 1.3  -Store the values in variables
P = 1000
R = 5
T = 3 

Simple_Interest = (P * R * T) / 100

print("Simple Intrest for 3 years is:", Simple_Interest)

#2 NUMBERS

#task 2.1  -Format number using 'o' (octal)
num = 145 
formatted = format(num, 'o')
print("Octal represtentation of 145 is;" , formatted)

#task 2.2 -Pond area and gives Values
radius = 84
pi = 3.14
water_per_sqare_meter = 1.4

area = pi *  (radius ** 2)
total_water = area * water_per_sqare_meter

print(int(total_water))

#task 2.3  -Speed in m/s without decimal
distance =  490
speed = 7
time_seconds = time_minutes = 60 * 7

speed = distance / time_seconds
print(int(speed))

#3 IF condition

#task 3.1  -Function to calculate BMI and determine the category

def calculate_bmi():
    # Get user input for height and weight
    height = float(input("Enter height in meters: "))
    weight = float(input("Enter weight in kilograms: "))
    
    # Calculate BMI
    bmi = weight / (height ** 2)
    
    # Determine BMI category
    if bmi >= 30:
        category = "Obesity"
    elif 25 <= bmi < 30:
        category = "Overweight"
    elif 18.5 <= bmi < 25:
        category = "Normal"
    else:
        category = "Underweight"
    
    # Print the BMI category
    print(f"Output: \"{category}\"")

# Call the function
calculate_bmi()

#task 3.2 -Define the cities for each country
countries = {
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
    "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
    "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
}

# Function to find the country of a given city
def find_country_by_city():
    # Get user input for the city name
    city = input("Enter a city name: ").strip()
    
    # Initialize a variable to track the country
    found_country = None
    
    # Check each country and its cities
    for country, cities in countries.items():
        if city in cities:
            found_country = country
            break
    
    # Print the result
    if found_country:
        print(f"Output: \"{city} is in {found_country}\"")
    else:
        print(f"Output: \"{city} is not in the list of known cities\"")

# Call the function
find_country_by_city()

#task 3.3 -Check cities for each country
def check_same_country(city1, city2):
    # Dictionary mapping cities to their countries
    city_country_map = {
        "Mumbai": "India",
        "Chennai": "India",
        "Delhi": "India",
        "Bangalore": "India",
        "Sydney": "Australia",
        "Melbourne": "Australia",
        "Dubai": "UAE",
        "Abu Dhabi": "UAE",
        "New York": "USA",
        "Los Angeles": "USA",
        "London": "UK",
        "Manchester": "UK"
    }
    
    # Get the countries for the entered cities
    country1 = city_country_map.get(city1)
    country2 = city_country_map.get(city2)
    
    # Check if both cities belong to the same country
    if country1 and country2:
        if country1 == country2:
            return f"Both cities are in {country1}"
        else:
            return "They don't belong to the same country"
    else:
        return "One or both cities are not in the database"

# User input
city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

# Output the result
result = check_same_country(city1, city2)
print(result)

        #5.FILE HANDLING
        #task 5.1 create a dictionary
        # List of friends' names
friends = ["Seema", "kanishka", "yuvraj", "pooja", "monishka"]

# List of tuples containing each name and its length
name_length_tuples = [(name, len(name)) for name in friends]

# Alternatively, you can do:
# name_length_tuples = []
# for name in friends:
#     name_length_tuples.append((name, len(name)))

print("List of friends:", friends)
print("List of name-length tuples:", name_length_tuples)

#task 5.2 Expences
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

# Your partner's expenses
partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

# Calculate total expenses for each
total_your_expenses = sum(your_expenses.values())
total_partner_expenses = sum(partner_expenses.values())

# Print total expenses
print(f"Your total expenses: ${total_your_expenses}")
print(f"Your partner's total expenses: ${total_partner_expenses}")

# Determine who spent more
if total_your_expenses > total_partner_expenses:
    print("You spent more money overall.")
elif total_your_expenses < total_partner_expenses:
    print("Your partner spent more money overall.")
else:
    print("You both spent the same amount of money.")

# Find the category with the most significant difference in spending
significant_difference = {}
for category in your_expenses:
    difference = abs(your_expenses[category] - partner_expenses[category])
    significant_difference[category] = difference

# Find the category with the maximum difference
max_category = max(significant_difference, key=significant_difference.get)
max_difference = significant_difference[max_category]

# Print the category and the difference
print(f"The category with the most significant difference is '{max_category}' with a difference of ${max_difference}.")