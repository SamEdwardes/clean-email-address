# Clean Email Addresses
Convert the email recipients copy and pasted from email clients into a list of
emails you can copy and paste into any browser.

## Usage

Clean a list of emails:

```bash
$ python main.py "abc@acme.com, Sam Edwardes <Sam.Edwardes@gmail.com>"
abc@acme.com, sam.edwardes@gmail.com
```

Test the tool:

```bash
$ python main.py test
```