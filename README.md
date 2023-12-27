# Emotion Recognition from Twitter Posts

## Project Overview

This project aims to develop an automated system capable of recognizing and categorizing emotions expressed in English text messages. It focuses on six basic emotions: anger, fear, joy, love, sadness, and surprise, providing a nuanced understanding of human sentiments in social media text.

## Dataset

The dataset consists of 20,000 labeled tweets, each associated with one of the six emotions. The dataset is publicly available and can be retrieved from: [DAIR AI Emotion Dataset on GitHub](https://github.com/dair-ai/emotion_dataset)

## Methodology

The core of the system is built using TensorFlow and the Keras API, leveraging the power and flexibility of neural networks, and Optuna for hyperparameter tuning. The architecture includes:
- **Preprocessing**: Utilizing TensorFlow Keras for tokenization and sequence padding.
- **Model Architecture**: Employing a neural network with two Bidirectional LSTM layers, specifically designed to understand the context and sequence in the text data effectively.
- **Hyperparameter Tuning**: Demonstrating the use of Optuna for optimizing the neural network, leading to improved model performance.

## Results

The model achieved a best validation accuracy of 0.94 and test accuracy score of 0.93, indicating a high level of proficiency in categorizing tweets into the respective emotions. This result underscores the potential of LSTMs in handling complex text classification tasks like emotion recognition and the importance of hyperparameter tuning.

## Future Outlook

- **Apply Trained Model to Other Datasets**: Exploring the model's performance on various text sources and domains to evaluate its generalizability and robustness.
- **Expand Emotion Categories**: Considering the addition of more emotion categories or sub-categories for a more granular emotional analysis.
- **Improve Model with Advanced Techniques**: Experimenting with more sophisticated neural network architectures, fine-tuning of pretrained language models, and techniques to enhance accuracy and efficiency.

## How to Use

To use this emotion recognition model, follow these steps:
1. **Clone the Repository**: Clone the repository to your local machine.
2. **Install Dependencies**: Run `pip install -r requirements.txt` to install the necessary packages.
3. **Run the Main Notebook**: Navigate to the notebook directory and launch the main notebook to train the model and make predictions.
