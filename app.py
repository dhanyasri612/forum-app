from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key

# In-memory data storage for simplicity
users = {}
posts = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            return 'User already exists'
        users[username] = password
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if users.get(username) == password:
            session['username'] = username
            return redirect(url_for('dashboard'))
        return 'Invalid credentials'
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', posts=posts)

@app.route('/post', methods=['POST'])
def post():
    if 'username' in session:
        content = request.form['content']
        posts.append({'user': session['username'], 'content': content, 'likes': 0})
    return redirect(url_for('dashboard'))

@app.route('/like/<int:post_id>', methods=['POST'])
def like(post_id):
    if 'username' in session and post_id < len(posts):
        posts[post_id]['likes'] += 1
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/delete/<int:post_id>', methods=['POST'])
def delete(post_id):
    if 'username' in session:
        if post_id < len(posts):
            del posts[post_id]
    return redirect(url_for('dashboard'))


if __name__ == '__main__':
    app.run(debug=True)
