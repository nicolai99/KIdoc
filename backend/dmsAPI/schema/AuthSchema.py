from ninja import Schema


class AuthSchema(Schema):
    username: str
    password: str
