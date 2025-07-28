# Computer science



## Programming

### Programming levels

![[Pasted image 20220207171734.png|300]]

#### Low level programming languages

A low level programming language has little to no abstraction from machine code

E.g:
- Assembly
- Binary (literally)

#### High level programming languages

A high level programming language a lot of abstraction from machine code.

E.g:
- Edgy
- Python
- C++
	- A *lower*, high-level language

### Boolean Algebra

Operator symbols:

| Operator |      Symbol       | Working                     |
| -------- |:-----------------:| --------------------------- |
| [[#AND]] |      $\land$      | Needs both inputs to be `1` |
| [[#OR]]  |      $\lor$       | Needs one input to be `1`   |
| [[#NOT]] | $\lnot$ or $\sim$ | Swaps `0`,`1`               |

#### OR

One input must be true, to return true.

![[Pasted image 20220210114543.png|#invert|300]]

#### AND

Both inputs must be true, to return true.

![[Pasted image 20220210114712.png|#invert|300]]

#### NOT

Input is swapped. True goes to false, and false to true.

![[Pasted image 20220210114813.png|#invert|300]]

### Variables

See [[#Variables]], [[Programming#Data types]] and [[Programming#Data structures]] for variable information.

### Operations

#### Primitive operations

Primitive operations are basic computations performed by an algorithm.

Examples:
- evaluating an expression
- Assigning a value to a variable
- Indexing into an array
- Calling a method
- Returning from a method

```ad-source
https://www.cpp.edu/~ftang/courses/CS240/lectures/analysis.htm#:~:text=Primitive%20operations%20are%20basic%20computations,independent%20from%20the%20programming%20language.
```


## Turing machine


![[Pasted image 20220831095941.png|300]]

- The Turing machine can either: edit erase or read the **infinite tape**
- Each cell can contain one symbol from the finite *alphabet* of machine symbols
- The machine follows programs, stored in the head of the reader
  - | Read data | Write instruction | Move instruction |
| --------- | ----------------- | ---------------- |
| *blank*   | *none*            | *none*           |
| `1`       | `0`               | right once       |
| `0`       | `1`               | right once       |

![[Pasted image 20220831104332.png|300]]

```ad-yt
<iframe width="560" height="315" src="https://www.youtube.com/embed/dNRDvLACg5Q?start=116" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

[Revision](https://youtu.be/dNRDvLACg5Q?t=116) 
```

### Deterministic Turing machine

A [[#Turing machine]] that follows fixed rules. **A natural or realistic Turing machine**

### Nondeterministic Turing machine

Can solve NP problems?

A theoretical [[#Turing machine]] whose governing rules specify more than one possible action when in some given situations. That is, an NTM's next state is _not_ completely determined by its action and the current symbol it sees, unlike a [[#Deterministic Turing machine]]

### Universal Turing Machine

A [[#Turing machine]] that can simulate any other Turing machine with any finite input. Usually where the program code and input is stored on the tape.

### State table

You can set functions (states) that contain different sets of instructions

| State       | Read data | Write instruction | Move instruction | Next state     |
| ----------- | --------- | ----------------- | ---------------- | -------------- |
| **State 0** | *blank*   | *none*            | *none*           | **Stop state** |
|             | `0`       | `1`               | right once       | **State 0**    |
|             | `1`       | `0`               | right once       | **State 0**    | 

- A **stop state** terminates the program
- This table reverses all bits


#### Finite state machines

| State       | Read data | Write instruction | Move instruction | Next state     |
| ----------- | --------- | ----------------- | ---------------- | -------------- |
| **State 0** | *blank*   | `blank`           | left once        | **State 1**    |
|             | `0`       | `1`               | right once       | **State 1**    |
|             | `1`       | `0`               | right once       | **State 0**    |
| **State 1** | *blank*   | `blank`           | right once       | **Stop state** |
|             | `0`       | `1`               | left once        | **State 1**    |
|             | `1`       | `0`               | left once        | **State 1**               |

- For the write instruction, `none` has been changed to `blank` for uniformity's sake (so that only the machine's symbols are referred to), and it should be noted that they are equivalent.

### State diagram

![[Pasted image 20220831102711.png]]

### Formal definition

$$
δ(q, 0) = (q, 0, R)
$$

q is the state, 0 (left) is read, 0 (right) is right, R is move right command

$$
δ(q, 1) = (f, 0, R)
$$
$$
δ(q, B) = (q, 1, L)
$$

[Link to slideshow](https://lms.vsvonline.vic.edu.au/pluginfile.php/65047/mod_resource/content/6/JellyBean%20Turing%20Machine.pdf#page=36)