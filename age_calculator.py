from datetime import datetime

def calculate_age(birth_date):
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def main():
    birth_date_str = input("Enter your birth date (YYYY-MM-DD): ")
    birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
    age = calculate_age(birth_date)
    print(f"You are {age} years old.")

if __name__ == "__main__":
    main()
