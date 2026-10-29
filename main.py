from nodes.load_dataset_node import load_dataset_node
from model.state import OverAllState
def main():
    print("Hello from micro1-eval-hackathon-26!")

    initial_state = OverAllState(
        input="Your Query Here",
        files=[r"test.txt"]
    )

    load_dataset_node(initial_state)
if __name__ == "__main__":
    main()
