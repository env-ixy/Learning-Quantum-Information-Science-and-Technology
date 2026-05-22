We already looked at a basic quantum computer. It gets us most of the ideas about quantum computing, complimentarity, observation, incompatiblity between position and momentum, Dirac notation. 

In any computing paradigm, you have
- input states (bits, 0/1)
- transformations (algorithms)
- output

The general circuits are as follows:
$$
\text{input }(010010) \rightarrow \text{information processor} \rightarrow \text{output }(1001)
$$

This same idea - in some form - carries over similarly.
$$
\ket{\Psi} \rightarrow \text{Quantum Computer } \rightarrow \ket{\Psi'}
$$

Most of the processing is quantum. Then you might have some device that measures or potentially collapses some or all of these states. 

To have one, you would need to initialise your state first. This would be equivalent to initialising a new register. This is not an easy thing, though. You cannot copy quantum states. There is a No-Cloning theorem ([Wikipedia](https://en.wikipedia.org/wiki/No-cloning_theorem#Theorem_and_proof)). 

Then you need some kind of transformation. These can be called many things: operation, quantum gate, unitary operation. 

Then you should have the ability to measure your states. Which, from the previous two, is not an easy task. So you have to repeat the experiment multiple times. Then work your way back to the coefficients of the output state (since observation collapses it). Then you have to work the probablity amplitudes. Tedious!

The quantum world is *tiring*. The quantum objects - electrons, protons, photons etc. - are *really, really* small. The effects of them only manifest at *really, really* low temperatures. Near 0 Kelvin. If you put a multimeter (set to V) across a resistor, it won't show 0. There is no such thing as 0. It will show noise. Johnson noise (or thermal noise), caused by the Brownian motion of electrons. That *is* voltage. Just *unbelievably* low voltage. A multimeter isn't really ideal. If you use an oscilloscope, you'd measure some vague noise. I can't find an image of this and I don't have an oscilloscope, since the people concerned with this measurements don't post the readings in pictures online and the people who *do* post aren't concerned with this. 

This is, by the way, as follows:
$$
V_n = \sqrt{4k_BTR\Delta{f}}
$$

This noise also exists in the quantum computer. There would be environmental factors. Quantum states, because they are very fragile, get observed, collapsed, interacted with, *by the environment* irrespective of the conscious* observer. These disturbances that *change the state to an undesirable configuration* are called **decoherence**. So when building one, you have to protect this fragile state from these disturbances. This is why it's difficult to build them. They take a finite amount of time (for processing, nothing is instentanious), and in that time, decoherence *creeps* in. They need a *pristine, pure, undisturbed, perfect* environment to work. Obviously the temperature needs to be as low as possible. 

Sometimes, errors are inevitable. You need methods to diagnose errors and correcting them. Thus, decoherence goes hand-in-hand with **error correction**. Computer scientists learn a lot about this. But this is **quantum error correction**. All of this is **useless** if you can't scale it up. Doing this might be easy for a single qubit, but you can't do much with a single qubit. We'd want 5, 10, 100's of qubits if we want something interesting. Technologists have a standard called the **Quantum Ascendency Limit** which is about 100 qubits. So you need to surpass this limit to do something intresting with quantum computing. 

These five criteriae - initialisation, transformation, measurement - dechorence, error correction - are called **DiVincenzo's criteria** with respect to Daivid P. DiVincenzo. 

Sometimes, if you try something at one point in time, you also try it someplace else. SO flying qubits too. Sometimes, this is also a criteria. 

This is about transformations. [Lecture 1](../Lecture%201/README.md) was about initilisation, [Lecture 2](../Lecture%202/README.md) was about measurement. 

These quantum computers are actually nothing but tangible pieces of hardware. Last time, the beamsplitter experiment too, that has to be built as well. It is not mystical, it just tedious. 

Let's look at quantum dynamics (not to be confused with quantum electrodynamics). Get our bloch sphere again. The same mumbo-jumbo, mark $\ket{0}$ and $\ket{1}$, x-y-z axes, $\frac{\ket{0} + \ket{1}}{\sqrt{2}}$ and $\frac{\ket{0} - \ket{1}}{\sqrt{2}}$. A general point on the sphere would be
$$
\ket{\Psi} = \cos\frac\theta2\ket{0} + \sin\frac\theta2e^{i\phi}\ket{1} \\
\theta, \phi \in \mathbb{R}
$$


The intuition is: since the z-axis is the basis, you don't need a z-co-ordinate. And the scalar multiplying then adding is the way to write vectors in linear algebra (QM is essentially LA on steroids). The $\cos$ because the side adjacent to the angle $\theta$ is the distance from the center towards the flattened projection of the point. $\sin$ is also for the similar purpose just in the vertical direction. Using $e^{i\phi}$ because point might not be exactly on the x-axis, so if it is, $\phi = 0 \therefore e^{i\phi} = 1$, but if it isn't, you sort of shift the point by that amount. $\frac\theta2$ is used because if it hadn't been used $\theta = 0$ and $\theta = \pi$ would give identical results (ignoring the $-1$ global phase). So we $\frac\theta2$. $\ket{0}$ and $\ket{1}$ are the basis vectors themselves.  

Now what did the beamsplitter do? It took $\ket{0} \rightarrow \frac{\ket{0} + \ket{1}}{\sqrt{2}}$ and $\ket{1} \rightarrow \frac{\ket{0} - \ket{1}}{\sqrt{2}}$. We start off at the north pole ($\ket{0}$). The output state is on the equitorial plane. What kind of transformation is this? It is a rotation. Lets call a rotation by denoting it with $\hat{R}$  This rotation in our case is $90^\circ$. We need two things: axis and amount. Let's call it about the $y$-axis. So $\hat{R}_y (\frac\pi2)$. This rotation, when acting on $\ket{0}$, gives the aforementioned output state. And what does this do to the $\ket{1}$? It rotates it towards the $-x$ direction. 

Note, we can have states inside the sphere (mixed states, later concern) but not outside. Because that would mean the $\sum\text{coefficients} > 1$, which breaks mathh. The states on the surface are called **pure states**. 

Now let's look at a few more quantum gates. 

1. **Quantum NOT gate**
    * Symbol: `N`
    * Truth table:  
    
    | Input | Output|
    | ---- | ---- |
    | $\ket{0}$ | $\ket{1}$ |
    | $\ket{1}$ | $\ket{0}$ |

    * Bloch sphere effect: Rotation by $180^\circ$ or $\pi$ radians about the y-axis ie. $\hat{R}_y(\pi)$. Which seems correct, but take the superposition for example $\frac{\ket{0} + \ket{1}}{\sqrt{2}}$. What if the not gate acts on this? It remains the same. Since $\ket{0}$ goes to $\ket{1}$ and $\ket{1}$ goes to $\ket{0}$. Simply flip. By commutativity, the same. 
$$
\hat{U}_{NOT}(\frac{\ket{0} + \ket{1}}{\sqrt{2}}) = \frac{\ket{0} + \ket{1}}{\sqrt{2}}
$$

This state is invarient under the NOT gate. If we use linear algebra terminology, this is the **eigenstate**. If $\hat{U}_{NOT}$ was a matrix, $\frac{\ket{0} + \ket{1}}{\sqrt{2}}$ is its eigenstate. From this we get that the quantum state must be a vector, and the transformation (NOT gate) must be a matrix. 

So our 180deg rotation as a NOT gate fails. What works, then? $\hat{R}_x(\pi)$. It works about the x-axis. Anything on the x-axis remains unchanged. Eigenstates of a NOT gate are $\frac{\ket{0} \pm \ket{1}}{\sqrt{2}}$. So we can represent transformations as matrices and states (kets) as vectors because when we write code, simulate, learn and think about quantum computers, we need to use classical computers with these matrices and vectors (NumPy, for example). So I can define $\ket{0}$ and $\ket{1}$ as:
$$
\ket{0} \equiv (1, 0) \\
\ket{1} \equiv (0, 1)
$$

(NOTE: using `bmatrix` for proper vertical vector co-ordinates is too much work)

Now if we bring our rules for inner products:
- $\bra{0}\ket{0} = ((1), (0)) \times (1, 0)$. A better representation perhaps in code would be `np.array([[1, 0]]) @ np.array([[1], [0]])`. This comes out to 1

Take $\ket{x}$. How will you represent it? Say this is the superposition of the $\ket{0}$ and $\ket{1}$. It'd be
$$
\ket{x} = \Big[\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}} \Big]
$$

The aforementioned $\ket{\Psi} =  \cos\frac\theta2\ket{0} + \sin\frac\theta2e^{i\phi}\ket{1}$ would have co-ordinates
$$
\ket{\Psi} = \Big[ \cos\frac\theta2, \sin\frac\theta2e^{i\phi}\Big]
$$

So yes, bras are rows and kets are column vectors. 

So now, can we come up with a matrix for this NOT gate? It has to be 2x2. It will be
$$
\hat{U}_{NOT} = 
\begin{bmatrix}
0 & 1 \\
1 & 0
\end{bmatrix}
$$

This is constructed in a normal matrix way. The first column $\begin{bmatrix} 0 \\ 1 \end{bmatrix}$ is the output when $\ket{0}$ is fed to the transformation (ie. $\ket{1}$). Similarly, the second position $\begin{bmatrix} 1 \\ 0 \end{bmatrix}$ is the $\ket{1}$ output (ie. $\ket{0}$). The convention is $\ket{0}$ first, $\ket{1}$ second. 

Now, when this acts on $\ket{0}$, we get $\ket{1}$ because
$$
\hat{U}_{NOT}(\ket{0}) = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}
\begin{bmatrix} 1 \\ 0 \end{bmatrix}
=
\begin{bmatrix} 0 \\ 1 \end{bmatrix}
=
\ket{1}
$$

