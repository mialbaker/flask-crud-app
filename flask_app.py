from flask import Flask, render_template, request
import logging

app = Flask(__name__)

global dictionary
dictionary = dict()

# Homepage
@app.route("/")
def crud_page():
    return render_template("/homepage.html")

# SET
@app.route("/set_page")
def post_page():
    return render_template("/set_page.html")

# Update dictionary
@app.route("/set_element", methods=['POST'])
def set_element():
    namespace = request.form["namespace"]
    key = request.form["key"]
    val = request.form["value"]

    if not namespace or not key or not val:
        logging.warning(f"Empty parameter.")
        return render_template("/error_empty.html")
    if namespace not in dictionary:
        dictionary[namespace] = dict()
    dictionary[namespace][key] = val
    logging.info(f"Namespace: {namespace}, Key: {key}, Value: {val} added to dictionary")

    return render_template("/set_success.html", namespace=namespace, key=key, val=val)

# GET
@app.route("/get_page")
def the_get_page():
    return render_template("/get_page.html", retrieve_dictionary=dictionary)

# Retrieve from dictionary
@app.route("/get_element", methods=['POST'])
def get_element():
    namespace = request.form["namespace"]
    key = request.form["key"]

    if not namespace or not key:
        logging.warning(f"Empty parameter.")
        return render_template("/error_empty.html")
    if namespace not in dictionary:
        logging.warning(f"Namespace: {namespace} not in dictionary.")
        return render_template("/error_not_found.html")
    if key not in dictionary[namespace]:
        logging.warning(f"Key: {key} not in {namespace}.")
        return render_template("/error_not_found.html")

    val = dictionary[namespace][key]
    logging.info(f"Namespace: {namespace}, Key: {key}, Value: {val} retrieved from dictionary")

    return render_template("/get_success.html", namespace=namespace, key=key, val=val)

# PRINT DICTIONARY
@app.route("/print_dictionary_page")
def the_print_dictionary_page():
    return render_template("/print_dictionary_page.html", retrieve_dictionary=dictionary)

# DELETE
@app.route("/delete_page")
def the_delete_page():
    return render_template("/delete_page.html", retrieve_dictionary=dictionary)

@app.route("/delete_element", methods=['POST'])
def delete_element():
    namespace = request.form["namespace"]
    key = request.form["key"]

    if not namespace or not key:
        logging.warning(f"Empty parameter.")
        return render_template("/error_empty.html")
    if namespace not in dictionary:
        logging.warning(f"Namespace: {namespace} not in dictionary.")
        return render_template("/error_not_found.html")
    if key not in dictionary[namespace]:
        logging.warning(f"Key: {key} not in {namespace}.")
        return render_template("/error_not_found.html")
    
    del dictionary[namespace][key]
    logging.info(f"Namespace: {namespace}, Key: {key} deleted from dictionary")

    if not dictionary[namespace]:
        del dictionary[namespace]
        logging.info(f"Namespace: {namespace} deleted from dictionary")
        
    return render_template("/delete_success.html")

# COUNT
@app.route("/count_page")
def the_count_page():
    return render_template("/count_page.html", retrieve_dictionary=dictionary)

@app.route("/count_element", methods=['POST'])
def count_element():
    namespace = request.form["namespace"]
    val = request.form["value"]
    count = 0

    if not namespace or not val:
        logging.warning(f"Empty parameter.")
        return render_template("/error_empty.html")
    if namespace not in dictionary:
        logging.warning(f"Namespace: {namespace} not in dictionary.")
        return render_template("/error_not_found.html")

    for v in dictionary[namespace].values():
        if v == val:
            count += 1
    logging.info(f"Count of value: {val} in namespace: {namespace} is {count}.")
    
    return render_template("/count_success.html", namespace=namespace, val=val, count=count)

# COUNT GLOBAL
@app.route("/count_global_page")
def the_count_global_page():
    return render_template("/count_global_page.html", retrieve_dictionary=dictionary)

@app.route("/count_global_element", methods=['POST'])
def count_global_element():
    val = request.form["value"]
    count = 0

    if not val:
        logging.warning(f"Empty parameter.")
        return render_template("/error_empty.html")
    for namespace in dictionary:
        for v in dictionary[namespace].values():
            if v == val:
                count += 1
    logging.info(f"Count of value: {val} is {count}.")
    
    return render_template("/count_global_success.html", val=val, count=count)

if __name__== '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)