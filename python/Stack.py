# def push(n, top, arr):
    
#     #global arr
#     if top == n-1:
#         print("Stack Overflow")
        
#     else:
#         num = int(input("Enter the number: "))
#         top += 1
#         arr[top] = num
#         for i in range (0, top):
#             print(arr[i])

#     return arr

# def pop(top, arr):
    
#     #global arr
#     if top == -1:
#         print("Stack Underflow")
        
#     else:
#         top -= 1

#     return arr 

# def display(top, arr):
    
#     #global arr
#     for i in range(0, top):
#         print(arr[i], end = "")

if __name__ == "__main__":

    n = int(input("Enter the stack size: "))
    arr = [0 for i in range (n)]
    top = -1

    while True:

        print("\n1. Push 2. Pop 3. Display 4. Exit")
        c = int(input())

        if c == 1:
            #arr = push(n, top, arr)
            if top == n-1:
                print("Stack Overflow")
        
            else:
                num = int(input("Enter the number: "))
                top += 1
                arr[top] = num
                for i in range (0, top+1):
                    print(arr[i], end = " ")

        elif c == 2:
            #arr = pop(top, arr)
            if top == -1:
                print("Stack Underflow")
        
            else:
                top -= 1

        elif c == 3:
            #display(top, arr)
            for i in range(0, top+1):
                print(arr[i], end = " ")

        elif c == 4:
            break

        else:
            print("Invalid argument try agan")
