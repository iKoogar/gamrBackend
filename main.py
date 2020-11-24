import Services.mongo_setup as mongo_setup
import Services.data_service as svc
from fastapi import FastAPI, Query

import Services.fast_api as fa
import uvicorn
import json

app = FastAPI()


def read_secrets():
    with open("secrets.json", "r") as read_file:
        data = json.load(read_file)
    return data


def main():
    secrets = read_secrets()
    mongo_setup.global_init(secrets)


    uvicorn.run(app, host="0.0.0.0", port=8000)

    #svc.createUser("poog", "poog@gamr.com", "yeet")
    svc.find_user_by_email("poog@gamr.com")


if __name__ == '__main__':
    main()