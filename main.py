from feature import search_by_date-linear,sort_amount,add_data,delete-data_date,sum_amount
#list of dict value in a varieble transactions
transactions=[
              {"date":"23-8-2024","amount":40,"description":"toy"},
              {"date":"24-8-2024","amount":60,"description":"mango"},
              {"date":"25-8-2024","amount":80,"description":"apple"},
              {"date":"26-8-2024","amount":100,"description":"orange"},
              {"date":"27-8-2024","amount":90,"description":"berry"}
             ]
#combining the features into application
flag=True
while flag:
  print("1.add")
  print("2.sort")
  print("3.search")
  print("4.delete")
  print("5.display")
  print("6.exit")
  print("7.sum amount")
  choice=int(input("enter your choice"))
  if choice==1:
    print("-"*50)
    print("adding data")
    print("-"*50)
    transactions=add_data(transactions)
    print("-"*50)
  elif choice==2:
     print("-"*50)
     print("search data")
     print("-"*50)
     transactions=search_by_data_linear(transactions)
     print("-"*50)
  elif choice==3:
     print("-"*50)
     print("sort data")
     print("-"*50)
     transactions=sort_amount(transactions)
     print("-"*50)
  elif choice==4:
     print("-"*50)
     print("delete data")
     print("-"*50)
     transactions=delete_data_date(transactions)
     print("-"*50)
  elif choice==5:
     print("-"*50)
     print("displaying transactions")
     print("-"*50)
     transactions=("transactions")
     print("-"*50)
  elif choice==6:
     print("-"*50)
     print("existing applications")
     flag=False
     print("-"*50)
  elif choice==7:
    print("-"*50)
    print("sum of amount of a given year")
    print(sum_amount(transactions))
    print("-"*50)
  else:
    print("-"*50)
    print("please enter the correct choice: ")
