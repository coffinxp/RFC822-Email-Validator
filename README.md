RFC822 Email Validator
=====================

A simple, offline Python tool for validating email addresses against the RFC822 standard.
Perfect for quick checks, integration into scripts, or security testing of email input fields.

Features
--------
- RFC822-compliant: Uses a regular expression closely matching the RFC822 specification.
- Offline: No network connection required.
- Easy to use: Just run the script and enter an email address.
- Security Testing: Useful for testing input validation, including XSS payloads.

Usage
-----
1. Clone the repository or download the script:
   git clone https://github.com/coffinxp/rfc822-email-validator.git
   cd rfc822-email-validator

2. Run the script:
   python3 rfc822_email_validator.py

3. Enter the email address you want to validate when prompted.

4. Result:
   The script will print "RFC822 valid: YES" if the email is valid, or "RFC822 valid: NO" if not.

Example
-------
$ python3 rfc822_email_validator.py
Enter email address: test@example.com
RFC822 valid: YES

$ python3 rfc822_email_validator.py
Enter email address: "><script>alert(1)</script>@test.com
RFC822 valid: NO

Security Testing
----------------
You can use this tool to test how your application handles potentially malicious email input, such as XSS payloads.
Example payloads to try:
- "><script>alert(1)</script>@test.com
- "><svg/onload=alert(3)>@test.com
- "><svg/onload=confirm(1337)>"@x.y

Requirements
------------
- Python 3.x

---
Inspired by the classic RFC822 email validation tools and designed for modern security testing workflows.
