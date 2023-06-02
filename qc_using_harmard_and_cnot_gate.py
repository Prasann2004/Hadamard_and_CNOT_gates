from qiskit import QuantumCircuit
qc=QuantumCircuit(3)

#wiring the circuit
#reseting all quibits
qc.reset(0)
qc.reset(1)
qc.reset(2)

qc.h(0)#applying hadamard gate
qc.cx(0,1)#applying cnot gate where q0 is controller
qc.cx(0,2)#applying cnot gate where q0 is controller

qc.measure_all()#measuring qubits

qc.draw(output="mpl")#displaying the circuit

