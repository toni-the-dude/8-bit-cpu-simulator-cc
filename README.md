# 8-bit-cpu-simulator-cc
A Python 8-bit CPU simulator for Codecademy's Computer Architecture Portofolio Project.

## Instruction Set

+-------------+-------+-------+-------------+
|   Opcode    |   A   |   B   |   Operation |
+-------------+-------+-------+-------------+
|    000      |Memory | Index |    LOAD     |
|    001      |   Ra  |   00  |    STORE    |
|    010      |   Ra  |   00  |    ADD      |
|    011      |   Ra  |   Rb  |    SUB      |
|    100      |   Ra  |   Rb  |    MUL      |
|    101      |   Ra  |   Rb  |    DIV      |
|    110      |   Ra  |   Rb  |    MOVE     |
|    111      |   Ra  |   Rb  |    CMP      |
+-------------+-------+-------+-------------+
