# 🐳 Dockerfile pour XTTS Sol

FROM python:3.10

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

EXPOSE 8020
CMD ["python3", "app.py"]
