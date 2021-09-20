from flask import Flask, request
from emoji import emojize

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  request_data = request.get_json(force=True, silent=True)
    
  if request_data:
    animal = request_data['animal']
    sound = request_data['sound']
    count = request_data['count']
    result = ''

    for i in range(0, count):
      result += '{} says {}\n'.format(emojize(':{}:'.format(animal)), sound)

    result += 'Made with {} by @don_cabron\n'.format(emojize(':red_heart:'))

    return result

  return 'Please, send me an animal) {}\n'.format(emojize(':hamster:'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
