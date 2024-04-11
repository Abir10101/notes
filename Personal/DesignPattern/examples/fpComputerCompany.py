from abc import ABC, abstractmethod


# Product Classes
class Gpu(ABC):
    @abstractmethod
    def assemble(self):
        pass

class MsiGpu(Gpu):
    def assemble(self):
        print("Assemble Msi Gpu")

class AsusGpu(Gpu):
    def assemble(self):
        print("Assemble Asus Gpu")


# Factory Classes
class Company():
    @abstractmethod
    def createGpu(self):
        pass

    def assembleGpu(self):
        gpu = self.createGpu()
        gpu.assemble()
        return gpu

class MsiManufacturer(Company):
    def createGpu(self):
        return MsiGpu()

class AsusManufacturer(Company):
    def createGpu(self):
        return AsusGpu()


# Driver
if __name__ == "__main__":
    msiStore = MsiManufacturer()
    msiStore.assembleGpu()
    print("=====")
    asusStore = AsusManufacturer()
    asusStore.assembleGpu()
