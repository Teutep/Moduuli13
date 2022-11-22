from flask import Flask

app = Flask(__name__)


@app.route("/alkuluku/<int:number>")
def prime_check(number):
    is_prime = False
    for i in range(2, number):
        if number % i == 0:
            print("Ei ole alkuluku")
            break
    else:
        print("On alkuluku")
        is_prime = True

    answer = {
        "Number": number,
        "isPrime": is_prime
    }

    return answer


if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=5000)