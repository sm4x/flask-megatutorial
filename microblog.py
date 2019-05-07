from app import app, db

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

# Run from Main Program
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
