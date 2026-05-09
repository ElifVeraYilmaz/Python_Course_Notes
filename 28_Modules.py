# We will use the code from the converter file in another file.

import Converters_Ex_File
from Converters_Ex_File import kg_to_lbs # With ctrl space I can see options. 

print(kg_to_lbs(100))

print(Converters_Ex_File.kg_to_lbs(70))