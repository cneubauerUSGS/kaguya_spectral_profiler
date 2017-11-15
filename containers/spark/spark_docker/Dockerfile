FROM singularities/hadoop:2.7

# Version
ENV SPARK_VERSION=2.2.0
ENV HBASE_VERSION=1.2.6

# Set home
ENV SPARK_HOME=/usr/local/spark-$SPARK_VERSION

# Install PY3 via Miniconda in order to match Jupyter container 
RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git mercurial subversion

RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget https://repo.continuum.io/miniconda/Miniconda3-4.3.27-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh

RUN apt-get install -y curl grep sed dpkg && \
    TINI_VERSION=`curl -k https://github.com/krallin/tini/releases/latest | grep -o "/v.*\"" | sed 's:^..\(.*\).$:\1:'` && \
    curl -k -L "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb" > tini.deb && \
    dpkg -i tini.deb && \
    rm tini.deb && \
    apt-get clean

ENV PATH=/opt/conda/bin:$PATH

# Install Spark
RUN mkdir -p "${SPARK_HOME}" \
  && export ARCHIVE=spark-$SPARK_VERSION-bin-without-hadoop.tgz \
  && export DOWNLOAD_PATH=apache/spark/spark-$SPARK_VERSION/$ARCHIVE \
  && curl -L -k https://mirrors.ocf.berkeley.edu/$DOWNLOAD_PATH | \
    tar -xz -C $SPARK_HOME --strip-components 1 \
  && rm -rf $ARCHIVE
COPY spark-env.sh $SPARK_HOME/conf/spark-env.sh
ENV PATH=$PATH:$SPARK_HOME/bin

# Ports
EXPOSE 6066 7077 8080 8081

# Copy start script
COPY start-spark /opt/util/bin/start-spark
RUN chmod +x /opt/util/bin/start-spark
ENV PATH=$PATH:/opt/util/bin/

# Fix environment for other users
RUN echo "export SPARK_HOME=$SPARK_HOME" >> /etc/bash.bashrc \
  && echo 'export PATH=$PATH:$SPARK_HOME/bin'>> /etc/bash.bashrc

# Copy the HBase plugin
COPY shc-core-1.1.2-2.2-s_2.11.jar $SPARK_HOME/jars/shc-core-1.1.2-2.2-s_2.11.jar

# Install the HBase jars
# Download and inject the HBase jars as well                                    
RUN wget http://apache.claz.org/hbase/${HBASE_VERSION}/hbase-${HBASE_VERSION}-bin.tar.gz && \
    tar xzf hbase-${HBASE_VERSION}-bin.tar.gz -C /usr/local && \                
    rm hbase-${HBASE_VERSION}-bin.tar.gz 
ENV HBASE_HOME = /usr/local/hbase-${HBASE_VERSION}

# Add deprecated commands
#RUN echo '#!/usr/bin/env bash' > /usr/bin/master \
#  && echo 'start-spark master' >> /usr/bin/master \
#  && chmod +x /usr/bin/master \
#  && echo '#!/usr/bin/env bash' > /usr/bin/worker \
#  && echo 'start-spark worker $1' >> /usr/bin/worker \
#  && chmod +x /usr/bin/worker
