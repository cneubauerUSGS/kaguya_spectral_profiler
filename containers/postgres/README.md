# PostGreSQL container

This stack consists to two containers: (1) a PostGreSQL 9.6 container with POSTGIS enabled and (2) a pgadmin4 container.  The former is accessible on port 5432 on the internal network and port 8001 on the external network.  The latter is running in destktop mode without any login/password.  This is **not** the way to run this as a service that will be externally accessible.

- To launch in single node mode: `docker-compose up`
- To launch in swarm mode that could be distirbuted over multiple machines: `docker stack deploy -c docker-compose.yml <service name>`

Once the service is up, you can access pgadmin4 on `localhost:5050`.  To connect to postgres:

- hostname: db
- port: 5432  # Access is via the private network
- login: jay
- password: abcde

PostGreSQL is expecting to be able to mount a data directory from /media/fast/postgres on the host to the standard /var location on the container.
