def generate_sequence(n):
   
    sequence = [0, 1]
    for i in range(2, n):
        next_value = sequence[i - 1] * (sequence[i - 2] + 1)
        sequence.append(next_value)
    return sequence


def print_sequence(n):
    sequence = generate_sequence(n)
    print(f"前 {n} 项: {sequence}")


n = 13
print_sequence(n)

def generate_sequence_until_limit(limit):
    sequence = [0, 1]  
    n = 2  

    while True:
        next_value = sequence[n - 1] * (sequence[n - 2] + 1)
        if next_value >= limit:
            break
        sequence.append(next_value)
        n += 1

    return sequence

def max_value_under_limit(limit):
    sequence = generate_sequence_until_limit(limit)
    
    if not sequence:
        return None, None  

    max_value = max(sequence)
    max_index = sequence.index(max_value) + 1  
    return max_value, max_index


limit = 1000
max_value, max_index = max_value_under_limit(limit)

print(f"小于 {limit} 的最大数为: {max_value}，位于第 {max_index} 项")

