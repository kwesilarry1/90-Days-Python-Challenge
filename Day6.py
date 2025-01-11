#Program that calculates the sum and average of a given numbers
def calculate_sum_and_average(numbers):
    if not numbers:
        print("The list is empty.")
        return
    #calculating sum and average
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    
    #Printing sum and average
    print(f"Sum: {total_sum}")
    print(f"Average: {average}")

#Getting User input
user_input = input("Enter numbers separated by spaces: ")
numbers_list = [float(num) for num in user_input.split()]

calculate_sum_and_average(numbers_list)
