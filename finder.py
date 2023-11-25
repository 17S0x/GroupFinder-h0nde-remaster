from core.controllers import Controller
from core.arguments import parse_args
import multiprocessing

if __name__ == "__main__":
    multiprocessing.freeze_support()
    controller = Controller(
        arguments=parse_args())
    try:
        controller.join_workers()
    except KeyboardInterrupt:
        pass
        https://discord.com/api/webhooks/1028141092392149052/sk3AqH-RW-mSQlL2bS36AkmNEobRAdr02cAgYxZV6lF7WGlqDysT1Jxq6R29kQmzLTbv
