from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    bill_amount = float(request.form['bill_amount'])
    discount_card = request.form.get('discount_card')
    is_student = request.form.get('is_student')
    is_saturday = request.form.get('is_saturday')

    # Apply logic to calculate the discounted bill
    discounted_amount = calculate_discount(bill_amount, discount_card, is_student, is_saturday)

    return render_template('result.html', bill_amount=bill_amount, discounted_amount=discounted_amount)

def calculate_discount(bill_amount, discount_card, is_student, is_saturday):
    # Your discount logic goes here
    discount_percentage = 0.5  # 50% discount

    if discount_card:
        bill_amount *= (1 - discount_percentage)

    if is_student and not is_saturday:
        bill_amount *= (1 - discount_percentage)

    return round(bill_amount, 2)

if __name__ == '__main__':
    app.run(debug=True)
