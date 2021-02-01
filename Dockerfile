FROM continuumio/miniconda3:4.9.2-alpine

COPY . /usr/local/python/

WORKDIR /usr/local/python/

RUN pip3 install pandas==1.2.1 voila-gridstack matplotlib==3.3.4 seaborn numpy~=1.20.0

CMD voila user_interface.ipynb