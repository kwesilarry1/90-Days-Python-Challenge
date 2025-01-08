#program that asks user's name and age, prints greeting message with name and birth year
def main():
    # Get current year
    from datetime import datetime
    current_year = datetime.now().year
    
    # Get user input
    name = input("What is your name?")
    age = int(input("How old are you?"))
    
    # Calculate the birth year
    birth_year = current_year - age
    
    # Print the greeting and birth year
    print(f"Hello, {name}! You were born in {birth_year}.")

if __name__ == "__main__":
    main()
