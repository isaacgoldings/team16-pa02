import sqlite3

def to_transactions_dict(transactions_tuple):
    ''' transactions is a category tuple (rowid, name, desc)'''
    transactions = {'rowid':transactions_tuple[0], 'itemNum':transactions_tuple[1], 'amount':transactions_tuple[2], 'date':transactions_tuple[3], 'description':transactions_tuple[4]}
    return transactions

def to_transactions_dict_list(transactions_tuple):
    ''' convert a list of category tuples into a list of dictionaries'''
    return [to_transactions_dict(transaction) for transaction in transactions_tuple]
    
class transaction:
    #added by Isaac
    def __init__(self, db):
    
        con= sqlite3.connect(db)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                    (itemNum INT, amount FLOAT, category TEXT, date DATE, description TEXT)''')
        con.commit()
        con.close()

        self.db = db
    #added by Isaac
    def show_transactions(self):
        ''' return all of the transactions as a list of dicts.'''
        con= sqlite3.connect(self.db)
        cur = con.cursor()
        cur.execute("SELECT * from transactions")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_transactions_dict_list(tuples)

    #added by Isaac
    def add_transactions(self, item):
        con= sqlite3.connect(self.db)
        cur = con.cursor()
        cur.execute("INSERT INTO transactions VALUES(?,?,?,?,?)",(item['itemNum'],item['amount'],item['category'],item['date'],item['description']))
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]

