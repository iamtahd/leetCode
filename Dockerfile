FROM python:3.9

WORKDIR /leetCode

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pre-commit install

COPY . .

RUN virtualenv /venv -ppython3 && /venv/bin/pip install flake8
RUN pre-commit install-hooks
ENV PATH=/venv/bin:$PATH