import random

def generate_random_string(length):
    """
    Generate a random string of characters with the given length.
    """
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
    return ''.join(random.choice(characters) for i in range(length))

def save_to_file(data, filename):
    """
    Save the given data to a file with the given filename.
    """
    with open(filename, 'w') as f:
        f.write(data)

if __name__ == '__main__':
    # Get the length of the random string from user input
    length = int(input("Enter the length of the random string: "))

    # Generate the random string
    random_string = generate_random_string(length)

    # Get the filename to save the random string to
    filename = input("Enter the filename to save the random string to: ")

    # Save the random string to the file
    save_to_file(random_string, filename)
    
    print(f"Random string of length {length} saved to {filename}")
