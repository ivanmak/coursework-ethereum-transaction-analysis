# Part B
## Requirement
The requirement of this part was find out the most popular smart contracts on the Ethereum network, in terms of total amount of Ether received, using both MapReduce and Spark.

## Deliverables
The MapReduce programmes produced were:
* [PartB_hadoop.py](./PartB_hadoop.py) - Finding out the most popular smart contracts using MapReduce.
* [PartB_spark.py](./PartB_spark.py) - Finding out the most popular smart contracts using Spark.

## Results
Both programme had produced the same results:
|Contract address|Total Ether received|
| ------------ | ------------ |
|0xaa1a6e3e6ef20068f7f8d8c835d2d22fd5116444|84155100|
|0xfa52274dd61e1643d2205169732f29114bc240b3|45787484|
|0x7727e5113d1d161373623e5f49fd568b4f543a9e|45620624|
|0x209c4784ab1e8183cf58ca33cb740efbf3fc18ef|43170356|
|0x6fc82a5fe25a5cdb58bc74600a40a69c065263f8|27068921|
|0xbfc39b6f805a9e40e77291aff27aee3c96915bdd|21104195|
|0xe94b04a0fed112f3664e45adb2b8915693dd5ff3|15562398|
|0xbb9bc244d798123fde783fcc1c72d3bb8c189413|11983608|
|0xabbb6bebfa05aa13e908eaa492bd7a8343760477|11706457|
|0x341e790174e3a4d35b65fdc067b6b5634a61caea|8379000|

By implmenting the programme in both MapReduce and Spark, the following advantages of using Spark over MapReduce were observed:
- **Less line of codes** – The Spark programme only consists of 15 lines of code while roughly 50 lines were involved in the MRJob framework on Hadoop.
- **Faster execution** – The jobs were executed on both Hadoop and Spark 5 times, and the comparison of the execution time is the following. The main difference between the Hadoop job and the Spark job is that the Hadoop job was actually two steps of MapReduce jobs, and therefore Spark was faster since it did not writing the intermediate results to HDFS.

| **Job** | **Execution #1** | **Execution #2** | **Execution #3** | **Execution #4** | **Execution #5** | **Median** | **Average** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Job 1** | 00:07:56 | 00:08:27 | 00:07:59 | 00:07:40 | 00:08:06 | 00:07:59 | 00:08:02 |
| **Job 2** | 00:00:54 | 00:01:32 | 00:00:40 | 00:00:39 | 00:00:40 | 00:00:40 | 00:00:53 |
| **Total** | **00:08:50** | **00:09:59** | **00:08:39** | **00:08:19** | **00:08:46** | **00:08:46** | **00:08:55** |

When the same job is written and executed on Spark instead, the mean and median execution times were around 2 minutes.
| **Execution #1** | **Execution #2** | **Execution #3** | **Execution #4** | **Execution #5** | **Median** | **Average** |
| --- | --- | --- | --- | --- | --- | --- |
| 02:00:00 | 02:17:00 | 02:07:00 | 01:56:00 | 01:50:00 | 02:00:00 | 02:02:00 |
