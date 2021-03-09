# Sentiment Classification

**Sentiment Classification**

Sentiment classification is the task of analyzing a piece of text and predicting if someone dislikes the thing they’re talking about.

**Input:** Piece of text

**Output:** Sentiment

**Dataset**

I am using the [IMDB Movie Review Dataset](https://www.tensorflow.org/datasets/catalog/imdb_reviews) for my model training, it contains two columns

**Preprocessing**

**Tokenization**

Tokenization is the process of splitting a text, phrase, sentence, document into smaller “chunks” or “tokens”

**Ex:** “Hey there, long time no see”

**Tokens:** ‘Hey’, ‘there’, ‘long’, ‘time’, ‘no’, ‘see’

Smaller units or tokens are created by locating word boundaries, word boundaries are the ending point of a word, and the beginning of the next word.

**Sequencing & Padding**

Sequencing is used for using our text as an input layer in a neural network

“Hey there”, “Hey there delilah”

[[‘1 2’], [‘1’, ‘2’, ‘3’]]

Padding is done to make the vector input of the same size

[[1,2]

[1,2,3]]

A corpus will have sentences of different sizes, as shown above in the example.

Padding is done to make them of the same size

[[0 1 2]

[1   2 3]]

**Model**

[https://lh6.googleusercontent.com/XxinSccKk_ibw_N1Hh7PqbmvSl-l-wNl98Rtrsg1mhh2Nfayfpcl72_qyApXf1v561r9o8xIvNmHMQ66PrZdG5N-UghSvCt30WoQIX6LcyD0zeoileG3c5uzE_QZ9Z-w57W4U64h](https://lh6.googleusercontent.com/XxinSccKk_ibw_N1Hh7PqbmvSl-l-wNl98Rtrsg1mhh2Nfayfpcl72_qyApXf1v561r9o8xIvNmHMQ66PrZdG5N-UghSvCt30WoQIX6LcyD0zeoileG3c5uzE_QZ9Z-w57W4U64h)

This model architecture is made using **tf.keras.utils.plot_model** 

**Input Layer** 

The input layer is a simple input layer that takes our tokenized and vectorized input that we preprocessed.

**Embedding Layer**

### TODO