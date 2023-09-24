import os
files = os.listdir(r"C:\Users\HP\Desktop\Notes\computer\pseudocode")
programs = [f for f in files if f.endswith(".pseudo")]
n = len(programs)
new_file = "program" + str(n+1) + ".pseudo"
open(new_file, "w").close()

