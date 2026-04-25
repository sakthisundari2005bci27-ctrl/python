if __name__ == '__main__':
    s = input()
    
    # Check if any character is alphanumeric
    print(any(char.isalnum() for char in s))
    
    # Check if any character is alphabetical
    print(any(char.isalpha() for char in s))
    
    # Check if any character is a digit
    print(any(char.isdigit() for char in s))
    
    # Check if any character is lowercase
    print(any(char.islower() for char in s))
    
    # Check if any character is uppercase
    print(any(char.isupper() for char in s))
