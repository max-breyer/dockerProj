FROM python:3.7
COPY ./bin/ /
RUN pip install --no-cache-dir numpy
CMD ["/entrypoint.py"]
