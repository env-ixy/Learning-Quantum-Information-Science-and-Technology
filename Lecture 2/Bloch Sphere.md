Bloch sphere is a way to visualise qubits. 

Named after Felix Bloch (1905-1983), a Nobel laureate physicist from Sweden. 

A qubit is any thing with 2 distinguishable states (spin of electron, photon polarisation, anything). It is a superposition of 0 and 1. 

The bloch sphere is a 3d representation of a qubit. It has radius 1. Every qubit lies on the surface of this sphere. +z and -z axes. 

To plot it, you have 2 important angles. $\theta$ which is the angle with the z-axis. $\theta = 0 \implies \text{spin up}$ (in case of electrons, for example. $\ket{0}$ in general cases). $\theta = \pi = 180^\circ$ (mesaured in radians, obviously) is 100% spin down (or $\ket{1}$). 

For anywhere in between, there are loads of possible states, those make a circle around a 2D span of the qubit vector. This necessitates another angle $\phi$. This is the phase. It doesn't govern probablities. But it allows for different qubits to interact with one another.

---

For our example,
- $\theta = 0 \implies \ket{0}$
- $\theta = \pi \implies \ket{1}$
- $\theta = \frac\pi2 \implies \frac{\ket{0} + \ket{1}}{\sqrt{2}}$
- $\theta = \frac{3\pi}{2} \implies \frac{\ket{0} - \ket{1}}{\sqrt{2}}$ 