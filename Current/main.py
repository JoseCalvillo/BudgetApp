import sqlite3
import datetime



con = sqlite3.connect("expenses")

cur = con.cursor()

while True:
		print("Select an option:")
		print("1. Enter a new expense:")
		print("2. View expenses summary:")
		
		choice = int(input())
		
		if choice == 1:
			date = input("Enter the date of the expense (YYYY-MM-DD) ")
			description = input("Enter description for the expense ")
			
			cur.execute("SELECT DISTINCT category FROM expenses")


			print("Select a category by number: ")
			for index, category in enumerate(category):
				print(f"{index + 1}. {category[0]}")
			print(f"{len(category) + 1}. Create a new category ")

			category_choice = int(input())
			if category_choice == len(category) + 1:
				category = input("Enter the new category name: ")
			else:
				category = category[category_choice - 1][0]

			price = input("Enter the price of the expense: ")

			
			#Notice here we use (?, ?, ?, ?) operator which is to help prevent sql injection.
			cur.execute("INSERT INTO expenses (Date, description, category, price) VALUES (?, ?, ?, ?)")

			con.commit()

		elif choice == 2:
			print("Select an option:")
			print("1. View all expenses")
			print("2. View monthly expenses by category")

			view_choice = int(input()) 
			if view_choice == 1:
				cur.execute("SELECT * FROM expenses")
				expenses = cur.fetchall()
				for expense in expenses:
					print(expense)
			elif view_choice == 2:
				month = input("Enter the month (MM): ")
				year = input ("Enter the month (MM): ")
			
				cur.execute("""SELECT category, SUM(price) FROM expenses
								WHERE strftime('%m', Date) = ? AND strftime('%Y', Date) = ?
								Group BY category""", (month, year))
				expenses = cur.fetchall()
				for expense in expenses:
					print(f"Category: {expense[0]}, Total: {expense[1]}")
			else:
				exit()



		else:
			exit()

		repeat = input("Would you like to do something else (y/n)?\n")
		if repeat.lower() != "y":
			break
    
con.close()