import json
import os

ADDITIONAL_PACKAGE = "ADDITIONAL_PACKAGE"
OVERWRITE_PACKAGE = "OVERWRITE_PACKAGE"
OUTPUT_PACKAGE = "OUTPUT_PACKAGE"

FILES = {
    "package.json": {
        ADDITIONAL_PACKAGE: "package-additional.json",
        OVERWRITE_PACKAGE: "package-overwrite.json",
        OUTPUT_PACKAGE: "package.json"
    },
    "gulpfile.js": {
        ADDITIONAL_PACKAGE: "",  # additional not supported
        OVERWRITE_PACKAGE: "gulpfile-overwrite.js",
        OUTPUT_PACKAGE: "gulpfile.js"
    }
}


def updatedict(a, b):
    for key in b:
        if not key in a or type(a[key]) != dict or type(b[key]) != dict:
            a[key] = b[key]
        else:
            updatedict(a[key], b[key])


if __name__ == '__main__':
    for core_package, file in FILES.items():
        print(file.get(OVERWRITE_PACKAGE))
        if os.path.isfile(file.get(OVERWRITE_PACKAGE)):
            print(core_package, file)
            with open(file.get(OUTPUT_PACKAGE), "w") as fout:
                fout.write(open(file.get(OVERWRITE_PACKAGE)).read())
        elif os.path.isfile(file.get(ADDITIONAL_PACKAGE)):
            with open(core_package) as fin1:
                data1 = json.load(fin1)
            with open(file.get(ADDITIONAL_PACKAGE)) as fin2:
                data2 = json.load(fin2)
            updatedict(data1, data2)
            with open(file.get(OUTPUT_PACKAGE), "w") as fout:
                json.dump(data1, fout, indent=4)
