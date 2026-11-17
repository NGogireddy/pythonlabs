from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Create circuit
qc = QuantumCircuit(1, 1)

# Apply Hadamard and measure
qc.h(0)
qc.measure(0, 0)

# Inspect circuit
print(qc.draw())
print("Qubits:", qc.num_qubits)
print("Classical bits:", qc.num_clbits)
print("Circuit depth:", qc.depth())

# Execute circuit
simulator = AerSimulator()
job = simulator.run(qc, shots=1000)

# Retrieve measurement results
result = job.result()
counts = result.get_counts()

print("Measurement counts:", counts)

total_counts = sum(counts.values())

assert total_counts == 1000
assert "0" in counts
assert "1" in counts

print("Total shots:", total_counts)
print("Probability of 0:", counts.get("0", 0) / total_counts)
print("Probability of 1:", counts.get("1", 0) / total_counts)

"""
Learning: 
Qiskit allows quantum circuits to be described using circuit instructions. Qiskit Aer simulates their execution and 
returns sampled measurement results. An ideal Hadamard circuit applied to |0⟩ produces approximately 50% zeros and 50% 
ones over repeated shots.

Hadamard and Measure both are instructions. Depth will be 2 in the above circuit. 
QuantumCircuit is to build the circuit. 
AerSimulator is to simulate the circuit, execute it and measure the outcomes. 

simulator = AerSimulator() --> creates a simulator that can execute our quantum circuit
job = simulator.run(qc, shots=1000) --> runs the simulator for 1000 times and the results are stored in job. 

result = job.result()   --> Retrieves the result from the job. 
counts = result.get_counts()    --> Gets the counts of the output i.e, number of times we get 0's and 1's. 
"""
