# Spark Connection to HBase Service

The docker-compose.yml file creates the `snet` network for the spark services
to communicate.  The spark master then connects to an external `vnet` network
that is being used by the HBase services.  This allows the spark service to
access HBase.


## Testing the network

To test this, fire up the HBase stack and let it stabalize.  Then fire up the
spark stack and launch the locally forwarded Jupyter instance.  Then use the
`requests` module to check that the HadoopUI is accessible via one of the name
nodes.

``python
import requests
resp = requests.get('http://namenode-1:50070')
resp.text

# Text blob output
```


## Mounting the HBase config and jars

Spark requires that the hbase-sites.xml file be available.  The necessary `jars` can be pulled dynamically. (Though it would be cleaner to download these into the spark image or mount a volume that contained the commonly used ones: HBase from Hortonworks, CSV from DataBricks, etc.)


## Data locality

When used inside of a swarm, it is going to be more performant to colocate the
spark workers with the regionservers.  This limits scans to local data AFAIK.
