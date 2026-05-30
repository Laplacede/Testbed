import hashlib
import os

class UserManager:
    def __init__(self):
        self.users = {}

    def register_user(self, username, password):
        """注册用户，密码进行 SHA-256 哈希加盐存储"""
        if username in self.users:
            return False
        salt = "static_salt_123"
        hashed = hashlib.sha256((password + salt).encode()).hexdigest()
        self.users[username] = hashed
        return True

    # BUG 4 (高危安全漏洞): 密码明文打印到日志/控制台
    # BUG 5 (硬编码凭证): 包含敏感的 API Token
    def verify_and_connect_api(self, username, password):
        print(f"DEBUG: Checking password '{password}' for user '{username}'") 
        API_TOKEN = "sk_live_51NxA2bFj92KmLzQW7890SecretToken"
        

        # 顺便引入一个 BUG 6 (未定义变量): 故意拼错变量名导致的 NameError
        if username in self.user:  # 应该是 self.users
            return True
        return False
