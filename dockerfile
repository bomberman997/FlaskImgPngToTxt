FROM ubuntu

WORKDIR /src

RUN apt-get update && apt-get install tesseract-ocr -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y

COPY src/ .

RUN pip install -r requirements.txt 

RUN apt-get --fix-missing update && apt-get --fix-broken install && apt-get install -y poppler-utils && apt-get install -y tesseract-ocr && \
    apt-get install -y libtesseract-dev && apt-get install -y libleptonica-dev && ldconfig && apt install -y libsm6 libxext6

RUN pip install pytesseract
RUN pip install numpy
RUN pip install pandas

RUN mkdir /output

EXPOSE 8080

# command to run on container start
CMD [ "python3", "/src/server.py" ]

