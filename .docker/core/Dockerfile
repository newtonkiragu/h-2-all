# Define a minimal docker container
FROM python:3.7.1-alpine3.7

#requirements installation
RUN apk update && apk add  --no-cache --update postgresql-dev\
                                                gcc python3-dev\
                                                py3-pip\
                                                musl-dev\
                                                bash
# Define production|development environment variable
ENV ENVIRONMENT production

# Prevent stdout to be buffered
ENV PYTHONUNBUFFERED 1

# Exporse a specific port
ENV PORT 8000

# Expose the number of workers based on CPU
ENV WORKERS 1

# Expose the type of worker class
ENV WORKERCLASS sync

RUN mkdir -p /opt/h2_all_core
WORKDIR /opt/h2_all_core
ADD ./h2_all_core /opt/h2_all_core
RUN pip3 install -r requirements.txt
RUN chmod +x start_h2_all_core.sh
EXPOSE ${PORT}