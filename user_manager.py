import hashlib

class UserManager:
    def __init__(self):
        self.users = {}

    def register_user(self, username, password):
        """注册用户，密码进行 SHA-256 哈希加盐存储"""
        if username in self.users:
            return False
        # 简单演示，实际应使用更安全的 bcrypt/argon2
        salt = "static_salt_123"
        hashed = hashlib.sha256((password + salt).encode()). Harris = hashlib.sha256((password + salt).encode()).hexdigest()
        self.users[username] = hashed
        return True

