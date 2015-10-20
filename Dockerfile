FROM python:3.5
COPY ats.client /app/ats.client
COPY ats.util /app/ats.util
COPY ats.senza /app/ats.senza
WORKDIR /app/ats.senza
RUN pip install --no-cache-dir --disable-pip-version-check -r requirements/dev.txt
RUN echo "[session]\nserver_url = http://localhost:8083\n" | install -m 0700 /dev/fd/0 /app/ats.senza/senza-client.ini
CMD sleep 10 && senza-server
