from flask import Flask, render_template, request
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'LocalHost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'ABC@2005'
app.config['MYSQL_DB'] = 'form'
mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def xyz():
    if request.method == 'POST':
        try:
            ticket_form_name = request.form['ticket_form_name']
            ticket_form_number = int(request.form['ticket_form_number'])  # Convert to int
            ticket_form_email = request.form['ticket-form-email']

            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO ticketdata(ticket_form_name, ticket_form_number , ticket_form_email) VALUES(%s, %s, %s)",
                (ticket_form_name, ticket_form_number, ticket_form_email))
            mysql.connection.commit()
            cur.close()
            return "INSERTED SUCCESSFULLY !!"
        except Exception as e:
            # Handle the error, log it, and return an error message
            error_message = f"Error: {str(e)}"
            return error_message
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)