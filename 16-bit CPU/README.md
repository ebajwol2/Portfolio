16-bit CPU — Custom HDL Processor
=================================

GitHub Repo Description (Short)
-------------------------------

Custom 16-bit CPU written in HDL. Includes ALU, registers, instruction control, PC, RAM/ROM, and runs a Tetris-like program in simulation.

Full Description
----------------

Designed and implemented a 16-bit CPU from scratch, including datapath and control logic. Verified correctness by successfully running a small Tetris-like program in the simulator.

Architecture Components
-----------------------

- ALU (add, sub, logic ops)
- Register file
- Program counter + instruction control
- ROM instruction memory
- RAM data memory
- Simple pipeline-style staged execution

Testing
-------

- Simulation using custom testbench
- Tetris-like program executed to validate full instruction flow

Tools
-----

HDL, ModelSim/Verilator


