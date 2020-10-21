FROM latonaio/l4t:latest

ENV POSITION=Runtime \
    SERVICE=microservice-watch \
    AION_HOME="/var/lib/aion"

# Setup Directoties
RUN mkdir -p ${AION_HOME}/$POSITION/$SERVICE
WORKDIR ${AION_HOME}/$POSITION/$SERVICE/

ADD . .

CMD ["python3", "-u" ,"main.py"]
