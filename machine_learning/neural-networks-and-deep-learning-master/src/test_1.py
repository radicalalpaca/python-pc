import neural_network
import tensorflow as tf

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
net = neural_network.NeuralNetwork([784, 30, 10])


net.stochastic_gradient_descent(training_data, 30, 10, 3.0, test_data=test_data)
