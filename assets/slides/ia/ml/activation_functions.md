# Activation Functions

Hidden layers have a number of benefits, but one key harm is that with every hidden layer comes more and more neurons swirling around our computers proverbial head, and sometimes it’s hard to know which data is relevant and how much weight to give it. Activation functions can help with that by doing something to each neuron in the hidden layers that changes its value relative to other neurons. You may also recall that we perform a sort of activation function on our output layer by normalizing it with a logistic curve. Activation functions are an important component of neural networks, so it’s valuable to know some of the common ones featured bellow.
Linear
Linear activation functions are very simple: they take the value of a neuron and keep it the same, sometimes multiplying the value by a ‘slope,’ just like a linear function in graphing.
ReLu
Image for post
ReLu, or rectified linear unit, is the exact same as the linear function except any negative value is mapped to zero instead.
Leaky ReLU
Image for post
Leaky ReLu uses a linear activation function for values above zero, much like ReLu, but unlike ReLu also uses a linear activation function for values below zero. However, the slope for the linear function for the values below zero must be less than the slope for values above zero.
Sigmoid
Image for post
As we’ve already covered, the sigmoid function turns everything into a value between one and zero, and as a value gets further from zero the closer it is to the values next to it.