from memory import Memory;
memory = Memory()

class CPU:

    def __init__(self):
        self.processor = self.Processor()
        self.cu = self.ControlUnit(self.processor)
        self.cache = self.Cache()
        print("Successfully created CPU object.")

    class ControlUnit:

        def __init__(self, processor):
            self.instructions = []
            self.instructionSet = {
                "000": processor.alu.loadA,
                "001": processor.alu.store,
                "010": processor.alu.loadB,
                "011": processor.alu.increment,
                "100": processor.alu.add,
                "101": processor.alu.sub,
                "110": processor.alu.move,
                "111": processor.alu.cmp
            }
            self.currentInstruction = None
            self.processor = processor
            print("-Successfully created ControlUnit object.")

        def fetch(self):
            with open("input.txt", "r") as instructions:
                content = instructions.read()
                print(content)
                self.instructions.append(content)
                print(self.instructions)
                self.instructions = self.instructions[0].splitlines()

        def decode(self):
            for instruction in self.instructions:
            # instruction = self.instructions[0]
                opcode = instruction[:3]
                regAValue = instruction[3:6]
                regBValue = instruction[6:]
                print(opcode)
                print(regAValue)
                print(regBValue)
                if opcode not in ["100", "101"]:
                    self.processor.regA.set_value(regAValue)
                    self.processor.regB.set_value(regBValue)
                print(self.processor.regA.get_value())
                print(self.processor.regB.get_value())
                try:
                    print(self.instructionSet[opcode])
                    self.currentInstruction = self.instructionSet[opcode]
                    return self.execute()
                except KeyError:
                    print("Unavailable instruction.")

        def execute(self):
            return self.currentInstruction()

    class Processor:

        def __init__(self):
            print("-Successfully created Processor object.")
            self.alu = self.ALU(self)
            self.regA = self.Register() 
            self.regB = self.Register()
            # self.decoded_instruction = 0

        class ALU:

            def __init__(self, processor):
                self.processor = processor
                print("--Successfully created ALU object.")

            def loadA(self):
                memory_index = int(self.processor.regA.get_value() + self.processor.regB.get_value(), 2)
                print("Loading value from memory at index: {}".format(memory_index))
                self.processor.regA = memory.read_memory(memory_index)
                return self.processor.regA

            def store(self):
                memory_index = int(self.processor.regA.get_value() + self.processor.regB.get_value(), 2)
                print("Storing value into memory at index: {}".format(memory_index))
                return memory.write_memory(memory_index, self.processor.regA.get_value())

            def add(self):
                pass

            def sub(self):
                pass

            def loadB(self):
                memory_index = int(self.processor.regA.get_value() + self.processor.regB.get_value(), 2)
                print("Loading value from memory at index: {}".format(memory_index))
                self.processor.regB = memory.read_memory(memory_index)
                return self.processor.regB

            def increment(self):
                pass

            def move(self):
                pass

            def cmp(self):
                pass

        class Register:

            def __init__(self):
                self.value = None
                print("--Successfully created Register object.")

            def set_value(self, value): 
                self.value = value

            def get_value(self):
                return self.value

    class Cache:

        def __init__(self):
            print("-Successfully created Cache object.")