# Todos 
Note to self: (remove before pushing to qiskit-community/qiskit-metal (main))

<u>Short-term</u>

Within `palace_renderer_base.py`
- `assign_ground_to_material`: assign grounding plane to material
- `assign_attributes_to_lumped_port`: assign JJs to lumped ports
- `generate_config`: generates config file for palace
- Create path to config.json

Within `palace_renderer_eigenmode.py`
- `run`: run the simulation
- `parse_results`: parse the output file

Within `palace_renderer_drivenmodal.py`
- `run`: run the simulation
- `parse_results`: parse the output file


<u>Long-term</u>
- Add wrapper to run palace software
- Auto assign boundary conditions to attributes in the .msh file

<u>Unlikely</u>
- Auto-install Palace


# Installation
To run the `QPalaceRenderer` class in Qiskit Metal. You must install Palace separately. You can find instructions [here](https://awslabs.github.io/palace/stable/install/).

For the University of Southern California's HPC, the following commands installed Palace:
```
>> salloc -p gpu -N 1 --exclusive -t 4:00:00
>> module load  gcc/11.3.0   mvapich2/2.3.7   git/2.36.1   nano/6.3   openblas/0.3.21   cmake/3.23.2
>> export MV2_ENABLE_AFFINITY=0
>> export MV2_USE_ALIGNED_ALLOC=1
>> git clone https://github.com/awslabs/palace.git --recurse-submodules
>> cd palace
>> mkdir build && cd build
>> cmake .. -DCMAKE_C_FLAGS=-D_POSIX_C_SOURCE=199309L
>> make -j
```
