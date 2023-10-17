from RunningSneakers import*
from ProtectedSneakers import*
from WinterSneakers import*
from Scripts import*
import os

if __name__ == "__main__":
    runningSneakers = RunningSneakers("Puma", "First mile", "Black", 43, True, "Sport")
    protectedSneakers = ProtectedSneakers("Nike", "Running Pro", "White", 41, False, "Casual")
    winterSneakers = WinterSneakers("Adidas", "Snow Trek", "Blue", 45, True, "Winter Sports")

    writeCharacteristicsToFile(runningSneakers, "file")
    runningSneakersCopy = RunningSneakers(*readCharacteristicsFromFile(os.path.join(os.getcwd(), "file.txt")))
    writeCharacteristicsToFile(runningSneakersCopy, "fileCOPY")