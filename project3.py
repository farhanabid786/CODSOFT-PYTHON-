import random
import string

def generate_password(length, include_uppercase=True, include_digits=True, include_punctuation=True):
    # Define the characters to use in the password
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase else ''
    digits = string.digits if include_digits else ''
    punctuation = string.punctuation if include_punctuation else ''
    
    # Combine all the characters
    all_characters = lowercase + uppercase + digits + punctuation
    
    # Ensure the password includes at least one character from each selected category
    password = []
    if include_uppercase:
        password.append(random.choice(uppercase))
    if include_digits:
        password.append(random.choice(digits))
    if include_punctuation:
        password.append(random.choice(punctuation))
    
    # Fill the rest of the password length with random choices from all characters
    while len(password) < length:
        password.append(random.choice(all_characters))
    
    # Shuffle the password list to ensure randomness
    random.shuffle(password)
    
    # Convert the list to a string
    return ''.join(password)

# Main program
if __name__ == "__main__":
    length = int(input("Enter the desired length for the password: "))
    include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
    include_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
    include_punctuation = input("Include punctuation? (yes/no): ").strip().lower() == 'yes'
    
    password = generate_password(length, include_uppercase, include_digits, include_punctuation)
    print(f"Generated password: {password}")
