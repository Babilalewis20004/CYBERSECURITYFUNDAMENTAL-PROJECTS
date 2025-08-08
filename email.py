class Email:
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    def mark_as_read(self):
        self.has_been_read = True

# Initialize an empty inbox list
inbox = []

def populate_inbox():
    # Create sample emails
    email1 = Email("example1@example.com", "Welcome to HyperionDev!", "Hello, welcome to the bootcamp!")
    email2 = Email("example2@example.com", "Great work on the bootcamp!", "Keep up the great work!")
    email3 = Email("example3@example.com", "Your excellent marks!", "Congratulations on your excellent marks!")

    # Add emails to the inbox
    inbox.extend([email1, email2, email3])

def list_emails():
    for index, email in enumerate(inbox):
        print(f"{index} {email.subject_line}")

def read_email(index):
    if 0 <= index < len(inbox):
        email = inbox[index]
        email.mark_as_read()
        print(f"From: {email.email_address}\nSubject: {email.subject_line}\nContent: {email.email_content}")
    else:
        print("Invalid index")

# Populate the inbox with sample emails at startup
populate_inbox()

# Example usage
list_emails()
read_email(1)




while True:
    print("\n1. Read an email")
    print("2. View unread emails")
    print("3. Quit application")
    choice = input("Choose an option: ")

    if choice == "1":
        list_emails()
        index = int(input("Enter the index of the email you want to read: "))
        read_email(index)
    elif choice == "2":
        print("\nUnread Emails:")
        for index, email in enumerate(inbox):
            if not email.has_been_read:
                print(f"{index} {email.subject_line}")
    elif choice == "3":
        print("Exiting the application.")
        break
    else:
        print("Invalid choice. Please try again.")

