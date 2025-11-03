class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  

class MyLinkedList:
    def __init__(self):
        self.head = None  

    def append(self, data):
        """Agregar un nodo al final de la lista"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        """Mostrar todos los elementos de la lista"""
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print(elements)

    def insert_at(self, data, position):
        """Insertar un nodo en una posición específica"""
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        count = 0
        while current and count < position - 1:
            current = current.next
            count += 1
        if not current:
            print("Posición fuera de rango")
            return
        new_node.next = current.next
        current.next = new_node

    def delete_at(self, position):
        """Eliminar un nodo en una posición específica"""
        if not self.head:
            print("Lista vacía")
            return
        if position == 0:
            self.head = self.head.next
            return
        current = self.head
        count = 0
        while current.next and count < position - 1:
            current = current.next
            count += 1
        if not current.next:
            print("Posición fuera de rango")
            return
        current.next = current.next.next
        
# Ejemplo de uso 
if __name__ == "__main__":
    lista = MyLinkedList()
    lista.append(10)
    lista.append(20)
    lista.append(30)
    lista.display()
