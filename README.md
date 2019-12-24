# Recommendation using Collaborative Filtering
Extended the basic implementation of [Bayesian Personalised Ranking](https://arxiv.org/pdf/1205.2618.pdf)  and [Social BPR](https://cseweb.ucsd.edu/~jmcauley/pdfs/cikm14.pdf) to include the influence of communities. The code has been implemented in PyTorch.

## Requirements

- Python 3.7.4 (not a hard requirement)
- pytorch 1.2.0

## Running Instructions


Clone this repo into your local machine and run the main.ipynb notebook. Don't forget to install the dependencies first.

#### Input
- The training data should be in csv format with 2 columns (user and item). Similar for test data.
- The top community data should also be in csv format having varying columns (user, comm_user1, comm_user2, ...). It's columns will equal to the highest community size among all users. (refer to the top_comm.csv file given in data/)
- All these data (both user and items) must be indexed. That is, for example, if the user names are in form of strings and there are 1500 users, your user column must only comprise of number between 0 and 1499. Each number should correspond to a particular user. This is required for creating embeddings.

#### Methods
- For creating community you can use [networkx library](https://networkx.github.io/documentation/stable/reference/algorithms/community.html#module-networkx.algorithms.community.kclique). I used clique percolation to identify all communities for a particular user. Further I found the most influencing community using a basic scoring method and used users from that community in top_comm.csv.
- You can also use [community api](https://python-louvain.readthedocs.io/en/latest/api.html) built on top of networkx.

#### Datasets
- You can use any dataset relevant to recommendation. We mined our own data from Twitter.

