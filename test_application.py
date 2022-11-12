import requests
import json


def test_get_all_users():

    users_url = "http://127.0.0.1:5011/api/users"

    try:
        users_message = requests.get(users_url)
        if users_message.status_code == 200:
            print("\n\n Congratulations. Your end-to-end test worked. \n\n")
            print("Application users message = \n")
            data = users_message.json()
            print(json.dumps(data, indent=2))
            print("\n")
        else:
            print("\n\n Epic Fail. Status code = ", users_message.status_code, "\n\n")
            print("\n")
    except Exception as e:
        print("\n\n Epic, Epic, Epic Fail. Exception = ", e, "\n\n")
        print("\n")


if __name__ == "__main__":
    test_get_all_users()


