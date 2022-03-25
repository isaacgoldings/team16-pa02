import sqlite3

def to_transactions_dict(transactions_tuple):
    ''' transactions is a category tuple (rowid, name, desc)'''
    transactions = {'itemNum':transactions_tuple[0], 'amount':transactions_tuple[1], 'category_t':transactions_tuple[2], 'date':transactions_tuple[3], 'description':transactions_tuple[4]}
    return transactions

def to_transactions_dict_list(transactions_tuple):
    ''' convert a list of category tuples into a list of dictionaries'''
    return [to_transactions_dict(transaction) for transaction in transactions_tuple]
    
class transaction:
    #added by Isaac
    def __init__(self, db):
    
        con= sqlite3.connect(db)
        cur = con.cursor()
        #cur.execute('''DROP TABLE transactions''')
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                    (itemNum INT, amount FLOAT, category_t TEXT, date DATE, description TEXT)''')
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
        cur.execute("INSERT INTO transactions VALUES(?,?,?,?,?)",(item['itemNum'],item['amount'] ,item['category_t'],item['date'],item['description']))
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]

    #added by Lucian
    def delete_transactions(self, item):
        con= sqlite3.connect(self.db)
        sql = "DELETE FROM transactions WHERE itemNUM=?"
        cur = con.cursor()
        cur.execute(sql, (item['itemNum']))
        con.commit()

    def summarize_by_date(self, date):
        con= sqlite3.connect(self.db)
        cur = con.cursor()
        cur.execute("SELECT * from transactions WHERE self.date==date")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_transactions_dict_list(tuples)
