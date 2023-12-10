import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def run_homelessness_assessment():
    questions = [
        """Question 1:
        a. Stable job and high income
        b. Stable job and moderate income
        c. Some job instability
        d. Unemployment or irregular income
        e. No job or income""",
        """Question 2:
        a. Own a home
        b. Renting stable housing
        c. Renting, but unstable
        d. Unstable housing or at risk of eviction
        e. No permanent housing""",
        """Question 3:
        a. Strong support network (family, friends)
        b. Moderate support network
        c. Limited support network
        d. Isolated or no support network
        e. Estranged from family and friends""",
        """Question 4:
        a. Good physical and mental health
        b. Some health issues
        c. Chronic health issues
        d. Serious health issues or disabilities
        e. Severe mental health challenges""",
        """Question 5:
        a. Emergency savings and financial safety net
        b. Limited savings or financial instability
        c. Some debt, struggling financially
        d. No savings or financial safety net
        e. Overwhelmed with debt and financial issues""",
        """Question 6:
        a. Strong support network (family, friends)
        b. Moderate support network
        c. Limited support network
        d. Isolated or no support network
        e. Estranged from family and friends""",
        """Question 7:
        a. Good physical and mental health
        b. Some health issues
        c. Chronic health issues
        d. Serious health issues or disabilities
        e. Severe mental health challenges""",
        """Question 8:
        a. Stable job and high income
        b. Stable job and moderate income
        c. Some job instability
        d. Unemployment or irregular income
        e. No job or income""",
        """Question 9:
        a. Own a home
        b. Renting stable housing
        c. Renting, but unstable
        d. Unstable housing or at risk of eviction
        e. No permanent housing""",
        """Question 10:
        a. Strong support network (family, friends)
        b. Moderate support network
        c. Limited support network
        d. Isolated or no support network
        e. Estranged from family and friends""",
        """Question 11:
        a. Good physical and mental health
        b. Some health issues
        c. Chronic health issues
        d. Serious health issues or disabilities
        e. Severe mental health challenges""",
        """Question 12:
        a. Emergency savings and financial safety net
        b. Limited savings or financial instability
        c. Some debt, struggling financially
        d. No savings or financial safety net
        e. Overwhelmed with debt and financial issues"""
    ]

    count_of_a = 0
    count_of_b = 0
    count_of_c = 0
    count_of_d = 0
    count_of_e = 0
    homelessness_risk_level = ''
    total_questions = 0

    for question in questions:
        answer = ''
        while not (answer.upper() in ['A', 'B', 'C', 'D', 'E']):
            try:
                answer = input(question).upper()
                if not (answer in ['A', 'B', 'C', 'D', 'E']):
                    raise ValueError("Invalid input. Please choose A, B, C, D, or E.")
            except ValueError as error:
                print(error)
            else:
                if answer == 'A':
                    count_of_a += 1
                elif answer == 'B':
                    count_of_b += 1
                elif answer == 'C':
                    count_of_c += 1
                elif answer == 'D':
                    count_of_d += 1
                elif answer == 'E':
                    count_of_e += 1
                total_questions += 1

    # Assess homelessness risk level
    if total_questions == len(questions):
        max_count = max(count_of_a, count_of_b, count_of_c, count_of_d, count_of_e)
        if max_count == count_of_a:
            homelessness_risk_level = 'Low'
        elif max_count == count_of_b:
            homelessness_risk_level = 'Moderate'
        elif max_count == count_of_c:
            homelessness_risk_level = 'Elevated'
        elif max_count == count_of_d:
            homelessness_risk_level = 'High'
        else:
            homelessness_risk_level = 'Severe'

    print(f"\nHomelessness Risk Level: {homelessness_risk_level}")

    comment = input("\nPlease provide any additional comments or feedback (optional): ")

    user_email = input("\nEnter your email address to receive the test results: ")

    send_email(user_email, homelessness_risk_level, comment)

def send_email(user_email, risk_level, comment):
    sender_email = 'kosiabby@gmail.com'
    sender_password = 'Kosi_abby21'

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = user_email
    message['Subject'] = 'Homelessness Assessment Results'

    body = f"Homelessness Risk Level: {risk_level}\n\n"
    if comment:
        body += f"User Comment: {comment}\n"
    message.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            text = message.as_string()
            server.sendmail(sender_email, user_email, text)
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

# Run the program
run_homelessness_assessment()
