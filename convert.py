from flask import Flask, request

app = Flask(__name__)
 
html = """
<center>
<form action='/convert' method='POST'>
Pound:<input type='text' name='pound' value='{pound}'> lb = <span id='kilo'>{kilo}</span> Kg<br>
<input type='submit' value='Submit'> 
</form>
"""
@app.route("/")
def index():
    lb = 0
    kg = 0
    return html.format(pound=lb, kilo=kg)

@app.route("/convert", methods=['POST'])
def convert():
    try: 
        lb = request.form["pound"]
        kg = int(lb) * 4.535923700000001
    except:                
        return '<h1 style="color:red;">TypeError : Only number please!</h1>'

    return html.format(pound=lb, kilo=kg)
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
