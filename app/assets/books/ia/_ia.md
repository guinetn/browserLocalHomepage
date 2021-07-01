# IA

Cloud → Proliferation of data and compute power → IA (computer vision...)

The machine learning development workflow is still very iterative, and is challenging for developers to manage due to the relative immaturity of ML tooling.” The machine learning workflow — from data ingestion, feature engineering, and model selection to debugging, deployment, monitoring, and maintenance, along with all the steps in between — can be like trying to tame a wild animal.
big tech companies challenge solved by their own ML and big data platforms for their data scientists to use: 
- Uber: [Michelangelo](https://eng.uber.com/michelangelo-machine-learning-platform/)
- Facebook, Instagram, WhatsApp: [FBLearner flow](https://engineering.fb.com/core-data/introducing-fblearner-flow-facebook-s-ai-backbone/)
- Google: [TFX](https://www.tensorflow.org/tfx/guide)
- Netflix: [Metaflow](https://metaflow.org/) and open sourced [Polynote](https://netflixtechblog.com/open-sourcing-polynote-an-ide-inspired-polyglot-notebook-7f929d3f447)
- Amazon: [SageMaker](https://aws.amazon.com/blogs/aws/amazon-sagemaker-studio-the-first-fully-integrated-development-environment-for-machine-learning/)
For smaller organizations, players have emerged, see by Gartner’s Magic Quadrant for Data Science and Machine Learning Platforms:

![](assets/books/ia/assets/gartner_magic_quadrant_on_ml.png)

* Takeaways

AI Artificial intelligence: machine mimic human behavior
ML Machine learning:
    subset of ai    
    data analytics technique that use statistical methods to learn from experience
    supervised learning 
        develop a predictive model
        trains a model on labeled data so that it can predict future outputs: classification/regression
    unsupervised learning 
        group & interpret data based only on input data
        trains a model on labeled data & finds hidden patterns in input data: clustering
DL Deep learning
    Subset of ML
    Train a model to do a task    
    Work on neural network architectures
    "Deep": refers to hidden layers in the neural network
    Came in 1980s, but due to a lack of labeled data and computing power, it was not popular at that time.
    Trained by using large sets of labeled data
    DL algorithms scale with data, whereas machine learning plateau at a certain level of performance when we add more data.
    CNN: Convolutional Neural Networks, automatic feature extraction (no manual work) 

    Use cases
        Autonomous Car: self-driving car researchers are using DL to automatically detect objects without human input such as traffic lights and stop signs.
    
        Defense and Aerospace sector: DL is used to detect objects from satellites that locate areas of interest, and detect safe or unsafe zones for troops.
    
        Industrial Automation: DL automatically detecting worker safety around heavy machinery.
    
        Medical Research: DL automatically detects cancer cells. High-dimensional data set used to train a DL application to exactly identify cancer cells.
    
        Electronics: Home assistance devices that reply to our voice and know our preferences are powered by DL applications.

|ALGORITHMS|Data transformations|
|---|---|
|CLASSIFICATION|data → known classes|
|REGRESSION|data → function|
|CLUSTERING|data → unknown classes = discovering groups association|

::::

# IA GOALS
lorem   

::::
download.page(ia/ml/_ml.md)
::::
download.page(ia/ml/ml_lifecycle.md)
::::

# Convolutional Neural Networks

download.page(ia/ml/cnn.md)
::::

download.page(ia/no-code-apps.md)


### protocol buffers
https://developers.google.com/protocol-buffers/docs/overview 

Ex: In IA, ONNX est écrit en protocol buffers (protobufs). Il existe un compilateur officiel protobufs pour Go. Cet outil permet de générer les fonctions de désérialisation, qui vont convertir le binaire ONNX en un objet Go. [onnx-go](https://github.com/owulveryck/onnx-go)


download.page(ia/bigdata/_bigdata.md)

::::
download.page(ia/articles.md)

## More

- https://intelligence-artificielle.developpez.com/actu/312174/Pourquoi-la-nouvelle-IA-liquide-de-MIT-est-elle-une-innovation-revolutionnaire-Elle-apprend-continuellement-de-son-experience-du-monde/
- https://venturebeat.com/2020/06/27/a-closer-look-at-sagemaker-studio-aws-machine-learning-ide