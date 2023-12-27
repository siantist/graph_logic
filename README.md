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

From Graph Dynamics:

Def 1.1: A discrete dynamical system is a set $\Gamma$ together with mapping $\Phi: \Gamma \rightarrow \Gamma$, and elements of $\Gamma$ are states.
Def 1.3: Let x be some state. x is convergent if $\Phi^n(x)/n$ is finite. Otherwise, x is divergent. x is periodic if there is a natural number n s.t. $\Phi^n(x)=x$. 
The depth(x) is the supremum of the set of all natural numbers $n$ for which there is some state $y \in \Gamma$ with $\Phi^n(y) = x$. 
Remark 1.4: A state x is convergent iff x is periodic or there is n where $\Phi^n(x)$ periodic.
A circuit: set of the form $\{ x, \Phi(x), ..., \Phi^p(x) = x\}$
Def 1.6: Let M be a circuit. The depth of M is the sup of set of all natural numbers n s.t. $\exists y \in \Gamma, \Phi^n(y) \in M$ but $\Phi^{n-1}(y) \notin M$.

Discrete dynamical systems can be represented visually with the iteration digraph (Collatz digraph). 
Def 1.11: A semibasin is subset B of state set $\Gamma$ with $\Phi(B) \subseteq B$. A basin is a semibasin $B$ where the complement $\Gamma \setminus B$ is also a semibasin. 

All circuits are finite semibasins. Any subset $M$ of $\Gamma$ generates semibasin $\cup_{x \in M} \cup_{n \in N} \Phi^n(x)$. 

Define 2 new systems given dynamical system $(\Gamma, \Phi)$ and semibasin $B$:
(i) subsystem $(B, \Phi_{|B}$
(ii) quotient system $(\Gamma_{ / B}, \Phi')$ where $\Gamma_{ / B} = \Gamma \setminus B \cup \{ B\}$ and $\Phi'$ is $\Phi'(x) = \Phi(x) , x \in \Gamma \setminus B$ if $\Phi(x) \notin B$, $= B , x \in \Gamma \setminus B$ if $\Phi(x) \in B$, else $\Phi'(B) = B$.
