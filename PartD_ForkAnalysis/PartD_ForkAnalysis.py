import pyspark
from datetime import datetime
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
"""

sc = pyspark.SparkContext()

fork_blocks = [200000, 1150000, 1920000, 2675000, 4370000, 4730666, 4936270, 5078585, 7280000]

fork_times = [ datetime(2015,9,8), datetime(2016,3,15), datetime(2016,7,20), datetime(2016,11,23), datetime(2017,10,16),
               datetime(2017,12,14), datetime(2018,1,19), datetime(2018,2,13), datetime(2019,2,28)]

fork_names = ['Ice Age', 'Homestead', 'Ethereum Classic', 'Spurious Dragon', 'Byzantium', 'EtherGold+EtherModification+Ether Fog',
              'Ether Zero', 'Ether Inc', 'Constantinople']


def is_good_line(line):

    try:
        fields = line.split(',')
        if len(fields) == 7: # transactions
            str(fields[2]) # to_addr
            int(fields[5])
            raw_timestamp = int(fields[6])
            block_number = int(fields[0])

            # Check if the transaction is within 1 week before hard fork
            transaction_time = datetime.fromtimestamp(raw_timestamp)

            count = 0
            beforeFork = False
            for t in fork_times:
                diff = (t - transaction_time).total_seconds()

                fork_block = fork_blocks[count]

                if diff > 0 and diff <= 604800 and block_number < fork_block:
                    beforeFork = True

                count = count + 1
        else:
            return False
        return (beforeFork and int(fields[3])>0)
    except:
        return False

def mapper(line):
    try:
        fields = line.split(',')
        block_num = int(fields[0])
        to_addr = str(fields[2])
        wei = int(fields[3])
        raw_timestamp = int(fields[6])

        # find out which fork
        transaction_time = datetime.fromtimestamp(raw_timestamp)

        count = 0
        beforeFork = False
        
        for t in fork_times:
            diff = (t - transaction_time).total_seconds()

            fork_block = fork_blocks[count]

            if diff > 0 and diff <= 604800 and block_num < fork_block:
                beforeFork = True
                fork_name = fork_names[count]

            count = count + 1

        if beforeFork and wei > 0:
            return ((fork_name, to_addr), wei)
    except:
        pass


transactions = sc.textFile('/data/ethereum/transactions').filter(is_good_line)

step1 = transactions.map(mapper)
step2 = step1.reduceByKey(add)
step3 = step2.mapValues(lambda x: float(round(x/1000000000000000000)) if x > 0 else 0)
step4 = step3.sortBy(lambda x: -x[1])

fork_listed = []
for i in range(0, len(fork_names)):
    fork_listed.append(0)

print('Fork,Address,TotalETH')
for row in step4.take(100000):
    i = fork_names.index(row[0][0])

    if fork_listed[i] < 10:
        print ('{},{},{}'.format(row[0][0], row[0][1], row[1]))
        fork_listed[i] = fork_listed[i] + 1

    if sum(fork_listed) >= 120:
        break
