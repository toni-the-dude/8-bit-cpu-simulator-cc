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
                "000": processor.alu.load,
                "001": processor.alu.store,
                "010": processor.alu.add,
                "011": processor.alu.sub,
                "100": processor.alu.mul,
                "101": processor.alu.div,
                "110": processor.alu.move,
                "111": processor.alu.cmp
            }
            print("-Successfully created ControlUnit object.")

        def fetch_instructions(self):
            with open("input.txt", "r") as instructions:
                content = instructions.read()
                print(content)
                self.instructions.append(content)

        def decode_instruction(self):
            opcode = self.instructions[0][:3]
            print(opcode)
            try:
                print(self.instructionSet[opcode])
            except KeyError:
                print("Unavailable instruction.")

    class Processor:

        def __init__(self):
            print("-Successfully created Processor object.")
            self.alu = self.ALU()
            self.regA = self.Register() # Accumulator
            self.regB = self.Register() # Program Counter
            self.decoded_instruction = 0

        class ALU:

            def __init__(self):
                print("--Successfully created ALU object.")

            def load(self):
                memory.read_memory(self.decoded_instruction)

            def store(self):
                pass

            def add(self):
                pass

            def sub(self):
                pass

            def mul(self):
                pass

            def div(self):
                pass

            def move(self):
                pass

            def cmp(self):
                pass

        class Register:

            def __init__(self):
                print("--Successfully created Register object.")

    class Cache:

        def __init__(self):
            print("-Successfully created Cache object.")