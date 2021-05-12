from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob import protocol

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

class PartB_AddressContractsJoin(MRJob):

    OUTPUT_PROTOCOL = protocol.RawValueProtocol

    def steps(self):
        return [MRStep(mapper=self.mapper_join, reducer=self.reducer_join, jobconf={'mapreduce.job.reduces': '8'}),
                MRStep(mapper=self.mapper_wei_to_eth, reducer=self.reducer_sort, jobconf={'mapreduce.job.reduces': '30'})]
    
    def mapper_join(self, _, line):
        try:
            fields = line.split(',')

            if(len(fields) == 5):
                # contracts
                contract_addr = fields[0]
                yield (contract_addr, (0, 0))

            elif (len(fields) == 7):
                # Wei received at each address
                eth_addr = fields[2]
                wei_received = int(fields[3])
                yield (eth_addr, (1, wei_received))
        except:
            pass

    def reducer_join(self, key, values):
        is_contract = False
        wei_received = 0

        for val in values:
            if val[0] == 0:
                is_contract = True
            elif val[0] == 1:
                wei_received += int(val[1])

        if is_contract:
            yield (key, wei_received)

    def mapper_wei_to_eth(self, key, value):
        try:
            if (value > 0):
                value = int(value) / 1000000000000000000
                yield ('sort', (key, value))
        except:
            pass

    def reducer_sort(self, key, value):
        sorted_values = sorted(value, reverse=True, key=lambda x: x[1])

        for i in range(0, min(10, len(sorted_values))):
            eth_received = int(sorted_values[i][1])
            yield (None, '{0},{1}'.format(sorted_values[i][0], int(eth_received)))

if __name__ == '__main__':
    #PartB_AddressContractsJoin.JOBCONF={'mapreduce.job.reduces': '4'}
    PartB_AddressContractsJoin.run()
