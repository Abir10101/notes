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

class Moniter(ABC):
    @abstractmethod
    def assemble(self):
        pass

class MsiMoniter(Moniter):
    def assemble(self):
        print("Assemble Msi Moniter")

class AsusMoniter(Moniter):
    def assemble(self):
        print("Assemble Asus Moniter")


# Factory Classes
class Company(ABC):
    @abstractmethod
    def createGpu(self):
        pass

    @abstractmethod
    def createMoniter(self):
        pass

class MsiManufacturer(Company):
    def createGpu(self):
        return MsiGpu()

    def createMoniter(self):
        return MsiMoniter()

class AsusManufacturer(Company):
    def createGpu(self):
        return AsusGpu()

    def createMoniter(self):
        return AsusMoniter()


# Driver
if __name__ == "__main__":
    msiStore = MsiManufacturer()
    msiGpu = msiStore.createGpu()
    msiGpu.assemble()
    msiMoniter = msiStore.createMoniter()
    msiMoniter.assemble()
    print("=====")
    asusStore = AsusManufacturer()
    asusGpu = asusStore.createGpu()
    asusGpu.assemble()
    asusMoniter = asusStore.createMoniter()
    msiMoniter.assemble()
