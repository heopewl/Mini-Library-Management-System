



#This is my imports

#These 2 import are used to import my Dictionary, Tuples and List from _234707R.py File
from Main import Book_Library
from Main import Type_of_Book_Allowed

#This 2 imports used to visualised data using Numpy and Matplotlib
import matplotlib.pyplot as plt
import numpy as np

#This 3 imports used for Checking Google Book by using json, requests and webbrowser
import json
import requests
import webbrowser as wb

def menu(): #This Function is used to display options for Main Menu
    print("")
    print("*" * 25)
    print("1. Add book")
    print("2. Update book")
    print("3. Remove book")
    print("4. View books")
    print("5. Check ISBN Infomation on Google Book")
    print("6. Exit")
    print("*" * 25)

def menu2(): #This Function is used to display options for Update Book
    print("")
    print("*" * 25)
    print("What do you want to Update ?")
    print("1. Update ISBN")
    print("2. Update Title")
    print("3. Update Book Type")
    print("4. Update Book Quantity")
    print("5. Go back")
    print("*" * 25)
    print("")

def menu3():#This Function is used to display options for View Book
    print("")
    print("*" * 25)
    print("How do you want to View Book? ?")
    print("1. View Normal")
    print("2. ISBN Ascending Order")
    print("3. ISBN Descending Order")
    print("4. View Quantity using Pie Graph")
    print("5. Go back")
    print("*" * 25)
    print("")

def exitprogram():#This function is used to exit the program
    print("")
    print("*" * 14)
    print("Program Ended!")
    print("*" * 14)
    print("")
    exit()

def ISBN_filter(ISBN_Input): #This Function will be used to filter our ISBN input is according to its Check Digit Validation

    #Declared my 3 flags here
    ISBN_Duplicate = False
    Valid_Book = False
    ISBN_validated = False

    #ISBN input will be strip of spaces and dashes
    ISBN_Input = ISBN_Input.strip()
    ISBN_Input_replaced = ISBN_Input.replace("-", "")

    #If ISBN length is 10 or 13 digit long, The code will then proceed.
    if len(ISBN_Input_replaced) == 10 or len(ISBN_Input_replaced) == 13:

        #The Loop below will run to check if ISBN input has been used in the Dictionary / List.
        for ISBN in Book_Library:
            if ISBN['ISBN'] == ISBN_Input:
                ISBN_Duplicate = True # Flag ISBN Duplicated will be = True
                break # Break the Loops

        #If there is no duplicate found, the code will proceed.
        if ISBN_Duplicate == False:

            #If ISBN input is 13 character long it will run this portion
            if len(ISBN_Input_replaced) == 13 and ISBN_Input_replaced.isdigit():# According to Check Digit Validation, it will do the mathematical formula to check 13 Digit ISBN
                i = 0
                ISBN_total_13Digit = 0
                while i < 12:
                    if i % 2 == 0:
                        ISBN_total_13Digit = ISBN_total_13Digit + (int(ISBN_Input_replaced[i]) * 1)
                    if i % 2 == 1:
                        ISBN_total_13Digit = ISBN_total_13Digit + (int(ISBN_Input_replaced[i]) * 3)
                    i+=1
                ISBN_total_13Digit = ISBN_total_13Digit % 10
                ISBN_total_13Digit = 10 - ISBN_total_13Digit
                if ISBN_total_13Digit == int(ISBN_Input_replaced[12]):
                    ISBN_validated = True # return back to the program what this 13 Digit ISBN is verified


            # If ISBN input is 10 character long it will run this portion
            elif len(ISBN_Input_replaced) == 10 and ISBN_Input_replaced[0-8].isdigit():
                i = 0
                a = 10
                ISBN_total_10Digit = 0
                while i < 9: #isbn number 1 to 9, stop before reaching last number
                    ISBN_total_10Digit += int(ISBN_Input_replaced[i]) * a
                    i +=1
                    a -= 1
                ISBN_total_10Digit = ISBN_total_10Digit % 11 #total modular by 11

                #If 10 Digit ISBN contains a X, it will run the code below.
                if ISBN_Input_replaced[9] == "X":
                    b = 10
                else: #Else it will run this
                    b = 11 % ISBN_total_10Digit


                if (ISBN_total_10Digit + b) % 11 == 0: # According to Check Digit Validation, it should be 0.
                    ISBN_validated = True
            if ISBN_validated:
                return True # It return back true that 10 Digit ISBN is verified.

        #if ISBN has already been used in the Library. It will print that following message below
        else:
            print(f"ISBN {ISBN_Input} is used already in system. Please try again !")




