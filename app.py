from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)


def get_computer_choice():
    choices = ['камень', 'ножницы', 'бумага']
    return random.choice(choices)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ничья!"
    elif (user_choice == 'камень' and computer_choice == 'ножницы') or \
            (user_choice == 'ножницы' and computer_choice == 'бумага') or \
            (user_choice == 'бумага' and computer_choice == 'камень'):
        return "Вы победили!"
    else:
        return "Компьютер выиграл!"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/play', methods=['POST'])
def play():
    user_choice = request.json['choice']
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    return jsonify({
        'user_choice': user_choice,
        'computer_choice': computer_choice,
        'result': result
    })


if __name__ == '__main__':
    app.run(debug=True)