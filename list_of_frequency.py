def list_of_frequency(input_string):
    # Step 1: Create a dictionary to store frequencies of each character
    frequency_dict = {}
    for char in input_string:
        # Count only alphabetical characters
        if char.isalpha():
            char = char.lower()  # Convert to lowercase to make it case-insensitive
            frequency_dict[char] = frequency_dict.get(char, 0) + 1
    
    # Step 2: Sort characters by frequency in non-increasing order
    sorted_chars = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)
    
    # Step 3: Print characters and their frequencies
    for char, freq in sorted_chars:
        print(f"{char}: {freq}")

# Example usage
input_string = input("Enter a string: ")
list_of_frequency(input_string)
