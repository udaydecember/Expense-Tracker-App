Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:5:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #linear search for transaction by date
... def search_by_date_linear(transactions,target_date):
...   for transaction in transactions:
...     if transaction["date"]==target_date:
...     return transaction
...   return "Transaction not found."
... #sorting transactions based on amount with bubble sort
... def bubble_sort(transactions):
...   amount=len(transactions)
...   for i in range(amount):
...     for j in range(0,amount-i-1):
...       if transactions[j]["amount"] >transactions[j+1]["amount"]:
...         transactions[j], transactions[j+1] = transactions[j+1], transactions[j]
...   return transactions
... #Fetching input from the user
... def add_data(transactions):
...   date=input("enter the date:")
...   amount=int(input("enter the amount:"))
...   description=input("enter the description")
...   transactions.append({"date":date,"amount":amount,"desctiption":description})
...   return transactions
... #Delete data from list
... def delete_data(transactions):
...   date=input("enter the date:")
...   amount=int(input("enter the amount:"))
...   description=input("enter the description")
...   transactions.remove({"date":date,"amount":amount,"desctiption":description})
...   return transactions                                                            #sum the amount
... def sum_amount(transactions):
...   sum=0
...   year=input("enter the year: ")
...   for transactions in transactions:
...     if transactions["date"][5:] == year:
...       sum=transactions["amount"]
