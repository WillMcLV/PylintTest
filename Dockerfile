FROM python:3

WORKDIR /home/willm/.local/lib/python3.6

COPY requirements.txt ./

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
    pip install pylint

COPY . .

CMD [ "python", "./pylint.py" ]
