FROM python:3.7
ADD ./bin/
RUN pip install --no-cache-dir numpy
CMD ["./bin/entrypoint.py"]