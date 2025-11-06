FROM python:3.9

WORKDIR /app
COPY . /app

# 安装 requests 和必要的系统库
RUN pip install --no-cache-dir requests

CMD ["python", "host.py"]
