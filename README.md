# 8-bit-cpu-simulator-cc
A Python 8-bit CPU simulator for Codecademy's Computer Architecture Portofolio Project.

## Instruction Set

`+-------------+-------+-------+-------------+`<br>
`|   Opcode    |   A   |   B   |   Operation |`<br>
`+-------------+-------+-------+-------------+`<br>
`|    000      |Memory | Index |    LOAD(Ra) |`<br>
`|    001      |Memory | Index |    STORE(Ra)|`<br>
`|    010      |Memory | Index |    LOAD(Rb) |`<br>
`|    011      |   RA  |   RB  |    FLIP     |`<br>
`|    100      |   RA  |   RB  |    ADD      |`<br>
`|    101      |   RA  |   RB  |    SUB      |`<br>
`|    110      |   RA  |   RB  |    SWAP     |`<br>
`|    111      |   RA  |   00  |    GEN      |`<br>
`+-------------+-------+-------+-------------+`<br>

The input.txt file contains all the instructions to be executed. They are in 8-bit format, with the first 3 bits representing the operation code, while the next were meant to be split between two general purpose registers. Eventually, I decided to use those 5-bits for specifying the memory index. I did not realize until later how limiting 8-bit is when it comes to what numbers I can perform operations on, so eventually the 5-bits become obsolete, except for the 3 operations that need a memory index. The values in both general registers are 8-bit, because they do not need to be specified in the instruction and are generated randomly with the generate() function.

I will describe all the available operations:<br>
LOAD(Ra) = Loads a value from the specified memory index into general purpose register A<br>
LOAD(Rb) = Loads a value from the specified memory index into general purpose register B<br>
STORE(Ra)= Stores whatever value register A holds into the specified memory index<br>
FLIP = Flips the bits of both registers<br>
ADD = Performs bitwise addition between the two general purpose registers<br>
SUB = Performs bitwise subtraction between the two general purpose registers<br>
SWAP = Swaps the values of the two general purpose registers<br>
GEN = Generates a random 8-bit value for register A<br>

The values that the program handles represent unsigned 8-bit integers.
