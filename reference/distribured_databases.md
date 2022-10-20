## Distributed database

A distributed database is a database in which data is stored across different physical locations.
It may be stored in multiple computers located in the same physical location (e.g. a data centre);
or maybe dispersed over a network of interconnected computers. 

## [Cassandra](https://cassandra.apache.org/_/index.html)


Cassandra is an open-source NoSQL data storage system that leverages a distributed architecture to enable high availability and reliability, managed by the Apache non-profit organization.

### Key Features:

- Distributed
- Schema free
- Fault tolerance
- Cassandra Query Language
- Scalability
- Open source availability


## [Hadoop](https://hadoop.apache.org/)

The Apache Hadoop software library is a framework that allows for the distributed processing of
large data sets across clusters of computers using simple programming models.
It is designed to scale up from single servers to thousands of machines, each offering local
computation and storage. 

The project includes these modules:

- Hadoop Common: The common utilities that support the other Hadoop modules.
- Hadoop Distributed File System (HDFS™): A distributed file system that provides high-throughput access to application data.
- Hadoop YARN: A framework for job scheduling and cluster resource management.
- Hadoop MapReduce: A YARN-based system for parallel processing of large data sets.

### Key Features

- Open Source
- Highly Scalable Cluster
- Fault Tolerance
- High Availability
- Cost-Effective

## [ClickHouse](https://clickhouse.com/docs/ru/)

ClickHouse® is a column-oriented database management system (DBMS) for online analytical processing of queries (OLAP).
ClickHouse’s performance exceeds all other column-oriented database management systems. 
It processes billions of rows and tens of gigabytes of data per server per second.

### Key Features:

- True Column-Oriented Database Management System
- Data Compression
- Parallel Processing on Multiple Cores
- Distributed Processing on Multiple Servers
- Real-Time Data Inserts

## Comparison

|       Feature       |           Cassandra            |              Hadoop               |                                        ClickHouse                                         | 
|:-------------------:|:------------------------------:|:---------------------------------:|:-----------------------------------------------------------------------------------------:|
|      Ecosystem      |               +                |                 +                 |                                             -                                             |
|     Open source     |               +                |                 +                 |                                             +                                             | 
|    Solution Type    |             NoSQL              | Distributed data storage solution |                                 column-oriented for OLAP                                  | 
|   Query Language    |              CQL               |              HiveQL               |                                            SQL                                            | 
| Read/Write politics | Writing is faster than reading |       Write once Read many        |                               Fast write, fast read by cols                               | 
|     Schema free     |               +                |                 -                 |                                             -                                             |
|        ACID         |  ACID transactions are coming  |           Hive has ACID           | + (INSERT into one partition in one table of MergeTree family up to max_insert_size rows) |

## Case

Using Yandex.Metrica on a multi-page site with about 500,000 visitors per day (for example, a news resource).

All traffic details and user events must be stored in a database. Thus, we have a big data with high granularity.
Also, we need high read performance, the ability to perform parallel analytical queries on individual columns, 
so it's good to use **ClickHouse**.