#This Function addBook is used to check if Book Type is valid.
def addBook(ISBN_num):
    Valid_Book = False #This will be my flag to see if book type is valid.
    booktitle_input = str(input("Input Title: ")) #ask user to input book type

    # Ask for book type now
    Type_of_Book = str(input("Type of Book (Hard Cover, Paper Back, eBook ONLY!! Case Sensitive ): "))

    for book_type in Type_of_Book_Allowed:#This for loops check for book type
        if book_type == Type_of_Book:
            Valid_Book = True #if input book type is same as the one checked through the loop, it will set the flag, valid_book true
            break

    if Valid_Book:#if flag is True, this loop will run
        Quantity_Available = int(input("Quantity Available: ")) #ask user to input quantity

        if Quantity_Available >= 0: #Quantity input must be equal or more than 0
            Book_Library.append({ #now it will add all of the input to Book_Library list as dictionary
                'ISBN': ISBN_num,
                'Title': booktitle_input,
                'BookType': Type_of_Book,
                'Quantity_Available': str(Quantity_Available)
            })
        else:
            print("Invalid Quantity, Cannot be negative") # if quantity is less than 0, this will trigger

    else:
        print("Invalid Book Type")#if book type is not valid.


def check_duplicate(ISBN_num): # This function will check there is already a duplicated ISBN in the Book_Library List with the parameter of the functuion.

    duplicate_bool = False #my Flag
    ISBN_num = ISBN_num.strip() #Strip all spaces
    ISBN_num_replaced = ISBN_num.replace("-", "") #replace dashes with nothing

    if len(ISBN_num_replaced) == 10 or len(ISBN_num_replaced) == 13: #if ISBN parameter is equal to 10 or 13, the loop below will run

        for ISBN in Book_Library: #This will loop for X amount of times depending on how many item/ book in Book_Library List
            if ISBN['ISBN'] == ISBN_num: #this will check if ISBN input is already in the Book_Library List

                duplicate_bool = True #If there is a duplicate, set the flag to True
                break
            else:
                duplicate_bool = False #if there is not duplicate, the flag will be set to false

        if duplicate_bool == True: # if flag is true, then it will return true.
            return True
        else:
            print("")
            print("*" * 42)
            return print("There is no such ISBN number in the system\n"+ ("*" * 42)) #if flag is false, will print this following message.
    else:
        print("")
        print("*" * 42)
        return print("There is no such ISBN number in the system\n" + ("*" * 42))#if ISBN number is not 10 or 13 character long, will print this following message.


def update_ISBN(ISBN_num): #This function will help to Update ISBN

    #This will loop for X amount of time, depend on how much Book is in Book_Library
    for ISBN in Book_Library:

        if ISBN['ISBN'] == ISBN_num: #if ISBN input is the same as ISBN in the Book_Library List

            new_ISBN = str(input("Enter New ISBN Number (Including - ): ")) #ask user to input new ISBN

            if ISBN_filter(new_ISBN) == True: # if new inputted ISBN is valid, it will run the following below and update the new ISBN number
                ISBN['ISBN'] = new_ISBN
                print("Changed ISBN Successfully")
                break

            else:
                return print("Invalid ISBN") #If newly inputted ISBN number is not valid, it will the following message.

def update_title(ISBN_num): # This function will help update the Book Title

    for ISBN in Book_Library: #This will loop for X amount of time, depend on how much Book is in Book_Library

        if ISBN['ISBN'] == ISBN_num: #if ISBN input is the same as ISBN in the Book_Library List

            new_Title = str(input("Enter New Title: "))#ask user to input new Title

            ISBN['Title'] = new_Title # it will run the following below and update the Title

            print("Changed Title Successfully")
            break


