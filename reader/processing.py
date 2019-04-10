import csv
import json

import tabula
from models import StatEntry


def read_table(file, user):
    tabula.convert_into(file, 'file.csv', output_format='csv', pages='all')
    head = ['Txn Date', 'Value Date', 'Description', 'Ref No./Cheque No.', 'Debit', 'Credit', 'Balance']
    with open('file.csv') as f:
        data = csv.reader(f)
        data = list(data)
        row0 = data[0]
        m = len(row0)
        i = 0
        while i < len(data):
            f = data[i]
            i += 1
            while i < len(data):
                rowi = data[i]
                if rowi[-1] != '':
                    break
                for j in range(m):
                    if rowi[j] != '':
                        f[j] = f[j] + ' ' + rowi[j]
                i += 1
            if f == head:
                print f
            else:
                entry = StatEntry(txn_date=f[0], val_date=f[1], description=f[2], ref_no=f[3], debit=f[4],
                                  credit=f[5], balance=f[6], user=user)
                entry.save()


def query_db(user):
    q = list(StatEntry.objects.filter(user=user))
    json_data = {}
    j = 1
    for i in q:
        data = {'txn_date': i.txn_date, 'val_date': i.val_date, 'description': i.description, 'ref_no': i.ref_no,
                'debit': i.debit, 'credit': i.credit, 'balance': i.balance}
        json_data[j] = json.dumps(data)
        j+=1
    return json.dumps(json_data)
