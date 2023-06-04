# The memory is comprised of BYTES * 8 cells of memory, each containing a string that is either '0' or '1'.
# The bundle of 8-bits stores instructions formatted according to the ISA.

BYTES = 32

class Memory:
    
    def __init__(self):
        self.memoryMatrix = [['0'] * 8] * BYTES
        print("Successfully created Memory object.")

    def read_memory(self, memoryIndex):
        print("Returning {} from index {}, formatted as {}.".format(self.memoryMatrix[memoryIndex], memoryIndex, ''.join(self.memoryMatrix[memoryIndex])))
        return ''.join(self.memoryMatrix[memoryIndex]) # Returns an 8-bit string representing a binary value

    def write_memory(self, memoryIndex):
        print("Writing {} to memory at index {}.".format(self.memoryMatrix[memoryIndex], memoryIndex))
        return None # Returns an 8-bit string representing a binary value