from flask import Flask, render_template, request
from flask_mysqldb import MySQL


app = Flask(__name__)

# Configure db

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'v2ghawana'
app.config['MYSQL_DB'] = 'prediction'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        gender = userDetails['gender']
        married = userDetails['married']
        dependents = userDetails['dependents']
        education = userDetails['education']
        employed = userDetails['employed']
        credit = userDetails['credit']
        area = userDetails['area']
        ApplicantIncome = userDetails['ApplicantIncome']
        CoapplicantIncome = userDetails['CoapplicantIncome']
        LoanAmount = userDetails['LoanAmount']
        Loan_Amount_Term = userDetails['Loan_Amount_Term']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO newprediction(gender,married,dependents,education,employed,credit,area,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term) VALUES(%s, %s, %s,%s, %s, %s, %s, %s,%s, %s ,%s)",(gender,married,dependents,education,employed,credit,area,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)