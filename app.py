from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__, static_url_path='/static')

HOST = "0.0.0.0"
PORT = 5000

@app.route('/', methods=["GET"])
def show_page():
    # Create or load a dataframe
    df = pd.DataFrame()
    df['col1'] = list(range(5))
    df['col2'] = list(range(2,7))
    df['col3'] = ['Value 1', 'Value 2', 'Value 3', 'Value 4', 'Value 5']
    # Send values as list of lists
    data = df.values.tolist()
    return render_template('hello.html', data=data)

if __name__ == "__main__":
    app.run(host=HOST, port=PORT)