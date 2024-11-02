from api_client import APIClient


class UserDataHandler:
    def __init__(self, api_url, quantity):
        self.api_url = api_url
        self.quantity = quantity
        self.api_client = APIClient(api_url)

    def fetch_users(self):
        users = []
        total_fetched = 0

        while total_fetched < self.quantity:
            response = self.api_client.get()
            if response and 'results' in response:
                for user in response['results']:
                    if total_fetched < self.quantity:
                        user_info = {
                            'gender': user['gender'],
                            'name': user['name'],
                            'email': user['email'],
                            'location': {
                                'city': user['location']['city'],
                                'country': user['location']['country']
                            },
                            'dob': {
                                'date': user['dob']['date'],
                                'age': user['dob']['age']
                            },
                            'phone': user['phone']
                        }
                        users.append(user_info)
                        total_fetched += 1
            else:
                print("Failed to retrieve data or no results found.")
                break

        return users
