import random
import time
import mysql.connector

#connecting to the sql server (feel free to change the credentials according to your system)
mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="12345678",
)

#creating the database if does not exist
mycursor = mydb.cursor()
create_db_if_doesnt_exist = "CREATE DATABASE IF NOT EXISTS adviceseeker"
mycursor.execute(create_db_if_doesnt_exist)

#connecting to the adviceseeker database
using_adviceseeker = "USE adviceseeker"
mycursor.execute(using_adviceseeker)

#creating a table if does not exist
create_table_if_doesnt_exist = "CREATE TABLE IF NOT EXISTS faqs (id INT AUTO_INCREMENT PRIMARY KEY, question VARCHAR(255), answer VARCHAR(255))"
mycursor.execute(create_table_if_doesnt_exist)

advice = ["If you stare at something you dropped on the ground, eventually someone will pick it up for you.",
"Never take decisions when you are angry and don’t make promises when you are happy.",
"Don’t set your goals around people, because people change.",
"Never be afraid of rejection.",
"Check your bank account often.",
"Floss. Its more important than you think.",
"Happiness is a choice rest all is a matter of perspective.",
"Life is short, don’t waste it living someone else’s life.",
"Love is like a fart. If you have to force it, it’s probably sh*t.",
"If you accidentally closed a browser tab, CTRL + SHIFT + T will reopen it.",
"Make great efforts to be a man you want your daughter to marry.",
"Drink a lot of water before consuming alcohol to prevent a hangover.",
"If you are driving, assume everyone is stupid and will make a terrible decision.",
"Don’t worry too much what other people think about you. Chances are, they probably don’t think about you a whole lot.",
"Hug and kiss people you love while you have a chance.",
"Do some physical exercise for at least 15 – 20 minutes a day.",
"Pick a sport, it will teach you a lot of things.",
"Get out of your comfort zone and try new things.",
"Filter what you say, before you say it.",
"Instead of complaining, try to fix the problem.",
"Spend time with your family more often.",
"Value the time, spend it wisely.",
"Always remember, you have the right to say no.",
"Always be kind to anyone, you’ll never know how deep you touch someone’s life.",
"When nothing is working , go to sleep , start fresh."
]

answers = ["It is certain.", "It is decidedly so.", "Without a doubt", "Yes definitely.", "You may rely on it.",
           "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy try again.",
           "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
           "Don\'t count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]

def main():
    print("\n------------------------------------------------")
    print("\tWelcome to AI advice seeker")
    print("------------------------------------------------\n")
    name = input("What is your name? ")
    print(f"\nHi {name}! You have come to the right place to get the answers of your questions and for adivce full of wisdom.\nChoose what you want to do")

    while(True):
        print("\n------------------------------------------------")
        print("\n-> Enter 1 for a friendly advice :)")
        print("-> Enter 2 to ask your questions")
        print("-> Enter 3 view the previous results")
        print("-> Enter any other key to quit\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            question = "Advice"
            print("\nThinking .............\n")
            time.sleep(2)
            answer= random.choice(advice)
            print(answer)
            #inserting the data into the table
            sql = "INSERT INTO faqs (question, answer) VALUES (%s, %s)"
            val = (question, answer)
            mycursor.execute(sql, val)
            mydb.commit()

        elif choice == "2":
            question = input("\nAsk away! Whatever it is, I will try to answer it: ")
            print("\nThinking .............\n")
            time.sleep(2)
            answer= random.choice(answers)
            print(answer)
            #inserting the data into the table
            sql = "INSERT INTO faqs (question, answer) VALUES (%s, %s)"
            val = (question, answer)
            mycursor.execute(sql, val)
            mydb.commit()

        elif choice == "3":
            mycursor.execute("SELECT * FROM adviceseeker.faqs")
            myresult = mycursor.fetchall()
            print("\nQuestion\t\t\t\tAnswer")
            for x in myresult:
                print(x[1], "\t\t\t\t", x[2])

        else:
            print("Bye bye!")
            break

    mydb.close()

if __name__ == "__main__":
    main()
