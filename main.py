"""
main.py
gamr
run python3 main.py to start the server
"""


import Services.mongo_setup as mongo_setup
import Services.fast_api as fa
from testing import runTests
import uvicorn
import json

# opens authentication information for remote connection to mongo database
def read_secrets():
    with open("secrets.json", "r") as read_file:
        data = json.load(read_file)
    return data


def main():
    secrets = read_secrets()
    mongo_setup.global_init(secrets)

    # print(runTests())

    app = fa.app
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == '__main__':
    main()
