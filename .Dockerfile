FROM continuumio/miniconda3:4.11.0
RUN mkdir /home/minefraft-ai/
WORKDIR /home/minefraft-ai/
ADD . /home/minefraft-ai/
RUN pip install -r requirements.txt