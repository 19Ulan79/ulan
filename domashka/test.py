from decouple import config

a = config("ULAN", default="NNNN")
print(a, type(a))