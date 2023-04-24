class CPU:

    def __init__(self):
        print("Successfully created CPU object.")
        self.cu = self.ControlUnit()
        self.processor = self.Processor()
        self.cache = self.Cache()

    class ControlUnit:

        def __init__(self):
            print(" Successfully created ControlUnit object.")

    class Processor:

        def __init__(self):
            print(" Successfully created Processor object.")
            self.alu = self.ALU()
            self.regA = self.Register()
            self.regB = self.Register()

        class ALU:

            def __init__(self):
                print("  Successfully created ALU object.")

        class Register:

            def __init__(self):
                print("  Successfully created Register object.")

    class Cache:

        def __init__(self):
            print(" Successfully created Cache object.")