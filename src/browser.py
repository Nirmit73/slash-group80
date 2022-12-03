from flask import Flask, render_template, request
import os
import slash

app = Flask(__name__, template_folder='templates')


@app.route("/")
def main():
    return render_template("UI.html")


@app.route("/", methods=['GET', 'POST'])
def my_form_post():
    if request.method == "POST":
        if request.form['search_item']:
            search_item = request.form['search_item']
        else:
            search_item = ""  # default value

        if request.form['num_item']:
            num_item = int(request.form['num_item'])
        else:
            num_item = 3  # default value

        if request.form['sort_item']:
            sort_item = request.form['sort_item']
        else:
            sort_item = "relevance"  # default value

        if request.form['order_item']:
            order_item = request.form['order_item']
        else:
            order_item = "Ascending"  # default value

        if request.form['email']:
            email = request.form['email']
        else:
            email = ""  # default value

        result = slash.main(search_item, num_item, sort_item, order_item,
                            email)
        # print(result)
    return render_template("UI.html", len=len(result), result=result)


if __name__ == '__main__':
    """
    Execution starts here.
    """
    app.run()
