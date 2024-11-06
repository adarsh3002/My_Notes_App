from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Using a list to store notes. Each note is a dictionary with 'heading', 'content', and 'color'.
notes = []

@app.route('/')
def index():
    return render_template('index.html', notes=notes)

@app.route('/add_note', methods=['POST'])
def add_note():
    note_heading = request.form.get('note_heading', '').strip()
    note_content = request.form.get('note_content', '').strip()
    note_color = request.form.get('note_color', 'yellow')
    if note_heading and note_content:  # Ensure that both heading and content are not empty
        notes.append({'heading': note_heading, 'content': note_content, 'color': note_color})
    return redirect(url_for('index'))

@app.route('/delete_note/<int:note_id>', methods=['POST'])
def delete_note(note_id):
    if 0 <= note_id < len(notes):
        del notes[note_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
