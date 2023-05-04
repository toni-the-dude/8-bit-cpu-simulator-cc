from CPU import CPU;
from memory import Memory;

cpuObj = CPU()
memoObj = Memory()
cpuObj.cu.fetch_instructions()
cpuObj.cu.decode_instruction()