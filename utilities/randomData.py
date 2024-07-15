
import random
class randomy():
    @staticmethod
    def generate_random_phone_number():
        area_code = 566  # Generate a random 3-digit area code
        prefix = 565  # Generate a random 3-digit prefix
        line_number = random.randint(100, 999)  # Generate a random 4-digit line number
        phone_number = f"{area_code}{prefix}{line_number}"  # Format the phone number
        return phone_number

    @staticmethod
    def add_random_numbers_to_email(email, num_digits=5):
        # Split the email address into local part and domain
        local_part, domain = email.split('@')
        # Generate random digits
        random_digits = ''.join(str(random.randint(0, 9)) for _ in range(num_digits))
        # Add "+1" followed by random digits to the local part and recombine
        new_email = f"{local_part}+{random_digits}@{domain}"
        return new_email