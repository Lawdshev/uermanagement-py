from typing import Literal

class User:
    def __init__(self, id, username, email, organization, phoneNumber, status, createdAt, password):
        self.id = id
        self.username = username
        self.email = email
        self.organization = organization
        self.phoneNumber = phoneNumber
        self.status = status
        self.createdAt = createdAt
        self.password = password

    def to_dict(self):
        return self.__dict__
