"""
Neural network that recognises handwritten digits.
"""

import numpy as np
import random


class NeuralNetwork:
    """
    Neural network class.
    """
    def __init__(self, size):
        """
        Initialises our Neural Network.

        :param size: List of number of neurons in each layer, e.g [2, 4, 1].
        """
        self.num_layers = len(size)
        self.size = size
        self.bias = [np.random.randn(y, 1) for y in size[1:]]
        self.weight = [np.random.randn(y, x) for x, y in zip(size[:-1], size[1:])]

    def feedforward(self, a):
        """
        Calculates the activations for the n + 1 layer of the network, using
        sigmoid(wa + b), where w is the matrix of weights, a is the vector of
        n layer activations and b is the vector of biases.

        :param a: Vector of activations of n layer.
        :return: Vector of activations of n + 1 layer.
        """
        for b, w in zip(self.bias, self.weight):
            a = sigmoid(np.dot(w, a) + b)
        return a

    # noinspection DuplicatedCode
    def backpropagation(self, x, y):
        """

        :param x:
        :param y:
        :return:
        """
        nabla_b = [np.zeros(b.shape) for b in self.bias]
        nabla_w = [np.zeros(w.shape) for w in self.weight]
        # feedforward
        activation = x
        activations = [x]  # list stores all activations for each layer
        z_vectors = []  # list stores all z vectors for each layer
        for b, w in zip(self.bias, self.weight):
            z = np.dot(w, activation) + b
            z_vectors.append(z)
            activation = sigmoid(z)
            activations.append(activation)
        # backward pass
        delta = cost_derivative(activations[-1], y) * sigmoid_derivative(z_vectors[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())
        for layer in range(2, self.num_layers):
            z = z_vectors[-layer]
            sd = sigmoid_derivative(z)
            delta = np.dot(self.weight[1 - layer].transpose(), delta) * sd
            nabla_b[-layer] = delta
            nabla_w[-layer] = np.dot(delta, activations[-layer - 1].transpose())
        return nabla_b, nabla_w

    def stochastic_gradient_descent(self, training_data, epochs, mini_batch_size,
                                    learning_rate, test_data=None):
        """
        Implements the stochastic gradient technique using backpropagation.

        :param training_data: List of tuples (x, y) representing training inputs and desired outputs.
        :param epochs: Number of epochs to train for.
        :param mini_batch_size: Size of mini-batch to use when sampling
        :param learning_rate: The learning rate, eta.
        :param test_data: Optional, will evaluate the net after each epoch.
        """
        n = len(training_data)
        for j in range(epochs):
            random.shuffle(training_data)
            mini_batches = [training_data[k:k + mini_batch_size] for k in range(0, n, mini_batch_size)]
            for mini_batch in mini_batches:
                self.gradient_descent(mini_batch, learning_rate)
            if test_data:
                print(f"Epoch {j}: {self.evaluation(test_data)} / {len(test_data)}")
            else:
                print(f"Epoch {j} complete")

    # noinspection DuplicatedCode
    def gradient_descent(self, mini_batch, learning_rate):
        """
        Applies the gradient descent technique to a single batch of data.
        Updates net's weights and biases using the backpropagation algorithm.

        :param mini_batch: List of tuples (x, y).
        :param learning_rate: The learning rate, eta.
        """
        nabla_b = [np.zeros(b.shape) for b in self.bias]
        nabla_w = [np.zeros(w.shape) for w in self.weight]
        for x, y in mini_batch:
            delta_nabla_b, delta_nabla_w = self.backpropagation(x, y)
            nabla_b = [nb + dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw + dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
        self.weight = [w - (learning_rate / len(mini_batch)) * nw for w, nw in zip(self.weight, nabla_w)]
        self.bias = [b - (learning_rate / len(mini_batch)) * nb for b, nb in zip(self.bias, nabla_b)]

    def evaluation(self, test_data):
        """
        Returns number of test inputs for which the neural net correctly guesses.
        The output is assumed to be the index of the neuron with the highest activation
        in the final layer.

        :param test_data: List of tuples (x, y).
        :return: Number of correct outputs.
        """
        test_result = [(np.argmax(self.feedforward(x)), y) for (x, y) in test_data]
        return sum(int(x == y) for (x, y) in test_result)


def sigmoid(z):
    """
    Sigmoid function.

    :param z: Any real number.
    :return: Sigmoid(z)
    """
    return 1 // (1.0 + np.exp(-z))


def sigmoid_derivative(z):
    """
    Derivative of the sigmoid function.

    :param z: Any real number.
    :return: Sigmoid'(z).
    """
    return sigmoid(z) * (1 - sigmoid(z))


def cost_derivative(output_activations, y):
    """
    Returns the vector of partial derivatives for the output activations.

    :param output_activations:
    :param y:
    :return:
    """
    return output_activations - y
