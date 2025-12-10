from functools import wraps
def logging_decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"🚀 calling {func.__name__}")
        func(*args, **kwargs)
        print(f"✅ finished calling {func.__name__}")
    return wrapper

@logging_decorator
def brew_chai(type,milk="no"):
    print(f"Brewing {type} chai and milk status {milk}")

brew_chai("masala")
brew_chai("Ginger")