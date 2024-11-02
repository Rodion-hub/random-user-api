from user_data_handler import UserDataHandler


def main():
    api_url = 'https://randomuser.me/api/'

    quantity = int(input("Введите количесвто пользователей для получения: "))

    user_data_handler = UserDataHandler(api_url, quantity)
    users = user_data_handler.fetch_users()

    print(users)


if __name__ == "__main__":
    main()
