import numpy as np 
import pandas as pd
import csv

def load_all(test_num=50):
    """
    load train.csv containing "numerical" user and item ids
    refer util for implementation
    data format:
        user_id, item_id
    """
    train_data = pd.read_csv("data/train.csv", 
        sep=',', header=None, names=['user', 'item'], 
        usecols=[0, 1], dtype={0: np.int32, 1: np.int32})

    user_num = train_data['user'].max() + 1
    item_num = train_data['item'].max() + 1

    users = np.unique(train_data.user)
    items = np.unique(train_data.item)

    train_data = train_data.values.tolist()


    """
    Load the file containing community data
    data format:
        target_user, comm_user_1, comm_user_2 ......., comm_user_n
    """
    # load the comunity
    comm_data = {}
    with open('data/top_comm.csv', newline='') as csvfile:
        read = csv.reader(csvfile, delimiter=',')
        for row in read:
            comm_data[int(row[0])] = [int(r) for r in row[1:]]
    
    """
    Load the test data
    data format:
        user_id, item_id
    """
    test_data = []
    test_df = pd.read_csv("data/test.csv", header=None)
    for index, row in test_df.iterrows():
        test_data.append([int(row[0]), int(row[1])]) #, int(row[])])

    return train_data, test_data, user_num, item_num, comm_data, users, items