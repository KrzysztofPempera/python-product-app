# python-product-app

## Features
* Api endpoint "deals" which creates csv with promotional data about two sets of products
* Api endpoint "index" that identifies product's type based on the input model, calculates it's profitability index and returns that data as a csv

## Requirements

Python 3.10+

## Instalation

<div class="termy">

```console
$ pip install requirements.txt

```
</div>

### Run it

Run the app with:

<div class="termy">

```console
$ uvicorn main:app --reload

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28720]
INFO:     Started server process [28722]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
</div>

Run the tests with:
<div class="termy">

```console
$ pytest

```
</div>

### Check it

Open your browser at <a href="http://127.0.0.1:8000" class="external-link" target="_blank">http://127.0.0.1:8000</a>.

You will be redirected to the swagger page. You can try out two api endpoints:
* The _path_ `/index/` has a _query parameter_ `model` that should be a name of an existing pc or laptop model, f.e.'pc-model' or 'laptop-model'. It returns a csv file with model type and it's profitability index.
* The _path_ `/deals/` that, when executed, returns a csv of two promotional sets.
