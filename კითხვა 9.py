


# კითხვა 9.

# 9) while ციკლისა და input-ის საშვალებით მომხარებელს შემოატანინეთ პაროლი სანამ არ იქნება ის "ჩემი რაზმი"-ის ტოლი.

correct_password = ("ჩემი რაზმი")

while True:

    guess_password = input("Enter Password: ")

    if guess_password == correct_password:
        print("Access Granted, Welcome!")
    else:
        print("In Access Denied, Try again:")    
    
