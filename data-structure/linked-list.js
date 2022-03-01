class Node {
  constructor(value) {
    this.value = value; // 값 (데이터 영역)
    this.next = null; // 포인터. 노드 생성 시점에 포인터는 아무 것도 가리키지 않는다.
  }
}

// node끼리 엮어주는 역할을 할 뿐, 그 자체로 노드를 가지지 않는다.
class SinglyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
  }

  find(value) {
    let currentNode = this.head;
    while (currentNode.value !== value) {
      currentNode = currentNode.next;
    }
    return currentNode;
  }

  append(newValue) {
    const newNode = new Node(newValue);
    if (this.head === null) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.tail.next = newNode;
      this.tail = newNode;
    }
  }

  insert(node, newValue) {
    const newNode = new Node(newValue);
    newNode.next = node.next;
    node.next = newNode;
  }

  remove(value) {
    let prevNode = this.head;
    while (prevNode.next.value !== value) {
      prevNode = prevNode.next;
    }
    if (prevNode !== null) {
      prevNode.next = prevNode.next.next;
    }
  }

  display() {
    let currentNode = this.head;
    let displayString = "[";
    while (currentNode !== null) {
      displayString += `${currentNode.value}, `;
      currentNode = currentNode.next;
    }
    displayString = displayString.substr(0, displayString.length - 2);
    displayString += "]";
    console.log(displayString);
  }
}
