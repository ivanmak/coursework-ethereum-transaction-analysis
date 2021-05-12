import pyspark
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

Contracts layout
0 - address: Address of the contract
1 - is_erc20: Whether this contract is an ERC20 contract
2 - is_erc721: Whether this contract is an ERC721 contract
3 - block_number: Block number where this contract was created
4 - UTC timestamp
"""

sc = pyspark.SparkContext()

def is_good_line(line):
    try:
        fields = line.split(',')
        if len(fields) == 7: # transactions
            str(fields[2]) # to_addr
            int(fields[5])
            int(fields[6])
        else:
            return False
        return True
    except:
        return False

def mapper(line):
    try:
        fields = line.split(',')
        raw_timestamp = int(fields[6])
        key = time.strftime('%Y-%m W%W', time.gmtime(raw_timestamp))

        gas_price = int(fields[5])
        return (key, (gas_price, 1))
    except:
        return ('dummy', (0, 1))


transactions = sc.textFile('/data/ethereum/transactions').filter(is_good_line)

step1 = transactions.map(mapper)
step2 = step1.reduceByKey(lambda a, b: (a[0]+b[0], a[1]+b[1]))
step3 = step2.mapValues(lambda x: int(round(x[0]/x[1]/1000000000)) if x[1] > 0 else 0)
step4 = step3.sortByKey()

print('Week, Gas Price in Gwei')
for row in step4.collect():
    print('{}, {}'.format(row[0], row[1]))
