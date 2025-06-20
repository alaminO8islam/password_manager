from flask import Blueprint, render_template, request, redirect, url_for
from .encryption import generate_key, encrypt_password, decrypt_password
from .database import get_db_connection

main = Blueprint('main', __name__)

MASTER_PASSWORD = 'admin123'  # You can change this dynamically
key = generate_key(MASTER_PASSWORD)

@main.route('/')
def index():
    conn = get_db_connection()
    items = conn.execute('SELECT * FROM passwords').fetchall()
    return render_template('index.html', items=items)

@main.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        site = request.form['site']
        username = request.form['username']
        password = request.form['password']
        encrypted = encrypt_password(key, password)

        conn = get_db_connection()
        conn.execute('INSERT INTO passwords (site, username, password) VALUES (?, ?, ?)',
                     (site, username, encrypted))
        conn.commit()
        return redirect(url_for('main.index'))
    return render_template('add.html')

@main.route('/view/<int:id>')
def view(id):
    conn = get_db_connection()
    entry = conn.execute('SELECT * FROM passwords WHERE id = ?', (id,)).fetchone()
    decrypted = decrypt_password(key, entry['password'])
    return render_template('view.html', entry=entry, decrypted=decrypted)
