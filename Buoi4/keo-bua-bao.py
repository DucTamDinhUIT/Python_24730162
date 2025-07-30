import random

def get_user_choice():
    print("Chon cua ban:")
    print("1. Keo")
    print("2. Bua")
    print("3. Bao")
    choice = input("Nhap so (1-3): ")
    while choice not in ['1', '2', '3']:
        choice = input("Sai cu phap. Nhap lai (1-3): ")
    return int(choice)

def get_computer_choice():
    return random.randint(1, 3)

def convert_choice(choice):
    return ["Keo", "Bua", "Bao"][choice - 1]

def determine_winner(user, comp):
    if user == comp:
        return "Hoa!"
    elif (user == 1 and comp == 3) or (user == 2 and comp == 1) or (user == 3 and comp == 2):
        return "Ban thang!"
    else:
        return "May thang!"

def play_game():
    user_choice = get_user_choice()
    comp_choice = get_computer_choice()

    print(f"\nBan chon: {convert_choice(user_choice)}")
    print(f"May chon: {convert_choice(comp_choice)}")

    result = determine_winner(user_choice, comp_choice)
    print(f"\nKet qua: {result}")

if __name__ == "__main__":
    while True:
        play_game()
        again = input("\nChoi lai? (y/n): ").lower()
        if again != 'y':
            print("Tam biet!")
            break
