# **Missionaries and Cannibals Problem **

## ** Overview**  
The **Missionaries and Cannibals** problem is a classic AI puzzle that requires safely transporting three missionaries and three cannibals across a river using a boat, while ensuring that at no point do the cannibals outnumber the missionaries on either side.

## ** Problem Statement**  
- There are **three missionaries** and **three cannibals** on the left side of a river.  
- A **boat** that can hold at most **two people** is available for crossing.  
- The goal is to move all missionaries and cannibals to the right side **safely**.  
- At no point should **cannibals outnumber missionaries** on either side, or the missionaries will be eaten.  

## ** State Representation**  
Each state is represented as:
```(M_left, C_left, B_left, M_right, C_right, B_right)```
Where:  
- `M_left`, `C_left` → Number of missionaries and cannibals on the **left** bank.  
- `M_right`, `C_right` → Number of missionaries and cannibals on the **right** bank.  
- `B_left`, `B_right` → Boat position (**1 = left, 0 = right**).  

### ** Initial State**  
``` (3, 3, 0, 0, 0, 0)```
- All missionaries and cannibals are on the **left bank**.  
- The boat is also on the left.  

### ** Goal State**  
``` (0, 0, 0, 3, 3, 1)```
- All missionaries and cannibals successfully reach the **right bank**.  

## **🚤 Valid Moves**  
The boat can carry:  
1. **(1C)** → Move *one cannibal*.  
2. **(2C)** → Move *two cannibals*.  
3. **(1M)** → Move *one missionary*.  
4. **(2M)** → Move *two missionaries*.  
5. **(1C1M)** → Move *one cannibal and one missionary*.  

### **⚠️ Constraints**
- The boat **cannot be empty** during a trip.  
- The boat **cannot carry more than two people**.  
- **Missionaries must never be outnumbered** by cannibals on either side.  

## **🔍 Search Algorithms Used**  
We explore solutions using the following **uninformed search strategies**:  

### **1️⃣ Breadth-First Search (BFS)**
✔ Explores all possible states **level by level**.  
✔ **Guarantees the shortest path**.  
✔ Uses a **queue (FIFO)** for exploration.  

### **2️⃣ Depth-First Search (DFS)**
✔ Explores a **path deeply** before backtracking.  
✔ Uses a **stack (LIFO)**.  
✔ May **not find the shortest path**.  

### **3️⃣ Iterative Deepening Search (IDS)**
✔ Combines **DFS and BFS advantages**.  
✔ Runs **DFS with increasing depth limits** until the goal is found.  

## **📌 Graph Representation**  
The state space can be visualized as a **directed graph** where:  
- **Nodes** represent valid states.  
- **Edges** represent valid moves.  

Graphs are generated using **NetworkX** and visualized with **Matplotlib**.  

## **💻 Implementation Details**  
- The solution is implemented in **Python**.  
- The state space is explored using **BFS, DFS, and IDS**.  
- The graph is displayed for better visualization.  

-