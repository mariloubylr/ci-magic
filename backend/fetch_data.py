import json
import os
import sys


if __name__ == "__main__":
    data_dir = sys.argv[1]
    f = open(os.path.join(data_dir, "ComplexData.json"), "a")
    f.write(json.dumps({"some": {"very": {"complex": "data"}}}))
    f.close()
