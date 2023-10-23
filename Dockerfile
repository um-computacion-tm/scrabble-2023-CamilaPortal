FROM python:3-alpine
RUN apk update
RUN apk add git
RUN git clone https://github.com/um-computacion-tm/scrabble-2023-CamilaPortal.git
WORKDIR /scrabble-2023-CamilaPortal
RUN pip install -r requirements.txt

CMD [ "sh", "-c", "coverage run -m unittest && coverage report -m && python -m game.main " ]