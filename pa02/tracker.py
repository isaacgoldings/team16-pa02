#! /opt/miniconda3/bin/python3
'''
tracker is an app that maintains a list of personal
financial transactions.

It uses Object Relational Mappings (ORM)
to abstract out the database operations from the
UI/UX code.

The ORM, Category, will map SQL rows with the schema
  (rowid, category, description)
to Python Dictionaries as follows:

(5,'rent','monthly rent payments') <-->

{rowid:5,
 category:'rent',
 description:'monthly rent payments'
 }

Likewise, the ORM, Transaction will mirror the database with
columns:
amount, category, date (yyyymmdd), description

In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database ~/tracker.db

Note the actual implementation of the ORM is hidden and so it 
could be replaced with PostgreSQL or Pandas or straight python lists

'''

#from transactions import Transaction
from category import Category
from transactions import transaction
import sys

#transactions = Transaction('tracker.db')
category = Category('tracker.db')

transactions = transaction('tracker.db')


# here is the menu for the tracker app

menu = '''
0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu
'''



def process_choice(choice):

    if choice=='0':
        return
    elif choice=='1':

        cats = category.select_all()
        print_categories(cats)
    elif choice=='2':
        name = input("category name: ")
        desc = input("category description: ")
        cat = {'name':name, 'desc':desc}
        category.add(cat)
    elif choice=='3':
        print("modifying category")
        rowid = int(input("rowid: "))
        name = input("new category name: ")
        desc = input("new category description: ")
        cat = {'name':name, 'desc':desc}
        category.update(rowid,cat)
    elif choice=='4':
        transact = transactions.show_transactions()
        print(transact[0])
        print_transactions(transact)
    elif choice=='5':
        itemNum = input("transaction itemNum: ")
        amount = input("transaction amount: ")
        category_t = input("transaction category: ")
        date = input("transaction date: ")
        description = input("transaction description: ")
        transaction = {'itemNum':itemNum, 'amount':amount, 'category_t':category_t, 'date':date, 'description':description}
        transactions.add_transactions(transaction)
    elif choice=='6':
        itemNum = input("transaction itemNum: ")
        transaction = {'itemNum':itemNum}
        transactions.delete_transactions(transaction)
    elif choice=='7':
        d_date = input("Date: ")
        d_transactions = transactions.summarize_by_date(d_date)
        print_transactions(d_transactions)
    elif choice=='8':
        month = input("Month: ")
        month_search = transactions.summarize_by_month(month)
        print_transactions(month_search)
    elif choice =='9':
        year_date = input("Input year:")
        year_transactions = transactions.summarize_by_year(year_date)
        print_transactions(year_transactions)

    elif choice=='11':
        print(menu)
    else:
        print("choice",choice,"not yet implemented")

    choice = input("> ")
    return(choice)


def toplevel():
    ''' handle the user's choice '''

    ''' read the command args and process them'''
    print(menu)
    choice = input("> ")
    while choice !='0' :
        choice = process_choice(choice)
    print('bye')

#
# here are some helper functions
#

def print_transactions(items):
    ''' print the transactions '''
    if len(items)==0:
        print('no items to print')
        return
    print('\n')
    print("%-10s %-10s %-10s %-10s %-30s"%(#changed 2nd and 4rd d to s
        'item #','amount','category','date','description'))
    # print("%-10s %-10d %-10s %-10d %-30s"%(
    #     'item #','amount','category','date','description'))
    print('-'*40)
    for item in items:
        values = tuple(item.values()) 
        print("%-10s %-10s %-10s %-10s %-30s"%values)#changed 2nd and 4th d to s

def print_category(cat):
    print("%-3d %-10s %-30s"%(cat['rowid'],cat['name'],cat['desc']))

def print_categories(cats):
    print("%-3s %-10s %-30s"%("id","name","description"))
    print('-'*45)
    for cat in cats:
        print_category(cat)


# here is the main call!

toplevel()

