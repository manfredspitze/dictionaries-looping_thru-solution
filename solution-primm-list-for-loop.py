# PRIMM List & For Loop Activity
# Solution


# Import random module for the Bonus Challenge below
import random

candy_list = ["Snickers", "Twix", "M&M's", "Starburst", "Lollipop"]
total_candy = 0

# Count the total number of candies
for candy in candy_list:
    total_candy += 1

# Calculate the number of candies for each person
candies_per_person = total_candy // 2

print("Total number of candies:", total_candy)
print("Each person gets:", candies_per_person, "candies")


# Make Activity
# Spider Rings List

# Add ring colors to a list
spider_rings = ['black', 'green', 'orange']

# Use loop to move through the list from beginning to end
for spider_ring in spider_rings:
    print(f'The color of this spider ring is {spider_ring}.')

# Bonus Challenge
rings_received = int(input("How many spider rings did you collect on Halloween? (Example: 3)\n"))

my_spider_rings = []
colors = ['black', 'green', 'orange']

for my_spider_ring in range(rings_received):
    print(f'This spider ring is colored {random.choice(colors)}.')