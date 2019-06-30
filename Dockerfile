FROM ubuntu:16.04

MAINTAINER Artur Ribeiro <artur.adr@hotmail.com>

RUN apt-get -qq update && apt-get -qq -y install curl bzip2 \
    && curl -sSL https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -o /tmp/miniconda.sh \
    && bash /tmp/miniconda.sh -bfp /usr/local \
    && rm -rf /tmp/miniconda.sh \
    && conda install -y python=3 \
    && conda update conda \
    && apt-get -qq -y remove curl bzip2 \
    && apt-get -qq -y autoremove \
    && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/* /var/log/dpkg.log \
    && conda clean --all --yes

ENV PATH /opt/conda/bin:$PATH

RUN mkdir /easyResource/

WORKDIR /easyResource/

RUN apt-get -qq update && apt-get -qq -y install postgresql

COPY / /easyResource

WORKDIR /easyResource/

RUN conda install psycopg2

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

ENTRYPOINT bash entrypoint.sh