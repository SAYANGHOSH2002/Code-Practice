if __name__ == "__main__":

    n = int(input("Enter the queue size: "))
    arr = [0 for i in range (n)]
    front = -1
    rear = -1

    while True:

        print("\n1. Enqueue 2. Dequeue 3. Display 4. Exit")
        c = int(input())

        if c == 1:
            #arr = push(n, top, arr)
            if front == -1 and rear == -1:
                num = int(input("Enter the number: "))
                front = 0
                rear = 0
                arr[rear] = num

            elif front == n-1:
                print("Queue limit reached")
        
            else:
                num = int(input("Enter the number: "))
                rear += 1
                arr[rear] = num

        elif c == 2:
            #arr = pop(top, arr)
            if rear == -1:
                print("Queue is empty")
        
            else:
                front += 1

        elif c == 3:
            #display(top, arr)
            if rear == -1:
                print("Queue is empty")
                
            for i in range(front, rear+1):
                print(arr[i], end = " ")

        elif c == 4:
            break

        else:
            print("Invalid argument try agan")
