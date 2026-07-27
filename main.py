from datetime import datetime
import pandas as pd
import random
import smtplib
import os

my_email = os.environ.get("MY_EMAIL")
my_password = os.environ.get("MY_PASSWORD")

today = (datetime.now().month, datetime.now().day)

data = pd.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as file:
        content = file.read()
        new_content = content.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person.email,
            msg=f"Subject:Happy Birthday!\n\n{new_content}"
        )
