"""Ticket Counter — Array-Based Circular Queue (FIFO)."""


class ArrayQueue:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Queue capacity must be greater than zero.")
        self.items = [None] * capacity
        self.capacity = capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, customer):
        if self.size == self.capacity:
            print("Queue is full. Cannot add another customer.")
            return False

        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = customer
        self.size += 1
        print(f"Customer added to queue: {customer}")
        return True

    def dequeue(self):
        if self.size == 0:
            print("Queue is empty. No customer to serve.")
            return None

        customer = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        print(f"Now serving: {customer}")
        return customer

    def display(self):
        if self.size == 0:
            print("Queue is empty.")
            return

        print("Customers waiting (front to rear):")
        for offset in range(self.size):
            index = (self.front + offset) % self.capacity
            print(f"{offset + 1}. {self.items[index]}")


def main():
    while True:
        try:
            capacity = int(input("Enter queue capacity: "))
            if capacity > 0:
                break
            print("Capacity must be greater than zero.")
        except ValueError:
            print("Enter a valid integer.")

    queue = ArrayQueue(capacity)

    while True:
        print("\nTICKET BOOKING COUNTER")
        print("1. Enqueue customer")
        print("2. Dequeue / serve customer")
        print("3. Display queue")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Enter customer name or token: ").strip()
            if name:
                queue.enqueue(name)
            else:
                print("Customer name or token cannot be empty.")
        elif choice == "2":
            queue.dequeue()
        elif choice == "3":
            queue.display()
        elif choice == "0":
            print("Ticket counter closed.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()