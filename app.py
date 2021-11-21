import os
import numpy as np
import tensorflow
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

GPUs = tensorflow.config.experimental.list_physical_devices('GPU')
for GPU in GPUs:
    tensorflow.config.experimental.set_memory_growth(GPU, True)

app = Flask(__name__)


def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(160, 120))

    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    predictions = model.predict(x)
    return predictions


cells = ['Eosinophil', 'Lymphocyte', 'Monocyte', 'Neutrophil']

descriptions = [
    'Eosinophils are a type of disease-fighting white blood cell. This condition most often indicates a parasitic infection, an allergic reaction or cancer. You can have high levels of eosinophils in your blood (blood eosinophilia) or in tissues at the site of an infection or inflammation (tissue eosinophilia).',
    'Lymphocytes are white blood cells that are also one of the body’s main types of immune cells. They are made in the bone marrow and found in the blood and lymph tissue.The immune system is a complex network of cells known as immune cells that include lymphocytes. These cells work together to defend the body against foreign substances, such as bacteria, viruses, and cancer cells that can threaten its functioning.',
    'Monocytes are a type of leukocyte, or white blood cell. They are the largest type of leukocyte and can differentiate into macrophages and conventional dendritic cells. As a part of the vertebrate innate immune system monocytes also influence the process of adaptive immunity. They fight certain infections and help other white blood cells remove dead or damaged cells and fight cancer cells.',
    'Neutrophils are the most abundant type of granulocytes and make up 40% to 70% of all white blood cells in humans. They form an essential part of the innate immune system, with their functions varying in different animals. Neutropenia is a blood condition characterized by low levels of neutrophils, which are white blood cells that protect your body from infections. Without enough neutrophils, your body can\'t fight off bacteria. Having neutropenia increases your risk for many types of infection.']


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    f = request.files['file']
    MODEL_PATH = 'model-blood-cell.h5'

    model = load_model(MODEL_PATH)
    model.make_predict_function()

    basePath = os.path.dirname(__file__)
    file_path = os.path.join(basePath, secure_filename(f.filename))
    predictions = model_predict(file_path, model)
    return cells[np.argmax(predictions)] + " cells were detected. " + descriptions[np.argmax(predictions)]


if __name__ == '__main__':
    app.run(debug=True)
