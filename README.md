# graph_logic
FO formulas, transductions on graphs

ideas:
- fo formulas on graph operated graphs
- graph operator operation as formula

Summary: 
Every FO sentence defines family of graphs that can be recognized in polynomial time. 0-1 law: if S is any sentence in FO logic, the probability the graph chosen unif. at random among all n vertex graphs is either 0/1 as $n \rightarrow \infty$. 

Existence of tiwns (vertices whose set of neighbors are identical, not including selves) FO sentence: $\exists u,v : (u \neq v) \bigwedge \forall w: (u=w) \bigvee (v = w) \bigvee ((u \sim w) \leftrightarrow ( v \sim w))$.
In second order logic, the variables represent complex structures built from $k$-ary relations.
A restricted set of second order logic of graphs, MSO 1 and 2. 
MSO1 : Add another type of variable for sets of vertices to FO logic. (ability to test if a vertex belongs to a set)
MSO2 : MSO2 is similar, but allows four types of variables: vertices, edges, and sets of vertices and edges. 

Apply Courcelle's theorem, which says that every MSO2 formula can be translated into a fixed-parameter tractable algorithm on graphs parameterized by their treewidth, and that every MSO1 formula can be translated into an FPT algorithm on graphs parameterized by their clique-width

The point of this is completely constructive: it's not just that an algorithm exists, but in principle we could automatically translate the formula into the algorithm. It's also completely useless in practice because the dependence on the parameter is ridiculously high (some kind of tower of powers). When an algorithm is found in this way, additional research is needed to find a more direct algorithm that reduces this dependence to something more reasonable like single-exponential with a small base, or even removes it to get a polynomial time algorithm. 
