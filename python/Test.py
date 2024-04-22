def get_combinations(string, prefix=''):
    combinations = []
    if len(string) == 0:
        combinations.append(prefix)
    else:
        for i in range(len(string)):
            new_prefix = prefix + string[i]
            remaining = string[:i] + string[i+1:]
            combinations.extend(get_combinations(remaining, new_prefix))
    return combinations

# Example usage:
user_input = input("Enter a string: ")
all_combinations = get_combinations(user_input)
print("All possible combinations:")
# for index, combination in enumerate(all_combinations, start=1):
#     print(f"Combination {index}: {combination}")

for i in all_combinations:
    print(i)