Most of the simple operations are called **unitary** operations. They can be expressed as rotations of the Bloch sphere. These are unitary because if you take the inverse of this matrix, it is equal to the transpose of the complex conjugate of this matrix. ie.
$$
\text{Matrix } \hat{U}_{NOT} \text{ is unitary if: } \\
\hat{U}^{-1} = \hat{U}^\dagger = (\hat{U}^*)^T
$$

Now, moving on.

2. **Hadammard Gate**
    * Symbol: `H`
    * Truth table:

    |Input|Output|
    |----|----|
    |$\ket{0}$|$\frac{\ket{0} + \ket{1}}{\sqrt{2}}$|
    |$\ket{1}$|$\frac{\ket{0} + \ket{1}}{\sqrt{2}}$| 

    * Matrix:
$$
\hat{U}_H = \frac{1}{\sqrt{2}}
\begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix}
$$
It is called Hadamard because a matrix where all the columns are orthogonal to one another and all the rows are orthogonal to one another are called Hadamard matrices. A special property is, applying this twice undoes the action. So a Hadamard twice is identity. It is an inverse of itself.

In rotations, this won't be a simple rotation about x or y. It will be rotation about a strange axis between x and z. The denominator will be $\sqrt{2}$ because $\cos 45$ and $\sin 45$. So..
$$
\hat{U}_H = \hat{R}_{\frac{\vec{x} + \vec{z}}{\sqrt{2}}}(\pi)
$$

