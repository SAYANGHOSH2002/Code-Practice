def count_substring_occurrences(string, substring):
    count = 0
    start_index = 0

    while True:
        # Find the next occurrence of the substring
        next_index = string.find(substring, start_index)

        # If no further occurrence is found, break the loop
        if next_index == -1:
            break

        # Increment the count of occurrences
        count += 1

        # Update the start index for the next search to the next position after the current occurrence
        start_index = next_index + 1

    return count

def game(s):
    cs = s
    done_words = []
    v_count = 0
    c_count = 0
    for i in range(0, len(cs)):
        if cs[i] == 'A' or cs[i] == 'E' or cs[i] == 'I' or cs[i] == 'O' or cs[i] == 'U':
            for j in range(i,len(cs)):
                ms = cs[i:j+1]
                if ms in done_words:
                    continue
                else:
                    done_words.append(ms)
                    v_count = v_count + count_substring_occurrences(s, ms)
                    print("VS: ", ms, "Count: ", v_count)
        else:
            for j in range(i,len(cs)):
                ms = cs[i:j+1]
                #print("CS: ", ms)
                if ms in done_words:
                    continue
                else:
                    done_words.append(ms)
                    c_count = c_count + count_substring_occurrences(s, ms)
                    print("VS: ", ms, "Count: ", c_count)

    print("\nPlayer 1 Score: " , c_count , "\nPlayer 2 Score: " , v_count)
    if v_count > c_count:
        print("\nPlayer 2 Wins !!")
    elif c_count > v_count:
        print("\nPlayer 1 Wins !!")
    else:
        print("\nNobody Wins !!")            


s = input("Enter the String in CAPS only: ")
game(s)