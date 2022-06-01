#print("Hello World")

# 5 + 2 * 3
# 8 // 5 - 3
# 8 + 22 * 2 - 4
# 16 - 3 / 2 + 7 - 1
# 3 ** 3 % 5
# 5 + 9 * 3 / 2 - 4
# (5 + 2) * 3
# (8 // 5) - 3
# 8 + (22 * (2 - 4))
# 16 - 3 / (2 + 7) - 1
# 3 ** (3 % 5)
# 5 + (9 * 3 / 2 - 4) and 5 + (9 * 3 / (2 - 4))

#counties = ["Arapahoe","Denver","Jefferson"]
#counties = ("Arapahoe","Denver","Jefferson")

#Example of how to print out
# How many votes did you get?
# my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
# total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")

#Example: of if statement
# counties = ["Arapahoe","Denver","Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])

# Example: of if else statements
# temperature = int(input("What is the temperature outside? "))
# if temperature > 80:
#     print("Turn on the AC.")
# else:
#     print("Open the windows.")

# What is the score?
#score = int(input("What is your test score? "))

# Determine the grade.
# if score >= 90:
#     print('Your grade is an A.')
# elif score >= 80:
#     print('Your grade is a B.')
# elif score >= 70:
#     print('Your grade is a C.')
# elif score >= 60:
#     print('Your grade is a D.')
# else:
#     print('Your grade is an F.')

# counties = ["Arapahoe","Denver","Jefferson"]
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not the list of counties.")

# counties = ["Arapahoe","Denver","Jefferson"]
# if "Arapahoe" in counties or "El Paso" in counties:
#     print("Arapahoe and El Paso are in the list of counties.")
# else:
#     print("Arapahoe or El Paso is not in the list of counties.")

# x = 0
# while x <= 5:
#     print(x)
#     x = x + 1

# count = 7

# while count < 1:

#     print("Hello World")

# counties = ["Arapahoe","Denver","Jefferson"]

# for county in counties:
#     print(county)

# numbers = [0, 1, 2, 3, 4]
# for num in numbers:
#     print(num)

# for num in range(5):
#     print(num)

# counties_tuples = ("Arapahoe","Denver","Jefferson")

# for i in range(len(counties_tuples)):
#       print(counties_tuples[i])

# for county in counties_tuples:
#       print(county)

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county in counties_dict:
#     print(county)

# for county in counties_dict.keys():
#     print(county)



# for voters in counties_dict.values():
#     print(voters)

# for county in counties_dict:
#     print(counties_dict[county])

# for county, voters in counties_dict.items():
#     print(county, "county has",voters, "registered voters.")

# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     print(county_dict)

# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)

#How would you retrieve the number of registered voters from each dictionary?
# for county_dict in voting_data:

#      print(county_dict['registered_voters'])

#If we only want to print the county name from each dictionary
# for county_dict in voting_data:
#     print(county_dict['county'])

#Calculate the percentage of votes using f-string literals
# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")

#Easier read Calculate the percentage of votes using f-string literals
# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#F-String with dictionairies
# counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
# for county, voters in counties_dict.items():
#      print(county + " county has " + str(voters) + " registered voters.")

# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters.")
    
#Multiline f-String
# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes} number of votes. "
#     f"The total number of votes in the election was {total_votes}. "
#     f"You received {candidate_votes / total_votes * 100}% of the total votes.")

# print(message_to_candidate)

#Formating Floating-Point Decimals
# f'{value:{width}.{precision}}'
# Formating two decimal places we would put .2f
# When adding a thousands separator we would put
# f'{value:{width},.{precision}}'

# Import the datetime class from the datetime module.
# import datetime
# Use the now() attribute on the datetime class to get the present time.
# now = datetime.datetime.now()
# Print the present time.
# print("The time right now is ", now)

# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each each candidate won
# 5. The winner of the election based on popular vote.

# import csv
# dir(csv)

# Assign a variable for the file to load and the path.
# file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file.
# election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
# election_data.close()

# Open the election results and read the file
# with open(file_to_load) as election_data:

     # To do: perform analysis.
    #  print(election_data)
# import os
# dir(os)
# print(dir(os))