from memory import Memory;
memory = Memory()

class CPU:

    def __init__(self):
        print("Successfully created CPU object.")
        self.cu = self.ControlUnit()
        self.processor = self.Processor()
        self.cache = self.Cache()

    class ControlUnit:

        def __init__(self):
            print("-Successfully created ControlUnit object.")

        def fetch_instructions(self):
            with open("input.txt", "r") as instructions:
                content = instructions.read()
                print(content)

        def decode_instruction(self, instruction):
            pass

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