3. **Phase gate**
    * Symbol: $\phi$
    * Truth table:

    |Input|Output|
    |----|----|
    |$\ket{0}$|$\ket{0}$|
    |$\ket{1}$|$e^{i\phi} \ket{1}$|

    * Matrix:
$$
\hat{U}_\phi = \begin{bmatrix} 1&0 \\ 0 & e^{i\phi} \end{bmatrix}
$$

How do I get this on the Bloch sphere? both lie on the z axis. So just a rotation about the z-axis would do. 
$$
\frac{\ket{0} + \ket{1}}{\sqrt{2}} \rightarrow^{U_\phi} \frac{1}{\sqrt{2}}\Big(\ket{0} + e^{i\phi}\ket{1}\Big)
$$

So we looked at 3 gates. All of these are unitary just like rotation operators. 

Now we need Pauli matrices. They are:
$$
\sigma_x = \begin{bmatrix} 0&1 \\ 1&0\end{bmatrix} \\
$$
$$
\sigma_y = \begin{bmatrix} 0&-i \\ i&0\end{bmatrix}
$$
$$
\sigma_z = \begin{bmatrix} 1&0 \\ 0&-1\end{bmatrix}
$$

To clarify, $\hat{I}$ is the identity matrix which means all the elements from the top-left to the bottom-right diagonal are 1s and all the other elements are 0s. In 2D, this'd be equal to the aforementioned $\sigma_x$.

Armed with these, we can do:
1. $\sigma_i^2 = \hat{I}$
2. $[\sigma_x, \sigma_y] = 2i\sigma_0$
    * Note: $[\hat{A}, \hat{B}] = \hat{A}\hat{B} - \hat{B}\hat{A}$ where $\hat{A}$ and $\hat{B}$ are matrices. This is called the **commutator** of $\hat{A}$ and $\hat{B}$.

So rotational operators become:
$$
\hat{R}_\alpha (\beta) = e^{-i\beta\frac{\sigma_\alpha}{2}}
$$
($\alpha$ is the axis, $\beta$ is the rotation in radians)

