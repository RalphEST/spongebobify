from chalice import Chalice
import random as rd
app = Chalice(app_name='helloworld')
app.debug = True

@app.route('/spongebobify/{text}')
def spongebobify(text):
    mod_text = ''
    for c in text:
        if rd.randint(1,100)>=50: 
            mod_text += c.lower()
        else:
            mod_text += c.upper()
    return {'spongebobified': mod_text}
