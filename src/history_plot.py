# takes history object from tensorflow model.fit() and plots accuracy and loss

import matplotlib.pyplot as plt

def show_history(h):
    epochs_trained = len(h.history['loss'])
    plt.figure(figsize=(16,6))

    # Accuracy subplot
    plt.subplot(1,2,1)
    plt.plot(range(epochs_trained), h.history.get('accuracy', []), label='Training Accuracy') 
    plt.plot(range(epochs_trained), h.history.get('val_accuracy', []), label='Validation Accuracy') 
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()

    # Loss subplot
    plt.subplot(1,2,2)
    plt.plot(range(epochs_trained), h.history.get('loss', []), label='Training Loss') 
    plt.plot(range(epochs_trained), h.history.get('val_loss', []), label='Validation Loss') 
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()

    # Show the plot
    plt.show()