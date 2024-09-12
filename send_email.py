import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

from dotenv import load_dotenv

PORT = 587
EMAIL_SERVER = "smtp.gmail.com"

# Load enviroment variables
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)

# Read enviroment variables
sender_email = os.getenv("EMAIL")
sender_password = os.getenv("PASSWORD")



def send_email(subject, reciever_email, name, position):
    #creating base text message.
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("Niteesh Kulhari", f"{sender_email}"))
    msg["To"] = reciever_email
    msg["BCC"] = send_email

    msg.set_content(
        f"""\
        Hi {name}
        I hope you are doing well
        I want to apply to {position}

        Regards
        Niteesh Kulhari
        """
    )

    # Add the html version.
    msg.add_alternative(
            f"""\
        <html>
            <body>
                <p> Hi {name}</p>
                <p> I hope you are doing well</p>
                <p> I want to apply to <strong>{position}</strong> </p>
                <p>Best Regards</p>
                <p>Niteesh Kulhari</p>
            </body>
        </html>
        """,
            subtype="html"
    )

    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, reciever_email, msg.as_string())

if __name__ == "__main__":
    send_email(
        subject = "Referral Request",
        name = "Jack",
        reciever_email = "nkulhari07@gmail.com",
        position = "SDE-1"
    )