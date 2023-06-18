# CrawlingChallenge

# How to use it

## Step 1
First of all we have to set up the environment.
For that we have to create the venv and install the dependencies needed.

```
virtualenv crawlingvenv
source crawlingvenv/bin/activate
pip install -r requirements.txt
```
## Step 2
Now that we have the dependencies installed on our venv we have to set up the database with the models defined in CrawlingAPI/models.py

```
cd CrawlingChallenge
python manage.py migrate
```
## Step 3
Our database is ready to save the data of the products, now it's time to run the spider
```
cd CrawlingChallenge
scrapy crawl adidas-spider
```
After this, our spider had taken all the data of adidas products and saved in the database them using the pipeline function

## Step 4
Data have been taken from adidas and saved into our database. It's time to check it.

```
cd ..
python manage.py runserver
```
Doing this we're running the server, it's time to open a browser and navigate to http://127.0.0.1:8000/api/products and we can check all the data of the products.