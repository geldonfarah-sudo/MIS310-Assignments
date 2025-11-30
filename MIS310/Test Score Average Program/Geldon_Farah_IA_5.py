def get_average():
    test1 = float(input("enter score for test 1: "))
    test2 = float(input("enter score for test 2: "))
    test3 = float(input("enter score for test 3: "))
    average = (test1 + test2 + test3) / 3
    return average

def check_average(avg):
    print(f"your average is {avg:.2f}")
    if avg > 95:
        print("Congratulations! You did great!")
    elif 85 <= avg <= 95:
        print("You did great, but did not reach the Top High.")
    elif 70 <= avg <= 84:
        print("Good effort, but you could do better.")
    else:
        print("You need to study harder next time.")

def main():
    avg = get_average()
    check_average(avg)

if __name__ == "__main__":
    main()
