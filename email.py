# The following programmes manage users' emails.
# You can specify the emails you want to check by number and read them, or check unread emails.


### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email(object):

    # has_been_read initialise to False.
    has_been_read = False

    # Declare the class variable, with default value, for emails.
    def __init__(self, email_address, subject_line, email_content):
        # Initialise the instance variables for emails. 
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        self.has_been_read = True

# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox = []

# --- Functions --- #
# Build out the required functions for your program.
def populate_inbox():   
    # Create 3 sample emails and add it to the Inbox list. 
    email1 = Email("sender1@example.com", "Welcome to HyperionDev!", "Dear User, welcome to our platform!")
    email2 = Email("sender2@example.com", "Great work on the bootcamp!", "Congratulations on completing the bootcamp!")
    email3 = Email("sender3@example.com", "Your excellent marks!", "Your performance in the course was outstanding!")
    inbox.extend([email1, email2, email3])
    return inbox
    
# Create a function which prints the email’s subject_line, along with a corresponding number.
def list_emails():
    print("Inbox:")
    for index, email in enumerate(inbox):
        print(f"{index} {email.subject_line}")

# Create a function which displays a selected email. 
# Once displayed, call the class method to set its 'has_been_read' variable to True.
def read_email(index):    
    if index < len(inbox):
        email = inbox[index]
        print(f"\nFrom: {email.email_address}")
        print(f"Subject: {email.subject_line}")
        print(f"\n{email.email_content}")
        email.mark_as_read()
        print(f"\nEmail from {email.email_address} marked as read.\n")
    else:
        print("Invalid email index.\n")

# --- Email Program --- #
# Call the function to populate the Inbox for further use in your program.
def email_simulator():
    populate_inbox()

# Fill in the logic for the various menu operations.
menu = True

email_simulator()    

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
        # add logic here to read an email
        list_emails()
        index = int(input("Enter the index of the email you want to read: "))
        read_email(index)
        
    elif user_choice == 2:
        # add logic here to view unread emails.
        print("Unread emails:")
        for email in inbox:
            if not email.has_been_read:
                print(email.subject_line)
            
    elif user_choice == 3:
        # add logic here to quit application.
        print("Quitting application...")
        break

    else:
        print("Oops - incorrect input.")

