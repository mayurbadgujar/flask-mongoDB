FROM python

WORKDIR /tree

ADD . .

ENTRYPOINT [ "python" ]

CMD [  "app.py"]