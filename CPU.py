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
            pass

    class Processor:

        def __init__(self):
            print("-Successfully created Processor object.")
            self.alu = self.ALU()
            self.regA = self.Register() # Accumulator
            self.regB = self.Register() # Program Counter

        class ALU:

            def __init__(self):
                print("--Successfully created ALU object.")

            def load(self):
                pass

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