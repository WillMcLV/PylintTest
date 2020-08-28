FROM ubuntu:16.04

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.8 \
    python3-pip \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install nibabel pydicom matplotlib pillow
RUN pip3 install med2image
RUN pip3 install pylint
RUN pip3 install pycodestyle
RUN pip3 install pydocstyle
