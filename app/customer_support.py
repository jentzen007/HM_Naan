# app/customer_support.py

def respond_to_query(query):
    if "price" in query:
        return "You can check prices on our website."
    elif "hours" in query:
        return "Our hours are 9 AM to 5 PM, Monday through Friday."
    else:
        return "Let me find that information for you."
