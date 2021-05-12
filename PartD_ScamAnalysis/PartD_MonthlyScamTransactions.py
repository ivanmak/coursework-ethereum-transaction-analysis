import pyspark
from operator import add
import time

"""
Transactions layout
0 - block_number: Block number where this transaction was in
1 - from_address: Address of the sender
2 - to_address: Address of the receiver. null when it is a contract creation transaction
3 - value: Value transferred in Wei (the smallest denomination of ether)
4 - gas: Gas provided by the sender
5 - gas_price : Gas price provided by the sender in Wei
6 - block_timestamp: Timestamp the associated block was registered at (effectively timestamp of the transaction)

ScamsCSV layout
0 - Scam ID
1 - Name
2 - URL
3 - Coin
4 - Category
5 - Sub-category
6 - Address
7 - Status
"""

sc = pyspark.SparkContext()

def is_good_line(line):
    try:
        fields = line.split(',')
        if len(fields) == 7: # transactions
            str(fields[2]) # to_addr
            if int(fields[3]) == 0:
                return False
        elif len(fields) == 8: # contracts
            str(fields[6]) # Scam addr
            str(fields[4]) # Scam category
        else:
            return False
        return True
    except:
        return False

def mapper_transactions(line):
    try:
        fields = line.split(',')
        to_addr = fields[2]
        wei = int(fields[3])
        raw_timestamp = int(fields[6])
        year_month = time.strftime('%Y-%m', time.gmtime(raw_timestamp))

        key = to_addr
        value = ( year_month, wei, 1 )
        return (key, value)
    except:
        pass


transactions = sc.textFile('/data/ethereum/transactions').filter(is_good_line)
scams = sc.textFile('scams.csv').filter(is_good_line)

scams_addr = scams.map(lambda l: (l.split(',')[6], l.split(',')[4]))

# calculate Wei received at each address in each month
step1 = transactions.map(mapper_transactions)
step2 = step1.join(scams_addr)
step3 = step2.map(lambda x: ((x[1][1], x[1][0][0]), (x[1][0][1], x[1][0][2])))
step4 = step3.reduceByKey(lambda a, b: (a[0]+b[0], a[1]+b[1]) )
step5 = step4.map(lambda x: '{},{},{},{},{}'.format(x[0][0], x[0][1], float(x[1][0]/1000000000000000000), x[1][1], float(x[1][0]/1000000000000000000)/x[1][1]))

step5.saveAsTextFile('out_monthly_scam_transactions')
