# 
FROM python:3.9

# 
WORKDIR /python-product-app

# 
COPY ./requirements.txt /python-product-app/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /python-product-app/requirements.txt

# 
COPY ./app /python-product-app/app

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
