FROM python:3.12

# 设置工作目录为/app
WORKDIR /app

# 将当前目录内容复制到容器的/app内
ADD . /app

# 安装任何需要的包
RUN pip install --no-cache-dir -r requirements.txt

# 收集静态文件到staticfiles目录
RUN python manage.py collectstatic --no-input

# 对外暴露的端口号
EXPOSE 8000

# 当容器启动时运行python app.py
CMD ["gunicorn", "write_future.wsgi:application", "--bind", "0.0.0.0:8000"]
