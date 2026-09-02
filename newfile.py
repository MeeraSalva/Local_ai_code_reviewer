import time

class UserManager:
    def __init__(self):
        self.users = []
        self.cache = {}

    def add_user(self, name, age, email):
        user = {"name": name, "age": age, "email": email}
        self.users.append(user)
        return True

    def get_user_by_email(self, email):
        for u in self.users:
            if u["email"] == email:
                return u

    def remove_user(self, email):
        for i in range(len(self.users)):
            if self.users[i]["email"] == email:
                del self.users[i]

    def calculate_average_age(self):
        # Removed unused variable total
        total = 0
        for u in self.users:
            total += u["age"]
        return total / len(self.users)

    def get_adult_users(self):
        result = []
        for u in self.users:
            if u["age"] >= 18:
                result.append(u)
        return result

    def cache_user_lookup(self, email):
        if email in self.cache:
            return self.cache[email]
        # Simulate slow lookup without using time.sleep
        user = self.get_user_by_email(email)
        self.cache[email] = user
        return user


def process_users(manager, emails):
    results = []
    for e in emails:
        u = manager.get_user_by_email(e)
        results.append(u["name"])
    return results
