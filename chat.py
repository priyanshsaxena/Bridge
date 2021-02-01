from flask import Flask,render_template,redirect,request,url_for
from flask_socketio import SocketIO,send

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hello.html')
@app.route('/login')
def login():
    me=request.args.get("nm")
    if me in ["harshit","priyansh","atyant","yash","chandan"]:
        return redirect(url_for('chat',user=me))
    else:
        return "user not found"
@app.route('/chat/<user>')
def chat(user):
    return render_template('chat.html',user=user)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
@socketio.on('message')
def handle_message(message):
    print(message)
    send(message,broadcast=True)
    
if __name__ == '__main__':
    socketio.run(app)   
