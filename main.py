import Services.mongo_setup as mongo_setup
import Services.data_service as svc

import Services.fast_api as fa
import uvicorn
import json


def read_secrets():
    with open("secrets.json", "r") as read_file:
        data = json.load(read_file)
    return data


def main():
    secrets = read_secrets()
    mongo_setup.global_init(secrets)

    #svc.createUser("poog", "poog@gamr.com", "yeet")
    print(svc.findUserByEmail("poog@gamr.com").name)


    app = fa.app
    uvicorn.run(app, host="0.0.0.0", port=8000)



if __name__ == '__main__':
    main()

