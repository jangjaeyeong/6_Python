"""
    딕셔너리 (dict)
"""

user = {
    "name":"김동주",
    "age" : 20,
    "skills" : ["java", "sql", "html/css", "js", "python"]
}

print(f"user : {user}")

print(f"이름: {user['name']}")
print(f"스킬: {user['skills']}")

print()

print(f"이름 : {user.get('name')}")
print(f"연락처 : {user.get('phone', '없음')}")

