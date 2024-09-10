# Prerequisites

make a virtual environment 

```
python -m venv venv
source venv/bin/activate
```

and then install the requirements 

```
pip install beautifulsoup4
pip install requests
pip install playsound

```


# functions :

1- ```main_clicker.py```
This is a better version since it clicks on the available ticket and open the browser for you so you can react in due time

2- ``` main.py```

This will see when the ticket is available and open the page for you so you can choose it yourself. It can also take an input, setting a maximum price of tickets its searching for.

Example usage, searching for tickets under 300 DKK

``` main.py --price_limit 300```

It will also show the amount of available tickets, and the price of the lowest priced available ticket while searching.


# How to use:
```
python main_clicker.py
```
or
```
python main_clicker.py
```
or (searching for tickets below specific threshold - Example 300 DKK)
```
python main --price_limit 300
```
or (searching for tickets at specific rate limit)
```
python main --rate_limit 4
```

# Expected results
when it works , it will open a browser page like seen below , and take your time and put the information and finalize the purchase. 
![image](https://github.com/user-attachments/assets/fb2ea57c-9b6e-429f-9e08-b9952221c29d)

