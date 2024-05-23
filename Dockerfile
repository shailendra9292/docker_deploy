FROM python:latest
WORKDIR /app
COPY . /app/
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000 8501
CMD ["python", "run_servers.py"]