FROM python:3.8
COPY . /radamel
WORKDIR /radamel
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["radamel.py"]