# TuringMachine
A Turing Machine that implements a quadruple M = (K, Σ, δ, s),

## Where:

- K is a finite set of states (line numbers) 
- Σ is a finite set of symbols including empty and excluding #, <, - and >(alphabet)
- δ : K × Σ → (K ∪ {h,“yes”,“no”}) × Σ × {<, >, −}, a transition function (instructions) 
- s ∈ K, the initial state (starting point)
