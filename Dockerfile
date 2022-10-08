FROM python:3.8-slim-buster
LABEL maintainer="mz2716@columbia.edu"

ADD transcription.py .
ADD unit_test_transcription.py .

CMD python -m unittest unit_test_transcription.py -v