# webapp/app.py
from flask import Flask, request, render_template
from ram.models import ram_plus, tag2text

app = Flask(__name__)
ram_model = ram_plus.load_pretrained('models/ram_plus_swin_large_14m.pth')
tag2text_model = tag2text.load_pretrained('models/tag2text_swin_base.pth')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tag', methods=['POST'])
def tag_image():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        file.save(f'images/{file.filename}')
        tags = ram_model.tag(f'images/{file.filename}')
        return render_template('result.html', result=tags, method='Tagging')

@app.route('/caption', methods=['POST'])
def caption_image():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        file.save(f'images/{file.filename}')
        caption = tag2text_model.caption(f'images/{file.filename}')
        return render_template('result.html', result=caption, method='Captioning')

if __name__ == '__main__':
    app.run(debug=True)
