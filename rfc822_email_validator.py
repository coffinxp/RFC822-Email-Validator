import re
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# RFC822-compliant regex (simplified for practical use)
RFC822_REGEX = re.compile(
    r"^(?:[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*"
    r'|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")'
    r"@(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*)$"
)

def is_rfc822_valid(email):
    return bool(RFC822_REGEX.match(email))

if __name__ == "__main__":
    email = input("Enter email address: ").strip()
    if is_rfc822_valid(email):
        print(f"RFC822 valid: {Fore.GREEN}YES{Style.RESET_ALL}")
    else:
        print(f"RFC822 valid: {Fore.RED}NO{Style.RESET_ALL}")
