from py4web import action


@action("index")
@action.uses('index.html')
def index():
    return dict(message="Hello World")


@action("wallets/")
@action.uses('wallet.html')
def wallets():
    return dict(message="Hello World")

@action("wall")
@action.uses('wall.html')
def wall():
    return dict(message="Hello World")