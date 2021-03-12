# imports
import flask
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
# initiate our flask application and the keras model

app = flask.Flask(__name__)
model = None

def load_model_for_serving():
    global model
    model = load_model('model/mask_model.h5')

def prepare_text(sentences):
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(sentences)
    sequences = tokenizer.texts_to_sequences(sentences)
    padded = pad_sequences(sequences, truncating='post')

    return padded

@app.route("/predict/",methods=["POST"])
def predict():
    data = {"success": False}
    
    # ensure text was properly "uploaded" at endpoint
    if flask.request.method == "POST":
        # read image
        text = flask.request.files["text"].read()
        # preprocess text
        text = prepare_text(text)

        # make predictions
        preds = model.predict(text)

        return flask.jsonify(preds)

# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
   print(("* Loading Keras model and Flask starting server..."
      "please wait until server has fully started"))
   load_model_for_serving()
   # Add threaded=False if you want to use keras instead of tensorflow.keras
   app.run()