def count_characters(text):
  
    char_count = {}
    
    
    for char in text:
        
        if char.isalnum():
            char_count[char] = char_count.get(char, 0) + 1
            
    
    sorted_counts = dict(sorted(char_count.items(), key=lambda item: (-item[1], item[0])))
    
    return sorted_counts


input_text = "Hello, welcome to Cathay 60th year anniversary."

result = count_characters(input_text)
print(result)
