# Part D - Fork Analysis
## Requirement
This part was an optional task of the coursework. The task was to find out whether forks had an effect on the price of Ethereum, and to find out the top ten addresses with the most Ethers received prior to each fork.

## Deliverable
- [./PartD_ForkAnalysis.py](./PartD_ForkAnalysis.py)
- [./PartD_Fork.ipynb](./PartD_Fork)

## Results
A Spark programme “PartD_ForkAnalysis.py” was prepared to extract the Ethereum addresses that received the most Ether since 7 days before each of the forks. Since the forks of EtherGold, Ethereum Modification and EthereumFog happened on the same day, they were counted as the same fork when extracting the data.

Below are the top 10 addresses with the most Ether received since 7 days before each fork.
Fork: Ice Age
| **Address** | **TotalETH** |
| --- | --- |
| **0x32be343b94f860124dc4fee278fdcbd38c102d88** | 508312 |
| **0x6000b846630e4f8ae883a270c118f681bd12e593** | 323203 |
| **0xb794f5ea0ba39494ce839613fffba74279579268** | 299999 |
| **0x2910543af39aba0cd09dbb2d50200b3e800a63d2** | 199042 |
| **0x415655297a0f299d13acce68195890200c5d4a8b** | 124424 |
| **0xa20aa7c6890060f57100f77cc050915b3f336236** | 124424 |
| **0x46785a59acdd53e8b8ddf8b1d8833436259ad77f** | 119495 |
| **0xe93232a5ba251e7d4a6378fc1be81403de561e94** | 96474 |
| **0x0117aca5d98443a8ce8aee7ac4bec8450abbd852** | 44425 |
| **0x120a270bbc009644e35f0bb6ab13f95b8199c4ad** | 40136 |

Fork: Homestead
| **Address** | **TotalETH** |
| --- | --- |
| **0x32be343b94f860124dc4fee278fdcbd38c102d88** | 1420361 |
| **0x60e16961ad6138d2fb3e556fc284d9c2fff41486** | 1000700 |
| **0xb794f5ea0ba39494ce839613fffba74279579268** | 500000 |
| **0x7180eb39a6264938fdb3effd7341c4727c382153** | 369549 |
| **0xcafb10ee663f465f9d10588ac44ed20ed608c11e** | 355935 |
| **0x19ae27e1b61445eb9f27821a5eb4b3e957319e7e** | 290182 |
| **0x120a270bbc009644e35f0bb6ab13f95b8199c4ad** | 258536 |
| **0x2910543af39aba0cd09dbb2d50200b3e800a63d2** | 213937 |
| **0x9c09864b1868637e76b9765cf66b1f842350c147** | 187000 |
| **0x9c6df936c884811b9a6b49f0dd0a62919a6581d4** | 157900 |

Fork: Ethereum Classic
| **Address** | **TotalETH** |
| --- | --- |
| **0x53d284357ec70ce289d6d64134dfac8e511c8a3d** | 8292643 |
| **0x32be343b94f860124dc4fee278fdcbd38c102d88** | 2614071 |
| **0x2910543af39aba0cd09dbb2d50200b3e800a63d2** | 1061268 |
| **0xa2942dc76c4085295b7a6064a1cfa4d93c18d9bb** | 868600 |
| **0x04c973aff06f64b880524f16ae8c821928233ee5** | 828195 |
| **0xb794f5ea0ba39494ce839613fffba74279579268** | 600000 |
| **0x7180eb39a6264938fdb3effd7341c4727c382153** | 361253 |
| **0xa82657936cea2d34f3918539b87d35fc1307f6f1** | 285574 |
| **0x556b5712c2a7cc5506fbfa785b52536fb8243765** | 240000 |
| **0xeba576ee0a26eba945c43cf951118c420f6aa54b** | 223733 |

Fork: Spurious Dragon
| **Address** | **TotalETH** |
| --- | --- |
| **0xaa1a6e3e6ef20068f7f8d8c835d2d22fd5116444** | 944099 |
| **0x7727e5113d1d161373623e5f49fd568b4f543a9e** | 668732 |
| **0xab7c74abc0c4d48d1bdad5dcb26153fc8780f83e** | 600000 |
| **0xcafb10ee663f465f9d10588ac44ed20ed608c11e** | 575462 |
| **0x209c4784ab1e8183cf58ca33cb740efbf3fc18ef** | 540896 |
| **0xc630df154a719aee231fd7c1d22b7b115d14aa54** | 450000 |
| **0xabbb6bebfa05aa13e908eaa492bd7a8343760477** | 301867 |
| **0x02459d2ea9a008342d8685dae79d213f14a87d43** | 265483 |
| **0xfa52274dd61e1643d2205169732f29114bc240b3** | 232632 |
| **0x556b5712c2a7cc5506fbfa785b52536fb8243765** | 190000 |

Fork: Byzantium
| **Address** | **TotalETH** |
| --- | --- |
| **0x7727e5113d1d161373623e5f49fd568b4f543a9e** | 767468 |
| **0xf4b51b14b9ee30dc37ec970b50a486f37686e2a8** | 363184 |
| **0xe94b04a0fed112f3664e45adb2b8915693dd5ff3** | 265902 |
| **0xc257274276a4e539741ca11b590b9447b26a8051** | 219179 |
| **0xfa52274dd61e1643d2205169732f29114bc240b3** | 199489 |
| **0x22b84d5ffea8b801c0422afe752377a64aa738c2** | 179999 |
| **0x6fc82a5fe25a5cdb58bc74600a40a69c065263f8** | 153965 |
| **0x54a2d42a40f51259dedd1978f6c118a0f0eff078** | 138678 |
| **0xa4a6a282a7fc7f939e01d62d884355d79f5046c1** | 130000 |
| **0x209c4784ab1e8183cf58ca33cb740efbf3fc18ef** | 126300 |

