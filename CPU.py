from memory import Memory;
import random

memory = Memory()

class CPU:

    def __init__(self):
        self.processor = self.Processor()
        self.cu = self.ControlUnit(self.processor)
        print("Successfully created CPU object.")

    class ControlUnit:

        def __init__(self, processor):
            self.instructions = []
            self.instructionSet = {
                "000": processor.alu.loadA,
                "001": processor.alu.store,
                "010": processor.alu.loadB,
                "011": processor.alu.flip,
                "100": processor.alu.add,
                "101": processor.alu.sub,
                "110": processor.alu.swap,
                "111": processor.alu.generate
            }
            self.currentInstruction = None
            self.processor = processor
            print("-Successfully created ControlUnit object.")

        def fetch(self):
            print("Preparing to fetch input...")
            with open("input.txt", "r") as instructions:
                content = instructions.read()
                print("All unfiltered instructions: {}".format(content))
                self.instructions.append(content)
                print(self.instructions)
                self.instructions = self.instructions[0].splitlines()

        def decode(self):
            print("Decoding instructions...")
            for instruction in self.instructions:
            # instruction = self.instructions[0]
                print("\nCurrent instruction: {}".format(instruction))
                opcode = instruction[:3]
                regAValue = instruction[3:6]
                regBValue = instruction[6:]
                # print("Opcode: {}".format(opcode))
                # print("regAValue: {}".format(regAValue))
                # print("regBValue: {}".format(regBValue))
                if opcode in ["000", "001", "010"]:
                    self.processor.regMemory.set_value(regAValue + regBValue)
                # print(self.processor.regA.get_value())
                # print(self.processor.regB.get_value())
                try:
                    # print(self.instructionSet[opcode])
                    self.currentInstruction = self.instructionSet[opcode]
                    print(self.execute())
                except KeyError:
                    print("Unavailable instruction.")

        def execute(self):
            print("Executing instruction...")
            self.currentInstruction()

    class Processor:

        def __init__(self):
            print("-Successfully created Processor object.")
            self.alu = self.ALU(self)
            self.regA = self.Register() 
            self.regB = self.Register()
            self.regMemory = self.Register()

        class ALU:

            def __init__(self, processor):
                self.processor = processor
                print("--Successfully created ALU object.")

            def loadA(self):
                memory_index = int(self.processor.regMemory.get_value(), 2)
                print("Loading value from memory at index: {}".format(memory_index))
                self.processor.regA = memory.read_memory(memory_index)

            def store(self):
                memory_index = int(self.processor.regMemory.get_value(), 2)
                print("Storing value into memory at index: {}".format(memory_index))
                return memory.write_memory(memory_index, self.processor.regA.get_value())

            def add(self):
                regAValue = self.processor.regA.get_value() # String
                regBValue = self.processor.regB.get_value() # String
                result = ""
                index = -1
                carry = 0
                print("Adding\n{} and\n{}...".format(regAValue, regBValue))

                while abs(index) <= min(len(regAValue), len(regBValue)):
                    
                    if regAValue[index] == "1" and regBValue[index] == "1":
                        if carry == 1:
                            result = "1" + result
                        else:
                            result = "0" + result
                            carry = 1

                    elif regAValue[index] == "1" or regBValue[index] == "1":
                        if carry == 1:
                            result = "0" + result
                        else:
                            result = "1" + result

                    else:
                        if carry == 1:
                            result = "1" + result
                            carry = 0
                        else:
                            result = "0" + result

                    # print("Current result {}".format(result))
                    index -= 1

                print("Result of addition: {}".format(result))

            def sub(self):
                regAValue = self.processor.regA.get_value() # String
                regBValue = self.processor.regB.get_value() # String
                result = ""
                index = -1
                borrow = 0
                print("Subtracting\n{} from\n{}...".format(regBValue, regAValue))

                while abs(index) <= max(len(regAValue), len(regBValue)):
                    
                    if regAValue[index] == "1" and regBValue[index] == "0":
                        if borrow == 1:
                            result = "0" + result
                            borrow = 0
                        else:
                            result = "1" + result

                    elif regAValue[index] == "0" and regBValue[index] == "1":
                        if borrow == 1:
                            result = "0" + result
                        else:
                            result = "1" + result
                            borrow = 1

                    elif regAValue[index] == "1" and regBValue[index] == "1":
                        if borrow == 1:
                            result = "1" + result
                        else:
                            result = "0" + result

                    else:
                        if borrow == 1:
                            result = "1" + result
                        else:
                            result = "0" + result

                    # print("Current result {}".format(result))
                    index -= 1

                print("Result of subtraction: {}".format(result))

            def loadB(self):
                memory_index = int(self.processor.regMemory.get_value(), 2)
                print("Loading value from memory at index: {}".format(memory_index))
                self.processor.regB = memory.read_memory(memory_index)

            def flip(self):
                print("Flipping the bits of registers A and B...")
                regAValue = self.processor.regA.get_value() # String
                regBValue = self.processor.regB.get_value() # String
                index = -1
                flippedRegA = ""
                flippedRegB = ""
                lenA = len(regAValue)
                lenB = len(regBValue)
                print("Register A before flip: {}".format(self.processor.regA.get_value()))
                print("Register B before flip: {}".format(self.processor.regB.get_value()))

                while lenA < 8:
                    regAValue = "0" + regAValue
                    # print("Preparing to flip regAValue: {}".format(regAValue))
                    lenA += 1

                while lenB < 8:
                    regBValue = "0" + regBValue
                    # print("Preparing to flip regBValue: {}".format(regBValue)) 
                    lenB += 1

                while abs(index) < 8:

                    if regAValue[index] == "0":
                        flippedRegA = "1" + flippedRegA
                    else:
                        flippedRegA = "0" + flippedRegA

                    if regBValue[index] == "0":
                        flippedRegB = "1" + flippedRegB
                    else:
                        flippedRegB = "0" + flippedRegB

                    index -= 1
                    # print(index)

                self.processor.regA.set_value(flippedRegA)
                self.processor.regB.set_value(flippedRegB)
                print("Register A after flip: {}".format(self.processor.regA.get_value()))
                print("Register B after flip: {}".format(self.processor.regB.get_value()))

            def swap(self):
                print("Swapping the values of register A and B...")
                print("Register A before swap: {}".format(self.processor.regA.get_value()))
                print("Register B before swap: {}".format(self.processor.regB.get_value()))
                regAValue = self.processor.regA.get_value() # String
                regBValue = self.processor.regB.get_value() # String
                self.processor.regA.set_value(regBValue)
                self.processor.regB.set_value(regAValue)
                print("Register A after swap: {}".format(self.processor.regA.get_value()))
                print("Register B after swap: {}".format(self.processor.regB.get_value()))              

            def generate(self):
                print("Generating a random value for register A...")
                decimal = random.randint(0, 255)
                binary = bin(decimal)[2:].zfill(8)
                self.processor.regA.set_value(binary)
                print("Generated value: {}".format(binary))

        class Register:

            def __init__(self):
                self.value = "0"
                print("--Successfully created Register object.")

            def set_value(self, value): 
                self.value = value

            def get_value(self):
                return self.value