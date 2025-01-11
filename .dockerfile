FROM python:3.10.15
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["Streamlit","run","app.py"]