import pyspark
from operator import add

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
            if int(fields[3]) == 0:
                return False
        elif len(fields) == 5: # contracts
            str(fields[0]) # contract addr
        else:
            return False
        return True
    except:
        return False

transactions = sc.textFile('/data/ethereum/transactions').filter(is_good_line)
contracts = sc.textFile('/data/ethereum/contracts').filter(is_good_line)


step1 = transactions.map(lambda l: (l.split(',')[2], int(l.split(',')[3])))
step2 = step1.reduceByKey(add)
step3 = step2.join(contracts.map(lambda x: (x.split(',')[0], 'contract')))
top10 = step3.takeOrdered(10, key = lambda x: -x[1][0])

for record in top10:
    print("{},{}".format(record[0], int(record[1][0]/1000000000000000000)))
