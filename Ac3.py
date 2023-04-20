from flask import Flask

app = Flask(__name__)

def is_prime(num):
    #Função para verificar se um número é primo.
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

@app.route('/')
def display_primes():
    #Rota para exibir os 100 primeiros números primos.
    primes = []
    num = 2
    while len(primes) < 100:
        if is_prime(num):
            primes.append(num)
        num += 1
    return ', '.join(map(str, primes))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)