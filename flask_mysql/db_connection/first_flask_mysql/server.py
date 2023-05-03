from flask import Flask, render_template, request, redirect
# import the class from friend.py
from friend import Friend
app = Flask(__name__)
@app.route("/")
def index():
# call the get all classmethod to get all friends
  all_friends = Friend.get_all()
  print(all_friends)
  return render_template("index.html", friends=all_friends)

@app.route('/friend/show/<int:id>')
def show(id):
  friend=Friend.get_friend_by_id(id)
  return render_template("show_friend.html", friends=friend)

@app.route('/friends/create', methods=['POST'])
def create():
  Friend.save(request.form)
  return redirect('/')
  
@app.route('/friends/update', methods=['POST'])
def update():
  Friend.update(request.form)
  return redirect('/')

@app.route('/friends/delete/<int:id>')
def delete(id):
  Friend.delete(id)
  return redirect('/')

if __name__ == "__main__":
  app.run(debug=True)

