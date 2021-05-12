from mrjob.job import MRJob
import time

class PartC(MRJob):

    def mapper(self, _, line):
        try:
            fields = line.split(',')
            miner = fields[2]
            mined_size = int(fields[5])
            yield (miner, mined_size)
        except:
            pass

    def combiner(self, key, value):
        yield (key, sum(value))

    def reducer(self, key, value):
        yield (key, sum(value))

if __name__ == '__main__':
    PartC.JOBCONF = {'mapreduce.job.reduces': '4'}
    PartC.run()

#Code Ends