def update_booktype(ISBN_num): # This function will help update the Book Title
    Valid_Book = False #my Flag
    for ISBN in Book_Library:#This will loop for X amount of time, depend on how much Book is in Book_Library
        if ISBN['ISBN'] == ISBN_num:#if ISBN input is the same as ISBN in the Book_Library List
            Type_of_Book = str(input("Type of Book (Hard Cover, Paper Back, eBook ONLY!! Case Sensitive): ")) #ask user input book type they want to change to
            for book_type in Type_of_Book_Allowed:
                if book_type == Type_of_Book:
                    Valid_Book = True #if input book type is same as the one checked through the loop, it will set the flag, Valid_Book true
                    break

            if Valid_Book: #if flag is True, it will run the following code below to update Book Type
                ISBN['BookType'] = Type_of_Book
                print("Changed Type Successfully")
                break

            else:
                return print("Invalid Book Type") #if flag / book type is invalid, it will return and print the following.

def update_quantity(ISBN_num): #This Function help to update quantity.
    for ISBN in Book_Library:#This will loop for X amount of time, depend on how much Book is in Book_Library

        if ISBN['ISBN'] == ISBN_num:#if ISBN input is the same as ISBN in the Book_Library List
            new_Quantity = int(input("Enter New Quantity Number (No negative number): ")) #ask user input new quantity they want to change to

            if new_Quantity >= 0: #if inputted quantity is not in the negative range, then it will change the old quantity to the new quantity
                    ISBN['Quantity_Available'] = new_Quantity

                    print("Changed Quantity Successfully")
                    break

            else: #If quantity inputted is in the negative range, then return invalid quantity.
                return print("Invalid Quantity")

def delete(ISBN_num): #This Function help to delete book.

    for ISBN in Book_Library:#This will loop for X amount of time, depend on how much Book is in Book_Library

        if ISBN['ISBN'] == ISBN_num: #if ISBN input is the same as ISBN in the Book_Library List
            Book_Library.remove(ISBN)#this will then delete that book from the Book_Library lsit
            print("Delete Successfully")
            break



def makeTable(): #This will print out the books in the Book_Library list as a table
    position2 = [] #used to store title character length
    position3_ISBN = [] #used to store ISBN character length
    position4_Quantity = [] #used to store Quantity character length

    for ISBN in Book_Library: #This will loop for X amount of time, depend on how much Book is in Book_Library
        position2.append(len(ISBN['Title'])) #it will check and add the character length to position2

        ISBN['Quantity_Available'] = str(ISBN['Quantity_Available'])#convert quantity number to a string

        position3_ISBN.append(len(ISBN['ISBN']))#it will check and add the character length to position3_ISBN

        position4_Quantity.append(len(ISBN['Quantity_Available']))#it will check and add the character length to position4_Quantity


    #This part will print the table headers
    max_ISBN = max(position3_ISBN) + 1 # used the largest character length of ISBN number
    max_title = max(position2) # used the largest character length of Title
    position4 = (50 + int(max_title)) - (max_ISBN + 2) - (max_title + 2) - 12 - 5 #Calculation for the last column formatting

    #This will print the table header
    print((50 + int(max_title)) * "-")
    print("|" + " ISBN:"  + (" "* int(max_ISBN - 5)) +"|"
          + " Title:" +
          (" "* (max_title - 5) +"|" + " Book Type: |")
          + " Quantity:"+ (" "* int(position4 - 9) )  +"|")

    #This part will print the table data like book information
    for ISBN in Book_Library:#This will loop for X amount of time, depend on how much Book is in new_Dict
        print((50 + int(max_title)) * "-")

        print("|" + " " + ISBN["ISBN"] +(" " * (max_ISBN - len(ISBN['ISBN'])) ) +"| " + ISBN['Title'] +
              (" " * (max_title - len(ISBN['Title']))) + " | " + ISBN['BookType'] +
              (" " * (10 - len(ISBN['BookType']))) + " | " + str(ISBN['Quantity_Available'])+ (" " * (position4 - len(ISBN['Quantity_Available'])) ) +"|")

    print((50 + int(max_title)) * "-")


