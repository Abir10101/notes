# Process States

## Introduction

Primary states, mandatory and present by default: ***New***, ***Ready***, ***Running***, ***Terminated***, and ***Waiting***.
Additional states: ***Suspend Wait*** and ***Suspend Ready***.

## 1. New State

The "New" state is when a process is created but not yet running. When we launch an application or even boot computer, processes are initially in the "New" state.

## 2. Ready State

The "Ready" state, sometimes called the "Ready Queue," signifies that a process has been loaded into RAM and is ready for execution.  A **long-term scheduler** selects a process from the new state and loads into RAM, enabling multiple processes ready for execution.

## 3. Running State

The "Running" state means the process has been assigned to the CPU and is actively being executed. In a uniprocessor system, only one process can run at a time.  A **short-term scheduler** selects a process from the Ready state and dispatches it to the CPU for execution.

Sometimes, a running process might be interrupted.  A higher-priority process might arrive, or the process's allocated time slice (time quantum) might expire.  This is called pre-emptive multitasking. The interrupted process returns to the ***Ready state***.

## 4. Terminated State

When the process completes its instructions, it enters the "Terminated" state. This involves deallocation—reclaiming the resources and memory allocated to the process.

## 5. Waiting State

A process might enter the "Waiting" state. This happens when a process requests an I/O operation, such as reading from a file.  The CPU sends the process to wait until the I/O operation completes.  This prevents the CPU from being held up by slow I/O operations.  Once the I/O is finished, the process returns to the ***Ready state***, not directly to Running.

## 6. Suspend Wait & Suspend Ready States

If Wait queue becomes full then processes are moved to a ***Suspend Wait*** state and swapped out to secondary memory.
Similarly, if the Ready queue becomes full, new processes might be placed in a ***Suspend Ready*** state until space becomes available.

This is managed by a **medium-term scheduler**.  This prevents RAM overload. The purpose of the Suspend states is to manage limited RAM effectively.  ***Processes in these states are essentially paused and stored in secondary memory until resources become available***.
