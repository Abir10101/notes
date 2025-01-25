# Multi-programming v/s Multi-tasking

## Introduction

The goal is to maximize the number of processes in RAM and minimize CPU idle time.

## Multi-programming

- If process P1 is loaded from RAM and given to the CPU, the CPU will execute P1 completely before moving on to P2, P3, or P4.
- When a process initiates an I/O operation, CPU does not sit idle. Another process from the pool of available processes is given to the CPU. The key point is that once the CPU starts executing a process, it continues until that process completes or voluntarily requests an I/O operation.
- This is non-preemtive,  means CPU is not prevented from executing a process completely. Only if the process goes waiting state voluntarily then CPU moves to the next process in queue.

## Multi-tasking

- In multitasking, or time-sharing, we allocate a time slice for each processes. If a process completes within its allocated time, great. Otherwise, it's rescheduled for later.
- This is called preemtive. This means the CPU is prevented from executing the process completely, even if the process does not voluntarily goes into waiting state.
