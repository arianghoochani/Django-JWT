From python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /jwt_service/


COPY ./requirements.txt /jwt_service/
RUN pip install -r requirements.txt



COPY . /jwt_service/
