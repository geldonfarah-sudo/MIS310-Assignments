State Population Lookup Program
Overview

This program allows the user to enter a U.S. state code and retrieves the population value from a predefined dictionary. If the user enters an invalid code, the program reports the error, displays all valid options, and asks whether the user wants to try again.

How It Works

A dictionary stores state codes and their populations. The program waits for user input, normalizes it to uppercase, and checks if the code exists in the dictionary.

If it exists, the population is displayed and the program ends.

If not, the user is shown all valid codes and asked whether they want to retry.
Valid codes are extracted into a list and used to generate the error message.
