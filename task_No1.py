def mutate_string(string, position, character):
    """
    Changes the character at the given position in the string and returns the modified string.
    """
    # Convert the string to a list of characters
    string_list = list(string)
    
    # Replace the character at the given position with the new character
    string_list[position] = character
    
    # Convert the list of characters back to a string
    modified_string = ''.join(string_list)
    
    return modified_string

def main():
    # Read the input string, position, and character
    string = input().strip()
    position, character = input().strip().split()
    position = int(position)

    # Call the mutate_string function to get the modified string
    modified_string = mutate_string(string, position, character)

    # Print the modified string
    print(modified_string)

if __name__ == '__main__':
    main()
