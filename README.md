# graph_logic
FO formulas, transductions on graphs

ideas:
- fo formulas on graph operated graphs
- graph operator operation as formula

Summary: 
Every FO sentence defines family of graphs that can be recognized in polynomial time. 0-1 law: if S is any sentence in FO logic, the probability the graph chosen unif. at random among all n vertex graphs is either 0/1 as $n \rightarrow \infty$. 

Existence of tiwns (vertices whose set of neighbors are identical, not including selves) FO sentence: $ \exists u,v : (u \neq v) \bigwedge \forall w: (u=w) \bigvee (v = w) \bigvee ((u \sim w) \leftrightarrow ( v \sim w))$.
