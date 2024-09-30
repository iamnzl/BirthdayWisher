##################### Extra Hard Starting Project ######################
import datetime as dt
import random
import smtplib
import pandas as pd



# 2. Check if today matches a birthday in the birthdays.csv
birthdate_df = pd.read_csv("birthdays.csv")


now = dt.datetime.now()

birthdays_to_wish = birthdate_df[(birthdate_df['month'] == now.month) & (birthdate_df['day'] == now.day)]


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

i = random.randint(1,3)
with open(f"letter_templates/letter_{i}.txt") as letter:
    content = letter.read()


for index,row in birthdays_to_wish.iterrows():
    birthdays_to_wish.loc[index,"message"] = content.replace('[NAME]',row["name"])



# 4. Send the letter generated in step 3 to that person's email address.
my_email = "nooraninazil@gmail.com"

for index,row in birthdays_to_wish.iterrows():

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # secure connection
        connection.login(user=my_email, password="bevpmzpqkgqmgrbj")
        body = row["message"]
        connection.sendmail(from_addr=my_email,
                            to_addrs=row["email"],
                            msg=f"Subject:Happy Birthday\n\n{body}")




