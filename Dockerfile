# Base Python image for container
FROM python:3.7

# Set unbuffered output to make sure all logs are printed and not stuck in buffer
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN mkdir -p /drishtee

# Copy and install requirements
ADD requirements /drishtee/requirements
RUN pip install --upgrade pip
RUN pip install -r /drishtee/requirements/common.txt && pip install -r /drishtee/requirements/dev.txt

ADD . /drishtee/
WORKDIR /dristee
RUN pip install -e .

ENV PYTHONPATH=/drishtee

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
EXPOSE 8000
ENTRYPOINT ["/entrypoint.sh"]
