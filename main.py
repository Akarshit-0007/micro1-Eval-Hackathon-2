from model.state import OverAllState
from graph import app
def main():
    print("Hello from micro1-eval-hackathon-26!")

    initial_state = OverAllState(
        input="What is the topic of these files",
        files=[r"test.txt","test2.txt","test3.txt","test4.txt"]
    )

    app.invoke(initial_state)
if __name__ == "__main__":
    main()
