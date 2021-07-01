# HDFS - Hadoop Distributed File System

Computing power + fault tolerant

Distribute large file in 64Mo chunks on datanodes on the network
Chunks are dispatched by the namenode (central server)
Each chunk is replicated on 3 distincts serveurs (fault tolerant)
Namenode 
    manage the datanodes 
    dispatch the chunck on datanodes
    is replicated with a secondary namenode
Datanodes
    Store chunks 
    Process data (map/reduce)

    Elastic
    - new datanode gets its neighbours chunks
    - removed datanode: its neighbours replicate its chunks

! [hdfs](assets/books/data/assets/hdfs.png)

## More

- https://openclassrooms.com/courses/creez-votre-data-lake