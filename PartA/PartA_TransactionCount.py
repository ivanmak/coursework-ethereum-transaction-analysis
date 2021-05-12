from mrjob.job import MRJob
import time

class PartA(MRJob):

    def mapper(self, _, line):
        try:
            fields = line.split(',')
            raw_timestamp = int(fields[6])
            year_month = time.strftime('%Y-%m', time.gmtime(raw_timestamp))
            yield (year_month, 1)
        except:
            pass

    def combiner(self, key, value):
        yield (key, sum(value))

    def reducer(self, key, value):
        yield (key, sum(value))

if __name__ == '__main__':
    PartA.JOBCONF = {'mapreduce.job.reduces': '4'}
    PartA.run()

#Code Ends
