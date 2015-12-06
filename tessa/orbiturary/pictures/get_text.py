import subprocess
import os

li = [i for i in os.walk(os.getcwd())]

print(li)

for di in li:
    root = di[0]
    for fi in di[2]:
        lent = len(fi)
        if fi[lent-4:lent] == ".jpg":
            fi_path = os.path.join(root, fi)
            output_file = fi[:lent-4] + "_output"
            print(output_file)
            subprocess.call(["tesseract", fi, output_file])

