FROM python:3.10
COPY requirements.txt /stocks_products/requirements.txt
RUN pip install --no-cache-dir -r /stocks_products/requirements.txt
COPY . /stocks_products
WORKDIR stocks_products
EXPOSE 8080
CMD ["gunicorn", "stocks_products.wsgi", "--bind", "0.0.0.0:8080"]
RUN python manage.py collectstatic
