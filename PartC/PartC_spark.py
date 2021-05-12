import pyspark
from operator import add

"""
Blocks layout
0 - number: The block number
1 - hash: Hash of the block
2 - miner: The address of the beneficiary to whom the mining rewards were given
3 - difficulty: Integer of the difficulty for this block
4 - size: The size of this block in bytes
5 - gas_limit: The maximum gas allowed in this block
6 - gas_used: The total used gas by all transactions in this block
7 - timestamp: The timestamp for when the block was collated
8 - transaction_count: The number of transactions in the block
"""

sc = pyspark.SparkContext()

def is_good_line(line):
    try:
        fields = line.split(',')
        if len(fields) == 9:  # blocks
            str(fields[2])  # miner
            if int(fields[4]) == 0: # block size
                return False
        else:
            return False
        return True
    except:
        return False

def mapper(line):
    try:
        fields = line.split(',')

        if len(fields) == 9:
            key = fields[2]
            value = int(fields[5])
            return (key, value)
    except:
        pass

blocks = sc.textFile('/data/ethereum/blocks').filter(is_good_line)
step1 = blocks.map(mapper)
step2 = step1.reduceByKey(add)
step3 = step2.takeOrdered(10, key=lambda x: -x[1])

for record in step3:
    print('{0},{1}'.format(record[0],record[1]))