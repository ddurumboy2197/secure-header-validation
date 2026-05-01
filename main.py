class HeaderValidation:
    def __init__(self):
        self.required_headers = ["Content-Type", "Authorization"]
        self.allowed_methods = ["GET", "POST", "PUT", "DELETE"]
        self.allowed_content_types = ["application/json", "application/xml"]

    def validate_header(self, headers):
        if not isinstance(headers, dict):
            return False

        for header in self.required_headers:
            if header not in headers:
                return False

        if "Authorization" in headers:
            if not isinstance(headers["Authorization"], str):
                return False
            if not headers["Authorization"].startswith("Bearer "):
                return False

        if "Content-Type" in headers:
            if headers["Content-Type"] not in self.allowed_content_types:
                return False

        if "Method" in headers:
            if headers["Method"] not in self.allowed_methods:
                return False

        return True

# Misol foydalanish:
validation = HeaderValidation()
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer token",
    "Method": "POST"
}
print(validation.validate_header(headers))  # True

headers = {
    "Content-Type": "application/json",
    "Method": "POST"
}
print(validation.validate_header(headers))  # False
