FROM python:3

WORKDIR /home/fujii/oca_lecture

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./test_python.py"]

