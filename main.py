from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Получаем данные из формы
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    age = request.form.get('age', '').strip()
    comment = request.form.get('comment', '').strip()

    # === ЗАПИСЬ В ФАЙЛ form.txt ===
    with open('form.txt', 'a', encoding='utf-8') as f:
        f.write(f"Имя: {name}\n")
        f.write(f"Email: {email}\n")
        f.write(f"Возраст: {age}\n")
        f.write(f"Комментарий: {comment}\n")
        f.write("-" * 40 + "\n")

    # Передаём данные на страницу результата
    return render_template('result.html', name=name, email=email, age=age, comment=comment)

if __name__ == '__main__':
    app.run(debug=True)