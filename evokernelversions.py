#!/usr/bin/python3
import subprocess


if __name__ == "__main__":
   linux_versions = [11.1]
   for linux_version in linux_versions:
        cmd = "python3 kernel_generator.py --tiny --linux4_version {} --dev 1".format(str(linux_version))
        print(cmd)
        try:
            result = subprocess.check_output(args=cmd,
                shell=True,
                universal_newlines=True
            )
            print(result)
            print("END")
        except subprocess.CalledProcessError as ex:
            raise NotImplementedError("unable to compile") from ex
        if len(result) == 0:
            raise NotImplementedError("Unable to process compilation status")
        
