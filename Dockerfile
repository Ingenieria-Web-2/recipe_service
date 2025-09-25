FROM python:3.13

WORKDIR /usr/src/recipe_service/

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /usr/src/recipe_service/app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]