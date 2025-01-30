"""
File: weather_master.py
Name: Jennifer Li
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

TEMP_EXIT = -100  # The number the user inputs to stop entering new temperatures


def main():
    """
    Write a program to process weather data,
    and for all the input data, calculate the following four values:
    What is the highest temperature?
    What is the lowest temperature?
    What is the average temperature?
    How many days have a "low temperature warning" (below 16 degrees, but not including 16)?
    Your program will repeatedly ask the user to enter an integer.
    If the user wants to exit the program, they can simply enter -100.
    """
    weather()


def weather():
    print("stancode\"weather master 4.0\" !")
    temperature = int(input("Enter a temperature (or " + str(TEMP_EXIT) + " to exit): "))

    if temperature == TEMP_EXIT:
        print('No temperatures were entered.')
    else:
        # Initial values for the Weather Master 4.0
        max_temp = temperature
        min_temp = temperature
        days = 1  # Count how many days there are and will be used to calculate the average temperature
        total_temp = temperature

        # Check if the first temperature is a "cold day"
        if temperature < 16:
            cold_day = 1
        else:
            cold_day = 0

        if temperature > 30:
            hot_day = 1
        else:
            hot_day = 0

        while temperature != TEMP_EXIT:
            temperature = int(input("Enter a temperature (or " + str(TEMP_EXIT) + " to exit): "))
            if temperature == TEMP_EXIT:
                break
            else:
                if temperature > max_temp:  # Update max_temp when the input temperature is higher than the original value
                    max_temp = temperature
                if temperature < min_temp:  # Update min_temp when the input temperature is lower than the original value
                    min_temp = temperature

                days += 1  # Update days
                total_temp += temperature  # Update total temperature
                if temperature < 16:  # Update cold days
                    cold_day += 1
                if temperature > 16:  # Update hot days
                    hot_day += 1
        # Show the results
        print('Highest temperature = ' + str(max_temp))
        print('Lowest temperature = ' + str(min_temp))
        print('Average = ' + str(total_temp / days))
        print(str(cold_day) + ' cold day(s)')
        print(str(hot_day) + ' hot day(s)')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
