from task_bots.Qreserve import run_bot
import sys

if __name__ == "__main__":
    if sys.argv[1] == 'test':
        run_bot(True)
    else:
        run_bot(False)
