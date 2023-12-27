# function to plot confusion matrix

from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

def show_confusion_matrix(y_true, y_pred, classes):

    cm=confusion_matrix(y_true, y_pred, normalize='true')

    plt.figure(figsize=(8,8))
    sp = plt.subplot(1,1,1)
    ctx = sp.matshow(cm)
    plt.xticks(list(range(0,6)), labels=classes)
    plt.yticks(list(range(0,6)), labels=classes)
    plt.colorbar(ctx)
    plt.show()