How do we take the exponent of a matrix? There is a 3Blue1Brown video on it. But mostly, SciPy has a function for this - `scipy.linalg.expm()`. It is a very weird but it can be done. We mostly always use $e$ as the base anyway in every thing. 

So you can argue a NOT gate is
$$
\hat{R}_x (\pi) = e^{-i\pi\frac{\sigma_x}{2}}
$$

A theorem I'd present:
$$
\hat{A^2} = \hat{I} \implies
e^{\pm i \theta \hat{A}} = \cos\theta \hat{I} \pm i\sin\theta \hat{A} 
$$

The property of the square of the matrix being identity, makes the matrix **idempotent**. We can prove this using the Maclaurin series of $e^\theta$ so:
$$
e^\theta = 1 + \theta + \frac{\theta^2}{2!} + \frac{\theta^3}{3!} + \dots
$$
Every alternate term (ie. $\theta^\text{even number}$) will be identity. Then using the expansions for $\sin$ and $\cos$ in Maclaurin series, this can be proven. 

Now if we take our rotation by x-axis:
$$
\hat{R}_x(\beta) = e^{-i\beta\frac{\sigma_x}{2}} \\
= e^{-i\frac\beta2\sigma_x}  \\
= \cos(\frac\beta2) \hat{I} - i\sin(\frac\beta2) \sigma_x \quad (\because \sigma_x, \sigma_x^2 = \hat{I})\\ 
= \boxed{
    \begin{bmatrix}
    \cos\Big(\frac\beta2\Big) & -i\sin\Big(\frac\beta2\Big) \\
    -i\sin\Big(\frac\beta2\Big) & \cos\Big(\frac\beta2\Big)
    \end{bmatrix}
}
\quad \text{(Matrix form)}
$$

Now if I plug in $\beta = 180^\circ$ or $2\pi \text{ radians}$, I get:
$$
\begin{bmatrix}
0 & -i \\
-i & 0
\end{bmatrix}
$$ 

Which is a NOT gate because if you factor out a $-i$, you get it as a global phase, which if you recall, isn't observed in measurement.

Take this:
$$
\hat{R_\frac{\hat{x} + \hat{z}}{\sqrt{2}}}(\pi) \quad \text{(Hadamard Gate)} \\
= \exp(-i\pi \Big\{\frac{1}{\sqrt{2}}\frac{\sigma_x}{2} + \frac{1}{\sqrt{2}}\frac{\sigma_z}{\sqrt{2}}\Big\})
$$

Now say a roation by $\beta$ in any general axis $\vec{\sigma}$.

How do you undo a rotation? If it is $\beta$, make it $-\beta$. Similarly:
$$
\Big(\hat{R}_{\vec{\sigma}}(\beta)\Big)^{-1} = \hat{R}_{\vec{\sigma}}(-\beta)
$$
But notice, the LHS is just:
$$
\exp(-i\beta\frac{\vec{\sigma}}{2})
$$ 
And the RHS:
$$
\exp(-i(-\beta)\frac{\vec{\sigma}}{2}) = \exp(+i\beta\frac{\vec{\sigma}}{2})
$$

Notice that just the sign of the $i$ flips. Which is what happens in a complex conjugate. 

All the Pauli matrices:
$$
\sigma_x^\dagger = \sigma_x
$$
$$
\sigma_y^\dagger = \sigma_y \\
$$
$$
\sigma_z^\dagger = \sigma_z
$$

And remember that $\dagger$ is just complex conjugate and then transpose.

So for $\sigma_x$, it is itself since all real numbers and transpose won't affect since diagonals same. Similarly $\sigma_y$, you take the complex conjugate, the shift the $i$'s, you end with the same. Similarly $\sigma_z$, all real numbers. 

So the Pauli matrices are adjoined. They are are $\dagger$'s of themselves. 

So our:
$$
\exp(+i\beta\frac{\vec{\sigma}}{2}) = \Big[\exp(-i\beta\frac{\vec{\sigma}}{2})\Big]^\dagger
$$
by some simple arithmetic since $\vec{\sigma}$ will be adjoined of itself. 

Therefore, **a matrix whose inverse is its adjoined is called a unitary matrix**. In other words
$$
\hat{U}^{-1} = \hat{U}^\dagger
$$
or
$$
\hat{U}\hat{U^\dagger} = \hat{I}
$$.

So in single qubit quantum computing, states are given by vectors, rotation operators by unitary matrices. From the next lecture - Lecture 4 - we shall start with quantum algorithms. 