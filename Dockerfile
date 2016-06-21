FROM python:2.7-onbuild
ENV LD_LIBRARY_PATH /usr/local/lib:/usr/local/bin/python
CMD [ "python", "./run.py" ]
