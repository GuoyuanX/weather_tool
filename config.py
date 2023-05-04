import json

author = "lng"
version = "2023-4-18"
json_data = ""


def print_info():
    print("============================")
    print("author:", author)
    print("version:", version)
    print("============================")


def read_json():
    global json_data
    with open("./config.json", 'r', encoding='utf_8') as fp:
        json_data = json.load(fp)
    fp.close()


def read_json_config_city():
    return json_data['map'][0]['default_city']


def read_json_config_private_key():
    return json_data['map'][0]['private_key']


def set_json_config_city(city_name):
    json_data['map'][0]['default_city'] = city_name
    with open("./config.json", 'w', encoding='utf-8') as fp:
        json.dump(json_data, fp, ensure_ascii=False)  # ensure_ascii=False 防止写入中文乱码


def set_json_config_private_key(private_key):
    json_data['map'][0]['private_key'] = private_key
    with open("./config.json", 'w', encoding='utf-8') as fp:
        json.dump(json_data, fp, ensure_ascii=False)  # ensure_ascii=False 防止写入中文乱码


def main():
    print_info()


if __name__ == "__main__":
    main()
