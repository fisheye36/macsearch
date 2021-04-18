FROM python:3.9

RUN mkdir /application
WORKDIR /application

RUN pip install --upgrade pip setuptools

# install dependencies
COPY requirements.txt /application
RUN pip install -r requirements.txt

# install application so that it can be used directly, without python -m <module_name>, or python <script.py>
COPY . /application
RUN pip install .

# keep in mind that anyone with access to the built image can see the API key
# consider supplying environment variable when running the container, not during building
ARG MACSEARCH_API_KEY_ARG
ENV MACSEARCH_API_KEY=$MACSEARCH_API_KEY_ARG

# use docker run <container-name> macsearch <other-mac-address> to query different MAC address
CMD ["macsearch", "44:38:39:ff:ef:57"]