def sort_view():#This will print out Book information according to Ascending ISBN number in a table
    new_Dict = sorted(Book_Library,key=lambda num:num['ISBN'])#this will sort the Book_Library list in an ascending order based on ISBN number
    position2 = [] #used to store title character length
    position3_ISBN = [] #used to store ISBN character length
    position4_Quantity = [] #used to store Quantity character length

    for ISBN in new_Dict: #This will loop for X amount of time, depend on how much Book is in new_Dict

        position2.append(len(ISBN['Title']))#it will check and add the character length to position2

        ISBN['Quantity_Available'] = str(ISBN['Quantity_Available'])#convert quantity number to a string

        position3_ISBN.append(len(ISBN['ISBN']))#it will check and add the character length to position3_ISBN

        position4_Quantity.append(len(ISBN['Quantity_Available']))#it will check and add the character length to position4_Quantity

    # This part will print the table headers
    max_ISBN = max(position3_ISBN) + 1 # used the largest character length of ISBN number
    max_title = max(position2) # used the largest character length of Title
    position4 = (50 + int(max_title)) - (max_ISBN + 2) - (max_title + 2) - 12 - 5 #Calculation for the last column formatting


    # This will print the table header
    print((50 + int(max_title)) * "-")
    print("|" + " ISBN:" + (" " * int(max_ISBN - 5)) + "|"
          + " Title:" +
          (" " * (max_title - 5) + "|" + " Book Type: |")
          + " Quantity:" + (" " * int(position4 - 9)) + "|")

    # This part will print the table data like book information
    for ISBN in new_Dict:#This will loop for X amount of time, depend on how much Book is in new_Dict
        print((50 + int(max_title)) * "-")

        print("|" + " " + ISBN["ISBN"] +(" " * (max_ISBN - len(ISBN['ISBN'])) ) +"| " + ISBN['Title'] +
              (" " * (max_title - len(ISBN['Title']))) + " | " + ISBN['BookType'] +
              (" " * (10 - len(ISBN['BookType']))) + " | " + str(ISBN['Quantity_Available'])+ (" " * (position4 - len(ISBN['Quantity_Available'])) ) +"|")

    print((50 + int(max_title)) * "-")

def sort_view_descending():#This will print out Book information according to Descending ISBN number in a table

    new_Dict = sorted(Book_Library,key=lambda num:num['ISBN'],reverse = True)#this will sort the Book_Library list in an Descending order based on ISBN number

    position2 = []#used to store title character length

    position3_ISBN = []#used to store ISBN character length

    position4_Quantity = []#used to store Quantity character length

    # This part will print the table headers
    for ISBN in new_Dict: #This will loop for X amount of time, depend on how much Book is in new_Dict

        position2.append(len(ISBN['Title']))#it will check and add the character length to position2

        ISBN['Quantity_Available'] = str(ISBN['Quantity_Available'])#convert quantity number to a string

        position3_ISBN.append(len(ISBN['ISBN']))#it will check and add the character length to position3_ISBN

        position4_Quantity.append(len(ISBN['Quantity_Available']))#it will check and add the character length to position4_Quantity


    max_ISBN = max(position3_ISBN) + 1 # used the largest character length of ISBN number
    max_title = max(position2) # used the largest character length of Title
    position4 = (50 + int(max_title)) - (max_ISBN + 2) - (max_title + 2) - 12 - 5 #Calculation for the last column formatting

    # This part will print the table headers
    print((50 + int(max_title)) * "-")
    print("|" + " ISBN:" + (" " * int(max_ISBN - 5)) + "|"
          + " Title:" +
          (" " * (max_title - 5) + "|" + " Book Type: |")
          + " Quantity:" + (" " * int(position4 - 9)) + "|")

    # This part will print the table data like book information
    for ISBN in new_Dict:#This will loop for X amount of time, depend on how much Book is in new_Dict
        print((50 + int(max_title)) * "-")

        print("|" + " " + ISBN["ISBN"] +(" " * (max_ISBN - len(ISBN['ISBN'])) ) +"| " + ISBN['Title'] +
              (" " * (max_title - len(ISBN['Title']))) + " | " + ISBN['BookType'] +
              (" " * (10 - len(ISBN['BookType']))) + " | " + str(ISBN['Quantity_Available'])+ (" " * (position4 - len(ISBN['Quantity_Available'])) ) +"|")

    print((50 + int(max_title)) * "-")