Fork: EtherGold, Ethereum Modification, Ether Fog
| **Address** | **TotalETH** |
| --- | --- |
| **0x876eabf441b2ee5b5b0554fd502a8e0600950cfa** | 1583358 |
| **0xf4b51b14b9ee30dc37ec970b50a486f37686e2a8** | 691457 |
| **0x3f5ce5fbfe3e9af3971dd833d26ba9b5c936f0be** | 595452 |
| **0x6fc82a5fe25a5cdb58bc74600a40a69c065263f8** | 428384 |
| **0xe94b04a0fed112f3664e45adb2b8915693dd5ff3** | 348948 |
| **0x6ff73602b0bb13bc9093909a1bde304987fcdf95** | 322720 |
| **0xc613d65747bc36981e9654223369cb3c091b6811** | 320000 |
| **0xb3aaaae47070264f3595c5032ee94b620a583a39** | 241606 |
| **0xfa52274dd61e1643d2205169732f29114bc240b3** | 238788 |
| **0xc257274276a4e539741ca11b590b9447b26a8051** | 230431 |

Fork: Ether Zero
| **Address** | **TotalETH** |
| --- | --- |
| **0x3f5ce5fbfe3e9af3971dd833d26ba9b5c936f0be** | 1277000 |
| **0x876eabf441b2ee5b5b0554fd502a8e0600950cfa** | 723214 |
| **0x6fc82a5fe25a5cdb58bc74600a40a69c065263f8** | 412784 |
| **0xc257274276a4e539741ca11b590b9447b26a8051** | 364300 |
| **0x564286362092d8e7936f0549571a803b203aaced** | 306315 |
| **0xd551234ae421e3bcba99a0da6d736074f22192ff** | 278106 |
| **0x0681d8db095565fe8a346fa0277bffde9c0edbbf** | 250814 |
| **0x22b84d5ffea8b801c0422afe752377a64aa738c2** | 249999 |
| **0x390de26d772d2e2005c6d1d24afc902bae37a4bb** | 237459 |
| **0x01ce8f62037b87291e325b8b0aee01a8bdbf4242** | 236963 |

Fork: Ether Inc
| **Address** | **TotalETH** |
| --- | --- |
| **0x3f5ce5fbfe3e9af3971dd833d26ba9b5c936f0be** | 671325 |
| **0x876eabf441b2ee5b5b0554fd502a8e0600950cfa** | 530360 |
| **0x847ed5f2e5dde85ea2b685edab5f1f348fb140ed** | 420001 |
| **0xf726dc178d1a4d9292a8d63f01e0fa0a1235e65c** | 240796 |
| **0x6fc82a5fe25a5cdb58bc74600a40a69c065263f8** | 230243 |
| **0xfa52274dd61e1643d2205169732f29114bc240b3** | 212242 |
| **0x95cddecd01856aa896426bd1ee021d87f3a5c199** | 184772 |
| **0x564286362092d8e7936f0549571a803b203aaced** | 155394 |
| **0x0681d8db095565fe8a346fa0277bffde9c0edbbf** | 155044 |
| **0xd551234ae421e3bcba99a0da6d736074f22192ff** | 154453 |

Fork: Constantinople
| **Address** | **TotalETH** |
| --- | --- |
| **0x3f5ce5fbfe3e9af3971dd833d26ba9b5c936f0be** | 879895 |
| **0x4e9ce36e442e55ecd9025b9a6e0d88485d628a67** | 829719 |
| **0x876eabf441b2ee5b5b0554fd502a8e0600950cfa** | 431722 |
| **0x5e032243d507c743b061ef021e2ec7fcc6d3ab89** | 366619 |
| **0x6f50c6bff08ec925232937b204b0ae23c488402a** | 276202 |
| **0xdf95de30cdff4381b69f9e4fa8dddce31a0128df** | 273681 |
| **0xb9a4873d8d2c22e56b8574e8605644d08e047549** | 273264 |
| **0x8a288f63b9de32feeedd4c3fc3347f026b599dd1** | 260000 |
| **0x6cc5f688a315f3dc28a7781717a9a798a59fda7b** | 248538 |
| **0xfa52274dd61e1643d2205169732f29114bc240b3** | 244764 |

Referring to the historic price data, not every fork would see a surge in the price of ETH/USD. However, in hard forks, new copies of the Ethereum blockchain would split from the main chain, hence creating new cryptocurrency for all owners at the time of the hard fork. Therefore, the top 10 addresses might still make extra money by selling the new cryptocurrency derived from hard forks immediately.

|Fork|One week price change (US$)|
| ------------ | ------------ |
|Ice Age|-0.10918|
|Homestead|3.16279|
|Ethereum Classic|1.9501|
|Spurious Dragon|-0.21548|
|Byzantium|35.99201|
|EtherGold, Ethereum Modification, Ether Fog|261.408|
|Ether Zero|-234.1|
|Ether Inc|52.13599|
|Constantinople|-9.3846|