from mrjob.job import MRJob
import time

class PartA2(MRJob):

    def mapper(self, _, line):
        try:
            fields = line.split(',')
            raw_timestamp = int(fields[6])
            trxn_value = float(fields[3]) / 1000000000000000000
            year_month = time.strftime('%Y-%m', time.gmtime(raw_timestamp))
            yield (year_month, {'count': 1, 'trxn_value': trxn_value})
        except:
            pass

    def combiner(self, key, value):
        total_value = 0.0
        total_count = 0

        for val in value:
            total_count += val['count']
            total_value += val['trxn_value']

        result = { 'count': total_count, 'trxn_value': total_value }

        yield (key, result)

    def reducer(self, key, value):
        total_value = 0.0
        total_count = 0

        for val in value:
            total_count += val['count']
            total_value += val['trxn_value']

        avg_value = total_value / total_count

        yield (key, avg_value)

if __name__ == '__main__':
    PartA2.JOBCONF = {'mapreduce.job.reduces': '4'}
    PartA2.run()

#Code Ends
