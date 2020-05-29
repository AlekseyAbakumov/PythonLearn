import os
import tempfile
import argparse
import json

#creting temp file:
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

#work with file (open and reading):
def get_data():
    if not os.path.exists(storage_path):
        return {}

    with open(storage_path,'r') as f:
        data = f.read()
        if data:
            return json.loads(data)

        return {}

#getting a key:
def get_value(key):
    data = get_data()

    return data.get(key)

#puts the value in the key:
def put_value(key,val):
    data = get_data()

    if key in data:
        data[key].append(val)
    else:
        data[key] = [val]

    with open(storage_path, "w") as f:
        f.write(json.dumps(data))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--key")
    parser.add_argument("--val")

    args = parser.parse_args()

    if args.key and not args.val:
        if get_value(args.key) == None:
            print("None")
        else:
            print(*get_value(args.key), sep=', ')
    elif args.key and args.val:
        put_value(args.key, args.val)


if __name__ == '__main__':
    main()