## LAYERED ARCHITECTURE

"separation of concerns" principle
Software design is divided into layer laid over one another. Each layer performs a dedicated responsibility. Architecture divides the software into the following layers
- Presentation Layer
holds the user interface that interacts with the outside 
- Business Logic Layer
hold the business logic for the software application. This layer detach UI/UX from business related computations and hence provide a flexibility to modify the logic depending on constantly changing business requirements without having any affect on other layers.
- Data Link Layer
Keeps the responsibility of interacting with persistent storage like databases and miscellaneous data processing which is not domain specific (ie. not related to the business)
Data and control flows from one layer to another crossing every layer in design. These layer also increase the degree of Abstraction in the design. As stability is proportional to abstraction to certain extent , it also improves stability of software to some limit.

***Pro**
Simpler to implement compared to other approaches
Offers abstraction due to separation of concerns among layers
Isolation between layers keeps other layers immune from the modifications in one layer
Software becomes more manageable due to low coupling

***Cons**
Doesn't offer much scalability
Software build with this approach will be inclined to have a monolitical structure lacking ease of modifications
Data has to flow from each layer one after another even if its is unnecessary to pass from certain layers. This issue is termed as Sinkhole Problem