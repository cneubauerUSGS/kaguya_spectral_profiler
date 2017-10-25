# Spark Stack with Jupyter Notebook 

This is a n-worker spark stack with an associated Jupyter notebook.  To use:

- `docker-compose up -d`
- (optional) `docker-compose logs -f` to watch the system stabalize
- Navigate a browser to `localhost:8080` to see the spark-UI
- (optional) `docker-compose ps` to check on the status
- (optional) `docker-compose scale worker=n` where n is the number of desired
  workers
- `docker-compose logs jupyter` to grab the secret key, e.g.,
  http://localhost:8888/?token=8dd03021db0f3cfc8602d7ed5396f32bcdf47b793f51caf4
- `docker-compose ps` to check the auto-port, e.g.,  `spark_jupyter_1
  tini -- start-notebook.sh          Up
0.0.0.0:32782->8888/tcp`
- In a local browser navigate to
  `localhost:32782/?token=8dd03021db0f3cfc8602d7ed5396f32bcdf47b793f51caf4`.
The port number comes from the previous command.  The rest of the URL comes
from the logs command.
- Create a new notebook and run a little test:

```python
from pyspark import SparkContext

sc = SparkContext(master="spark://master:7077")
rdd = sc.parallelize(range(1000))
rdd.takeSample(False, 5)
``` 

