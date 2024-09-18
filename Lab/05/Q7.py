def is_valid_email(email):
    if '@' in email and '.' in email:
        username, domain = email.split('@', 1)
        if username and domain and '.' in domain:
            return True
    return False

def extract_emails(text):
    words = text.split()
    valid_emails = []

    for word in words:
        word = word.strip('.,;:!?"()[]')
        if is_valid_email(word):
            valid_emails.append(word)

    return valid_emails

text = """
Please contact us at support@example.com for any inquiries.
You can also reach out to john.doe123@example.co.uk or jane_doe@web.net.
Invalid email addresses include: user@.com, @missingusername.com.
For more info, email info@my-site.org or sales@example.org.
"""
emails = extract_emails(text)
print("Valid Email Addresses:")
for email in emails:
    print(email)
