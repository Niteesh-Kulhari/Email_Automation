from datetime import date
import pandas as pd
from send_email import send_email

#Googlesheets
SHEET_ID = "1M76cET9JHLoRiIylmyXAe873DkjY4pdkoGXhENr56a8"
SHEET_NAME = "Sheet3"
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"


def load_df(url):
    df = pd.read_csv(url)
    return df

#print(load_df(URL))


def query_dataand_send_emails(df):
    email_counter = 0
    for _, row in df.iterrows():
        if(row["sent"] == "no"):
            send_email(
                subject = "Referral Request",
                name = row["name"],
                reciever_email = row["email"],
                position = row["position"]
            )
            email_counter += 1
    return f"Total Emails sent: {email_counter}"

df = load_df(URL)
print(query_dataand_send_emails(df))