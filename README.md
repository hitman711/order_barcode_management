# Order Barcode management
Application read customer order and ordered barcode data from a CSV file, Match order numbers with barcode and generate new CSV file which contains customer_id, order_id and list of barcodes.

Requirements
------------

* **Python**        : 3.4+
* **Pandas**        : 0.24+

Installation
------------
1. Create a Virtual environment using python3

.. code-block:: sh

    python3 -m venv .env

2. Activate the environment

.. code-block:: sh

    source .env/bin/activate

3. Install dependencies

.. code-block:: sh

    pip install -r requirements.txt

4. Run code

    python index.py

Explanation
------------
Python pandas library used for data manipulation and analysis. Pandas provide the feature to read CSV file and convert it into JSON, DICT, LIST, TIME SERIES.

In code there are 3 function `order_set`, `barcode_set` and `filter_operation`(main function).

`order_set` read data from orders.csv file(CSV file contain "customer_id", and "order_id") using pandas. Pandas read_csv function convert CSV data to pandas dataset. Using pandas we clear out empty rows. Using pandas pivot table and aggregate function we print top 5 customers who have maximum orders. function will return order_dataset value.

`barcode_set` read data from barcodes.csv file(CSV file contain "barcode" and "order_id") using pandas. We first calculate and print total no barcode which are not linked with orders. Then we remove those barcodes from the remaining list. Using pandas group by the function we return a dataset of order_id and list of barcodes

    ```
    Ex. order_id    barcode
        1           [1111111, 1111112]
    ```

`filter_operation` is a main function which initializes `order_set`, `barcode_set` function. filter function merges both datasets using "order_id" column and generates a new dataset with all matching rows. Using new dataset we calculate and print a total number of orders which don't have any barcode assign. Reinitialize the order new dataset for output file i.e.`customer_id`, `order_id`, `barcode_id`.
