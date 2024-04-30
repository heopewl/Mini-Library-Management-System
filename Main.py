

#This is my imports

#This import all of my function from ISBN_Functions.py File
import ISBN_Functions as f2


#This is my dictionary, list, tuples
Book_Library = [
    {
        'ISBN': "978-0134846019",
        'Title': "Data Analytics with Spark Using Python",
        'BookType': "Paper Back",
        'Quantity_Available': "6"
    },
    {
        'ISBN': "978-0133316032",
        'Title': "Children's Reading",
        'BookType': "eBook",
        'Quantity_Available': "3"
    },
    {
        'ISBN': "978-1292100142",
        'Title': "Global Marketing, 7th Edition",
        'BookType': "eBook",
        'Quantity_Available': "8"
    },
    {
        'ISBN': "978-1587147029",
        'Title': "CCNA Cyber Ops SECFND #210-250 Official Cert Guide",
        'BookType': "Hard Cover",
        'Quantity_Available': "5"
    },
    {
        'ISBN': "0306406152",
        'Title': "Learn Data Analytics in 100 days",
        'BookType': "Paper Back",
        'Quantity_Available': "10"
    }
]

Type_of_Book_Allowed = ("Paper Back", "Hard Cover", "eBook")




#Start of program
if __name__ == "__main__":

    while 1: #Loop forever until exited
        break_out_choice2 = False
        break_out_choice3 = False
        f2.menu()

        choice = input("Enter your choice: ") #Ask for user input choice in the first menu

        if choice == "1": #if user select 1, in main menu, they can add a book
            ISBN_Input = str(input("Enter ISBN: "))
            if f2.ISBN_filter(ISBN_Input) == True: #This will check whether input ISBN is correct according the calculation, if it comes back as True, it will allow them to proceed and add book type, title , quantity.
                f2.addBook(ISBN_Input)

            else:#if ISBN is invalid, it will print the below
                print("-" * 15)
                print("Invalid ISBN")
                print("-" * 15)

        elif choice == "2" and break_out_choice2 == False: #if user select 2, in main menu,  they can update a book detail, etc

            f2.menu2() #print out menu 2

            update_input = input("Enter your choice: ") #Ask for user input choice in the second menu

            if update_input == "1": #if user select 1 in second menu, they will update ISBN number
                update_isbn = str(input("Please input ISBN number you want to update. Including the - : "))

                if f2.check_duplicate(update_isbn) == True: #if ISBN duplicate checker come back as true, it then allow the update of ISBN
                    f2.update_ISBN(update_isbn)


            elif update_input == "2":#if user select 2 in second menu, they will update Book Title

                update_title_input = str(input("Please Input ISBN Number of the Book Title you want to update. Including the - : "))

                if f2.check_duplicate(update_title_input) == True:#if ISBN duplicate checker come back as true, it then allow the update of Book Title
                    f2.update_title(update_title_input)


            elif update_input == "3":#if user select 3 in second menu, they will update Book Type
                update_booktype_input = str(input("Please Input ISBN Number of the Book Type you want to update. Including the - : "))
                if f2.check_duplicate(update_booktype_input) == True:#if ISBN duplicate checker come back as true, it then allow the update of Book Type
                    f2.update_booktype(update_booktype_input)


            elif update_input == "4":#if user select 4 in second menu, they will update Book Quantity
                update_quanitiy_input = str(input("Please Input ISBN Number of the Quantity you want to update. Including the - : "))
                if f2.check_duplicate(update_quanitiy_input) == True:#if ISBN duplicate checker come back as true, it then allow the update of Book Quantity
                    f2.update_quantity(update_quanitiy_input)


            elif update_input == "5":#if user select 5 in second menu, they will go back to main menu
                break_out_choice2 == True #set the flag to true and stop this loop of secondary menu

            else:#if choice is not from 1 to 5, it will print the following below.
                print("-" * 15)
                print("Invalid Choice")
                print("-" * 15)

        elif choice == "3": #if user select 3, in main menu, they delete a book
            deletion_of_book = str(input("Please Input ISBN Number of the Book you want to deleting. Including the - : "))

            if f2.check_duplicate(deletion_of_book) == True:
                f2.delete(deletion_of_book)

        elif choice == "4" and break_out_choice3 == False: #if user select 4, in main menu, they go to the third menu to view book

            f2.menu3()#print out third menu

            view_choice = input("Enter your choice: ") #ask user for choice

            if view_choice == "1": #if user select 1 in third menu, print normal table
                f2.makeTable()

            elif view_choice == "2":#if user select 2 in third menu, print table in an ascending table based on ISBN number
                f2.sort_view()

            elif view_choice == "3":#if user select 3 in third menu, print table in an descending table based on ISBN number
                f2.sort_view_descending()

            elif view_choice == "4":#if user select 4 in third menu, show an pie chart of book quantity in the Book_Library list.
                f2.piechart()

            elif view_choice == "5":#if user select 5 in third menu, they will go back to main menu
                break_out_choice3 = True

            else:#if choice is not from 1 to 5, it will print the following below.
                print("-" * 15)
                print("Invalid Choice")
                print("-" * 15)


        elif choice == "5": #if user select 5, in main menu, they can find out about ISBN information on Google Book API
            f2.GooglebookAPI()


        elif choice == "6": #if user select 6, in main menu, user will stop this program.
            f2.exitprogram()
            
        else:#if choice is not from 1 to 6, it will print the following below.
            print("-" * 15)
            print("Invalid Choice")
            print("-" * 15)

#End of Program





