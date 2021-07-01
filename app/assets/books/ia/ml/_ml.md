# NN - Neural Networks

https://medium.com/analytics-vidhya/neural-networks-the-basics-7cfd2ad15443

`Continual adjustment of weights`  
 and how they pass through neurons to accurately predict an outcome based on some input.

`Weights`   are adjusted through gradient descent.

***Activation functions***   determine how much given neurons are weighed.
Networks have several applications, such as image recognition.

::::

Right now, one big question is probably etching itself into your mind: how do we decide the values of the weights? (Remember the weights are how we go from one layer to the next.) The process to set weights is actually quite simple: guess and check. We take a set of data, for example attendance’s relationship to passing or fail, called the training set, and guesses different weights until one set of weights can accurately tell us what we want to know within a certain tolerance.
To illustrate, the tolerance could be 5%, meaning that 95% accuracy is good enough, or 1%, meaning that we demand 99% accuracy. Each guess is adjusted based on the success of the previous one through an algorithm called gradient descent. Let’s now look at a more formal, step by step definition at how we can set weights.
1. Pick random weights.
2. Use them on a piece of data from our training set of data.
3. Plug the results into a gradient descent function layer by layer, starting with the output layer and moving backwards — the formula for gradient descent is very complicated and not worth memorizing but the basic idea is simple: if our estimate was too high, decrease the weights. If our estimate was too low, increase the weights. This process is called back propagation, because we move our adjustments backwards through the network.
4. Repeat the above process until our network is accurate within the bounds of the tolerance.
Through this process, we can teach multi-layer neural networks to make very accurate predictions using massive amounts of data that in which no human could ever identify a pattern.
Avoiding Overfitting
Overfitting is one of the great pitfalls of machine learning and arises when our AI learns too well. It becomes so good at getting the result it wants from the specific set of training data that it can no longer apply itself to the general case. It’s kind of like if a quarterback got so good at throwing a deep ball that he lost the ability to connect on shorter passes. Let’s look at a couple methods for correcting overfitting:
Use more data — the more holistic a data set is, the more difficult to overfit.
Dropout — one of the popular methods to stop overfitting. Dropout periodically removes random nodes from the network, forcing the network to adjust to learn with different internal structures and become better equipped to handle any input.

::::
download.page(ia/ml/activation_functions.md)
download.page(ia/ml/embedded/_embedded.md)
::::

# Classification 

most popular application of NN’s