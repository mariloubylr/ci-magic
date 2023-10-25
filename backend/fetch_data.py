import json


if __name__ == "__main__":
    f = open("ComplexData.json", "a")
    f.write(json.dumps({"some": {"very": {"complex": "data"}}}))
    f.close()
