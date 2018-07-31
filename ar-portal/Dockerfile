FROM python
MAINTAINER DevOps "suresh.polam@jotter.ai"
VOLUME ["/opt/images"]
WORKDIR /opt
COPY requirements.txt /opt/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY images /opt/
COPY static /opt/static
COPY app.py /opt/app.py
RUN chmod +x /opt/app.py
COPY templates /opt/templates
CMD ["python", "app.py"]
