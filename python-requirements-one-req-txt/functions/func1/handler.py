import json
import pprint
import numpy as np


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NumpyEncoder, self).default(obj)


def func1(event, context):
    input = np.arange(12).reshape(3, 4)
    rot = np.rot90(input, -1)

    print("Input:")
    pprint.pprint(input)
    print()
    print("output:")
    pprint.pprint(rot)

    body = {
        "input": input,
        "output": rot
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body, cls=NumpyEncoder)
    }

    return response
