from flask import Flask, render_template, request
import re
import sqlite3
app = Flask(__name__)
import sqlite3
conn = sqlite3.connect('customer_service.db',check_same_thread=False)

c = conn.cursor()

@app.route('/')
def welcome():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def result():
    var_1 = request.form.get("var_1", type=int, default=0)
    var_3 = request.form.get("var_1", type=int, default=0)

    var_2 = request.form.get("var_2", type=str, default=0)

    def is_discord_username(string) -> bool:
        return re.match(r'^[a-zA-Z0-9]#[0-9]{4}$', string) is not None
    is_discord_username(var_2)
    operation = request.form.get("operation")
    operation2 = request.form.get("operation2")
    operation3 = request.form.get("operation3")
    var_1 = var_1 * 5
    contain = '#'

    if(operation == 'Low'):
        light_price = 15
        result = var_1 + light_price

    elif(operation == 'Mid'):
        light_price = 25

        result = var_1 + light_price
    elif(operation == 'High'):
        light_price = 35
        result = var_1 + light_price

    else:
        result = 'invaild inputs'
    if(operation2 == 'custom'):
        result = result + 20
    elif (operation2 == 'ingame animation'):
        result = result + 10
    elif (operation2 == 'already made by you'):
        result = result + 10
    if(operation3 == 'rain'):
        result = result + 20
    elif (operation3 == 'snow'):
        result = result + 15
    elif (operation3 == 'none'):
        result = result + 0
    oorder = (var_1,operation,operation2,operation3)
    entry = result
    Resulllt = str(var_3) + ',' + operation + ',' + operation2 + ',' + operation3
    c.execute("insert into customer_orders(discord_username,order1,price)VALUES ('{}','{}','{}');".format(var_2,Resulllt, result))
    conn.commit()
    return render_template('form.html', entry=entry)

if __name__ == '__main__':
    app.run(debug=True)
