# 8-bit-cpu-simulator-cc
A Python 8-bit CPU simulator for Codecademy's Computer Architecture Portofolio Project.

## Instruction Set

+-------------+-------+-------+-------------+
|   Opcode    |   A   |   B   |   Operation |
+-------------+-------+-------+-------------+
|    000      |   000 |   000 |    LOAD     |
|    001      |   Ra  |   000 |    STORE    |
|    010      |   Ra  |   000 |    ADD      |
|    011      |   Ra  |   Rb  |    SUB      |
|    100      |   Ra  |   Rb  |    MUL      |
|    101      |   Ra  |   Rb  |    DIV      |
|    110      |   Ra  |   Rb  |    MOV      |
|    111      |   Ra  |   Rb  |    CMP      |
+-------------+-------+-------+-------------+
