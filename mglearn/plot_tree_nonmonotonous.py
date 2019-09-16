import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.tree import DecisionTreeClassifier, plot_tree
from .tools import discrete_scatter
from .plot_2d_separator import plot_2d_separator


def plot_tree_not_monotone():
    # make a simple 2d dataset
    X, y = make_blobs(centers=4, random_state=8)
    y = y % 2
    fig, ax = plt.subplots(1, 2, figsize=(12, 4))
    discrete_scatter(X[:, 0], X[:, 1], y, ax=ax[0])
    ax[0].legend(["Class 0", "Class 1"], loc="best")

    # learn a decision tree model
    tree = DecisionTreeClassifier(random_state=0).fit(X, y)
    plot_2d_separator(tree, X, linestyle="dashed", ax=ax[0])

    # visualize the tree
    plot_tree(tree, impurity=False, filled=True, ax=ax[1])
