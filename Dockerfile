FROM ubuntu:latest
LABEL authors="jasur"

ENTRYPOINT ["top", "-b"]