class AutoBuildEnabledError(Exception):
    def __init__(self, msg: str = "Autobuild Enabled: cannot build again. Just skip the build method.") -> None:
        print(msg)
