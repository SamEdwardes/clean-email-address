"""
Convert the email recipients copy and pasted from email clients into a list of
emails you can copy and paste into any browser.

Usage
-----

Clean a list of two emails:

$ python main.py "abc@acme.com, Sam Edwardes <Sam.Edwardes@gmail.com>"
abc@acme.com, sam.edwardes@gmail.com

Test the tool:
$ python main.py test
"""

import sys


def main():
    input_string = sys.argv[1]
    if input_string.strip().lower() == "test":
        test_string = "abc@acme.com, Sam Edwardes <Sam.Edwardes@gmail.com>"
        expected_result = "abc@acme.com, sam.edwardes@gmail.com"
        assert clean_emails(test_string) == expected_result
        print("✅ test passed")
    else:
        emails = clean_emails(input_string)
        print(emails)


def clean_emails(input_string: str):
    emails = []
    for token in input_string.split(" "):
        if "@" in token:
            token = token.strip().strip(",").lower().lstrip("<").rstrip(">")
            emails.append(token)
    return ", ".join(emails)


if __name__ == "__main__":
    main()
