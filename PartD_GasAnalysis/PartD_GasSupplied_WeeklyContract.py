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
        if len(fields) == 7:  # transactions
            str(fields[2])  # to_addr
            if int(fields[3]) == 0:
                return False
        elif len(fields) == 5:  # contracts
            str(fields[0])  # contract addr
        else:
            return False
        return True
    except:
        return False

def mapper(line):
    try:
        fields = line.split(',')
        raw_timestamp = int(fields[6])
        year_month = time.strftime('%Y-%m W%W', time.gmtime(raw_timestamp))
        key = (fields[2], year_month)

        #print('Timestamp {0} to month {1}'.format(raw_timestamp, key))
        gas_supplied = int(fields[4])
        return (key, (gas_supplied, 1))
    except:
        pass

def shift_key(x):
    try:
        # key = (to_addr, week number), value = (gas, count)
        # key = to_addr, value = (week_number, gas, count)
        return (x[0][0], (x[0][1], x[1][0], x[1][1]))
    except:
        pass

def read_contract(line):
    try:
        fields = line.split(',')
        return (fields[0], 'Contract')
    except:
        pass

def shift_key_contract(x):
    try:
        # key = to_addr, value = ((week_number, gas, count), 'Contract' or None)
        # key = ('Contract' or 'Wallet', week_number), value = (gas, count)
        addr_type = 'Wallet' if x[1][1] is None else x[1][1]
        week_num = x[1][0][0]
        total_gas = x[1][0][1]
        total_trxn = x[1][0][2]
        return ((addr_type, week_num), (total_gas, total_trxn))
    except:
        pass

def shift_key_results(x):
    try:
        return (x[0][1], (x[0][0], x[1]))
    except:
        pass

transactions = sc.textFile('/data/ethereum/transactions').filter(is_good_line)
contracts = sc.textFile('/data/ethereum/contracts').filter(is_good_line)


step1 = transactions.map(mapper)
step2 = step1.reduceByKey(lambda a, b: (a[0]+b[0], a[1]+b[1]))
step3 = step2.map(shift_key)
step4 = step3.leftOuterJoin(contracts.map(read_contract))
step5 = step4.map(shift_key_contract)
step6 = step5.reduceByKey(lambda a, b: (a[0]+b[0], a[1]+b[1]))
step7 = step6.mapValues(lambda x: x[0]/x[1])
step8 = step7.map(shift_key_results)
step9 = step8.sortByKey()

print('YearMonthWeek,Year,WeekNum,Type,AverageGas')
for row in step9.collect():
    print('{0},{1},{2},{3},{4}'.format(row[0], row[0][0:4], row[0][9:], row[1][0], row[1][1]))

#step4 = step3.sortByKey()

#print('Week, Gas Price in Gwei')
#for row in step4.collect():
    #print('{}, {}'.format(row[0], row[1]))