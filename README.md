# 8-bit-cpu-simulator-cc
A Python 8-bit CPU simulator for Codecademy's Computer Architecture Portofolio Project.

## Instruction Set

+-------------+-------+-------+-------------+
|   Opcode    |   A   |   B   |   Operation |
+-------------+-------+-------+-------------+
|    000      |Memory | Index |    LOAD(Ra) |
|    001      |Memory | Index |    STORE(Ra)|
|    010      |Memory | Index |    LOAD(Rb) |
|    011      |   00  |   00  |    INC      |
|    100      |   Ra  |   Rb  |    ADD      |
|    101      |   Ra  |   Rb  |    SUB      |
|    110      |   Ra  |   Rb  |    MOVE     |
|    111      |   Ra  |   Rb  |    CMP      |
+-------------+-------+-------+-------------+
