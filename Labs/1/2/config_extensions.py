import importlib
import os
import magic  # to recognize file type
import re

file_types = ["ELF 64-bit", "PE32+", "7-zip", "POSIX tar", "pcap-ng", "ASCII text", "Zip", "MP4", "MS Windows shortcut",
              "Debian binary package"]

spec = importlib.util.spec_from_file_location("solution.py", "C:/Users/user/Desktop/test/Labs/1/1/solution.py")
find_file = importlib.util.module_from_spec(spec)
spec.loader.exec_module(find_file)
for root, dirs, files in os.walk(os.path.join(os.getcwd(), "samples")):
    for file in files:
        full_file_type = magic.from_file(os.path.join(root, file))
        for file_type in file_types:
            if file_type in full_file_type:
                pattern = file_type
                required_type = re.findall(pattern, full_file_type)
                if file_type == "pcap-ng":
                    required_type[0] = required_type[0].replace("-", "")
                if file_type == "PE32+":
                    required_type[0] += "+"
                # if file already has extension
                os.rename(os.path.join(root, file), os.path.join(root, file.replace("." + required_type[0], "")))
                file = file.replace("." + required_type[0], "")

                os.rename(os.path.join(root, file.replace("." + required_type[0], "")),
                          os.path.join(root, file + "." + required_type[0]))
