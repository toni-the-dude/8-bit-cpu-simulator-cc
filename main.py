from CPU import CPU;
from memory import Memory;

cpuObj = CPU()
memoObj = Memory()
cpuObj.cu.fetch()
print(cpuObj.cu.decode())
