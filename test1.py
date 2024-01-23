"""Testing module with basic operation"""

def sub(num_list: list[int]) -> int:
    total = 0
    for num in num_list:
        total = total - num
    return total

def divi(num_list: list[int]) -> int:
    total = 0
    for num in num_list:
        total = total / num
    return total

def multi(num_list: list[int]) -> int:
    total = 0
    for num in num_list:
        total = total * num
    return total

  
def add(num_list: list[int]) -> int:
    total = 0
    for num in num_list:
        total = total + num
    return total

def user_inputs() -> list[int]:
    total_num = int(input('how many number you wanna calculate? '))
    num_list: list[int] = []
    
    for i in range(0, total_num):
        number = int(input(f"num {i+1}: "))
        num_list.append(number)
    
    return num_list

def main():
    

    while True:
        print("choose any input listed below"
    "\n A: Addition",
    "\n S: Subtraction",
    "\n M: Multiplication",
    "\n D: Dividion"
    "\n Q for Quiting"
    )
        
        operation = input("Your option? ")
            
        
        if operation == 'a' or operation == 'A':
            num_list = user_inputs()
            result = add(num_list)
            print(result)
        elif operation == 's' or operation == 'S':
            num_list = user_inputs()
            result = sub(num_list)
            print(result)
        elif operation == 'm' or operation == 'M':
            num_list = user_inputs()
            result = multi(num_list)
            print(result)
        elif operation == 'd' or operation == 'D':
            num_list = user_inputs()
            result = divi(num_list)
            print(result)    
        elif operation == 'q' or operation == 'Q':
            print("Thank you")
            break
        else:
            print("Wrong input, try again!")
            continue
        

if __name__ == "__main__":
    main() 