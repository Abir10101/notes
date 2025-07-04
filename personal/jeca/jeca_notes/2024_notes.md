1. explain polymorphism?
ans:- polymorphism is feature of oops that allows developers to create multiple forms of a function. There are two types of polymorphism.
	a) compiletime polymorphism: function overloading
	b) runtime polymorphism: function overriding


2. explain decision tree?
ans:- decision trees are machine learning models that comes under supervised learning classification. It forms a hierarchical, tree like structure with root node, branches, internal nodes and leaf nodes. A decision tree can grow very complex by noise or anomaly training data which is called as overfitting. Overfitted decision trees performs excellently good on training data but performs poorly on test data. Pruning is a technique used to combat overfitted decision trees. There are two types of pruning. a) Pre-pruning: Stopping at the time of noise data. b) Post-pruning: Building the full tree first then delete noise data branches


3. Explain supervised and unsupervised learning?
ans:- Supervised learning is a machine learning approach where the algorithm learns from labeled training data to predict outcomes for unseen data. The "supervision" comes from the fact that the model is trained on input-output pairs where the correct answers are provided. Eg: Classification: Predicting a categorical label (e.g., spam detection, image recognition). Unsupervised learning involves training algorithms on data without labeled responses. The algorithm tries to learn patterns, relationships, or structure in the data on its own. Eg: Anomaly Detection: Identifying outliers or unusual data points


4. Time-to-live (TTL) field in IP header?
ans:- TTl field in IP header is used to prevent packets from circulating around the network indefinitely. It's an 8-bit field that limits a packet's lifetime by setting a maximum hop count. Each router that processes the packet decrements this value by at least 1, and when the TTL reaches zero, the packet is discarded, and an ICMP "Time Exceeded" message is typically sent back to the source.


5. Cache vs Paging
ans: Cache is between cpu and ram and storage used is sram (Static Ram), Page is between ram and HDD and storage used is HDD.


6. Explain friend keyword in class?
- The friend keyword in a class allows a specified function or another class to access its private and protected members, bypassing normal encapsulation rules
- Friendship is not mutual (if ClassA declares ClassB as a friend, ClassB can access ClassA's private members, but not vice versa unless explicitly declared).
- Friendship is not inherited (a derived class does not automatically become a friend of the base class's friends).


7. How a data bus in cpu works with ram?
- Data bus reads data from ram chip in chip width (words) so for 32 bit data bus and chip width 8 bits then bus will require minimum of 32/8=4 chips to read data. Similarly, for chip width of 16 bits will require minimum of 32/16=2 chips for the data bus to work. 


8. Explain transitive dependency?
- Transitive dependency occurs in a relational database when one non-key attribute is dependent on another non-key attribute, which in turn determined by a third attribute. This creates a chain of dependencies like the transitive property in maths.
- To eliminate transitive dependencies, relation should be divided into smaller relations, each with one of the determinants as its primary key, ensuring the relation is in third normal form.
- A -> B and B -> C; therefore A -> C
    Item_numb -> distrib_numb
    Distrib_numb -> warehouse_phone_number


9. Explain is Super Key, Primary Key, Alternate Key, Candidate Key, Compound Key, Composite Key.
- Super Key: Group of attributes that can identify a row in a table. Basically it is a group of all the keys in a table.
- Candidate Key: A group of attributes where each attribute can uniquely identify a row in a table. It is a minimal superkey.
- Primary Key: An attribute from the candidate key that is chosen to be primary key. Chosen on the basis of: It cannot be null.
- Alternate Key: Single or group of attributes from the Candidate Key which are not chosen as primary key is an alternate key.
- Compound Key: Set of foreign key attributes that together can identify each record in a table.
- Composite Key: Set of attributes that together can identify each record in a table but does not contain foreign keys.
