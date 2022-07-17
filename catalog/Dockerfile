FROM python

RUN mkdir /service
COPY protobufs/ /service/protobufs/
COPY catalog/ /service/catalog/
WORKDIR /service/catalog
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/recommendations.proto

EXPOSE 5000
ENV FLASK_APP=catalog.py
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]