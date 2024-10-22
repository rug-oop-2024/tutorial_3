
import streamlit as st

DICTIONARY = {
    "Apple": {
        "price": 1.5,
        "quantity": 1000
    },
    "Banana": {
        "price": 0.5,
        "quantity": 2000
    },
    "Orange": {
        "price": 1.0,
        "quantity": 1500
    },
    "Pineapple": {
        "price": 3.0,
        "quantity": 500
    },
}

CARDS = {
    "1234 1234 1234 1234": {
        "balance": 1000
    },
    "5678 5678 5678 5678": {
        "balance": 2000
    },
    "9876 9876 9876 9876": {
        "balance": 3000
    }
}

st.title("Exercise 1: Wholesale Store")

st.markdown(
"""
Problem: You are the owner of a wholesale store. You have a list of fruits and their prices and quantities. You also have a list of cards and their balances. You want to create a simple app that allows customers to buy fruits and pay with their cards.

"""
)

st.text("Use the following dictionaries")
st.json(DICTIONARY)

st.text("Use the following cards")
st.json(CARDS)

st.markdown("""
Goals:
    - User should be able to select which type of fruit they want to buy
    - User should be able to select which card they want to pay with
    - User should be able to enter the quantity of fruit they want to buy
    - User should be able to see the total price of the purchase
    - User should be able to see the remaining balance of the card
""")