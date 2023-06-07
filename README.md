# 8-bit-cpu-simulator-cc
A Python 8-bit CPU simulator for Codecademy's Computer Architecture Portofolio Project.

## Instruction Set

+-------------+-------+-------+-------------+
|   Opcode    |   A   |   B   |   Operation |
+-------------+-------+-------+-------------+
|    000      |Memory | Index |    LOAD(Ra) |
|    001      |Memory | Index |    STORE(Ra)|
|    010      |Memory | Index |    LOAD(Rb) |
|    011      |   00  |   00  |    FLIP     |
|    100      |   00  |   00  |    ADD      |
|    101      |   00  |   00  |    SUB      |
|    110      |   00  |   00  |    SWAP     |
|    111      |   00  |   00  |    GEN      |
+-------------+-------+-------+-------------+
