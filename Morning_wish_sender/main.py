import smtplib
import ssl
from email.message import EmailMessage
import requests
from bs4 import BeautifulSoup


def send_mail(R_mail, Body):
    sender_email = "write the sender's mail"
    passcode = "passcode"
    r_email = R_mail
    mail = EmailMessage()
    mail['From'] = sender_email
    mail['to'] = r_email
    mail['subject'] = "Morning wish"
    mail.set_content(Body)

    content = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=content) as smtp:
        smtp.login(sender_email, passcode)
        smtp.sendmail(sender_email, r_email, mail.as_string())


def scrap_message(url):
    # Send a GET request to the specified URL
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception if the request was unsuccessful

    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the elements containing the news headlines
    message = soup.find('button', id="selectable")  # Adjust this based on the specific HTML structure
    t_text = message.text.strip()

    return t_text


if __name__ == '__main__':
    body = scrap_message("https://www.morningimg.com/good-morninig-Messages/good-morning-message-for-friends/")#This is a website that is use to fetch the message for frineds
    send_mail("receiver's mail", body)
