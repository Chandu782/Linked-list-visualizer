import tkinter as tk

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Linked List Visualizer")
        self.root.geometry("800x300")
        self.canvas = tk.Canvas(root, width=780, height=200, bg="white")
        self.canvas.pack(pady=20)

        self.head = None
        self.nodes = []  # for drawing

        # Entry and buttons
        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(side=tk.LEFT, padx=10)

        tk.Button(root, text="Insert at End", command=self.insert_at_end).pack(side=tk.LEFT)
        tk.Button(root, text="Insert at Start", command=self.insert_at_start).pack(side=tk.LEFT, padx=5)
        tk.Button(root, text="Delete by Value", command=self.delete_by_value).pack(side=tk.LEFT, padx=5)
        tk.Button(root, text="Clear", command=self.clear_all).pack(side=tk.LEFT, padx=5)

    def draw_linked_list(self):
        self.canvas.delete("all")
        x = 20
        y = 80
        temp = self.head

        while temp:
            self.canvas.create_rectangle(x, y, x+60, y+40, fill="lightblue")
            self.canvas.create_text(x + 30, y + 20, text=str(temp.data), font=("Arial", 12))

            if temp.next:
                self.canvas.create_line(x + 60, y + 20, x + 100, y + 20, arrow=tk.LAST, width=2)

            x += 80
            temp = temp.next

    def insert_at_end(self):
        value = self.entry.get()
        if value == "":
            return

        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

        self.entry.delete(0, tk.END)
        self.draw_linked_list()

    def insert_at_start(self):
        value = self.entry.get()
        if value == "":
            return

        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

        self.entry.delete(0, tk.END)
        self.draw_linked_list()

    def delete_by_value(self):
        value = self.entry.get()
        if value == "":
            return

        curr = self.head
        prev = None

        while curr:
            if curr.data == value:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                break
            prev = curr
            curr = curr.next

        self.entry.delete(0, tk.END)
        self.draw_linked_list()

    def clear_all(self):
        self.head = None
        self.canvas.delete("all")
        self.entry.delete(0, tk.END)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = LinkedListVisualizer(root)
    root.mainloop()
