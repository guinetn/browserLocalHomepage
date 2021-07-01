# OPL - Optimization Programming Language

https://medium.com/smartbp/which-is-the-best-programming-language-to-formulate-an-optimization-model-with-cplex-opl-or-python-56404bb68908

CPLEX
an optimization software package (IBM)
has options for formulating different models
formulate a model and call the engine to do its work
- Formulating a model through OPL (Optimization Programming Language), using the IBM ILOG CPLEX Optimization Studio IDE.
- Formulating a model with the Python programming language, using the DOcplex library.


### Simple Production Planning problem
A company produces four products: A, B, C, D. 
To make their production decisions, they must consider that the plant has a limited capacity, measured in time, that cannot be exceeded, and they cannot produce more articles than those demanded.

***How many units of each product must the company produce to maximize its profit uner these conditions:***

Products to create|Demand|Profits|Production Time
---|---|---|---
A|50|40|15
B|70|20|15
C|100|10|5
D|20|70|25

# Mathemathecial formulation

        
- Problem initialization
- Parameters definition
- Decision variables
- Objective function
- Constraints
- Running the model
- Viewing results