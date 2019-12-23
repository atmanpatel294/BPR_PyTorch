import numpy as np
from collections import defaultdict


def metrics(model, test_loader, device):
    accuracy, auc = [], []
    tmp_auc = defaultdict(list)
    for user, item_i, item_j in test_loader:
        user = user.to(device)
        item_i = item_i.to(device)
        item_j = item_j.to(device)
        prediction_i, prediction_j, prediction_j = model(user.to(device), item_i.to(device), item_j.to(device), item_j.to(device))
        count = 0
        pred = prediction_i > prediction_j
        pred = [int(p) for p in pred]
        accuracy.append(sum(pred)/len(pred))
    return np.mean(accuracy)