def GooglebookAPI(): #This function will look up ISBN number on Google Book Database of ISBN, if the ISBN is on their database it will response back with all the book information.

    isbn = input("Enter ISBN: ") #ask user to input the ISBN number they want to find out about

    # it will strip all of the spaces and dashes.
    isbn = isbn.strip()
    isbn = isbn.replace("-", "")


    url = "https://www.googleapis.com/books/v1/volumes?q=isbn:" + isbn #This url is the google book API request link
    response = requests.get(url) #This will request the API for the ISBN information.
    data = json.loads(response.content) #This will convert the response data to a format that i can use.

    items_found = data["totalItems"] #To see how many search result came up

    if response.status_code == 429 or response.status_code == 403: #This will look at the response status code. When a successful Request is usually made, its response code is 200, but should the API request exceed or error happens, it will return either response code 429 or 403.
        print("API limit reach. This function will not work, Wait for a day") #should the response status code has an error this function will not work for a day or more depending on your IP address. If Testing in NYP network, this funcion will not work. (think the school using alot of google API)

    else:#should the response code is not the error code it will try to print the following below
        if items_found > 0: #This will find out how many search result, if there is more than 0 search result it will print out the book informaton.
            try:

                link = data['items'][0]['volumeInfo']['infoLink'] #This will look at the data find out about the book link on google book

                title = data["items"][0]["volumeInfo"]["title"]#This will look at the data find out about the title name on google book

                author = data["items"][0]["volumeInfo"]["authors"]#This will look at the data find out about the book author on google book

                publisher = data["items"][0]["volumeInfo"]["publisher"]#This will look at the data find out about book publisher on google book

                publishedDate = data["items"][0]["volumeInfo"]["publishedDate"]#This will look at the data find out about book published date

                amountofwords = len(data["items"][0]["volumeInfo"]["title"]) + 7 #This will look at the character length of the Title

                print("-"*amountofwords) #this will just print out dashes for easy viewing

                print("Google Book Search Result")

                print("-"*amountofwords) #this will just print out dashes for easy viewing

                print(f"Title: {title}") #print out book title

                print("-" * amountofwords) #this will just print out dashes for easy viewing

                print(f"Authors: {','.join(author)}") #print out book author

                print("-" * amountofwords) #this will just print out dashes for easy viewing

                print(f"Publisher: {publisher}")#print out book publisher

                print("-" * amountofwords) #this will just print out dashes for easy viewing

                print(f"Published Date: {publishedDate}")#print out book published data

                print("-" * amountofwords) #this will just print out dashes for easy viewing

                openlink = input("Do you want to view it in the browser (Y or N): ") #this will ask user whether if they want to view the book in google book on the browser
                if openlink == "Y" or openlink == "y":
                    wb.open(link,new=1,autoraise=True) #if user type Y, it will open a browser and go to the link of this book in google book

            except NameError: #should any error still happen it will print the following
                print("*" * 48)
                print("Invalid ISBN / Not found in Google Book Database")
                print("*" * 48)

            except:#should any error still happen it will print the following
                print("*" * 48)
                print("Invalid ISBN / Not found in Google Book Database")
                print("*" * 48)

        else:#if there is 0 search result it will print out the following.
            print("*"*48)
            print("Invalid ISBN / Not found in Google Book Database")
            print("*" * 48)

def piechart(): #this will visualise book quantity as an pie chart

    BookTitle = [] #This will keep book title in here

    Quantity = [] #This will keep the quantity value in here

    for ISBN in Book_Library: #This will loop for X amount of time, depend on how much Book is in Book_Library

        BookTitle.append(ISBN['Title']) #add book title to BookTitle List

        Quantity.append(ISBN['Quantity_Available']) #add book quantity to Quantity List

    y = np.array(Quantity) #This will convert Quantity list to an array

    plt.pie(y,labels= Quantity) #This will then convert it into a pie chart

    plt.legend(BookTitle,title = "Book Title:") #this will add an legend to the pie chart, about book title

    plt.show() #This will now show the pie chart out

