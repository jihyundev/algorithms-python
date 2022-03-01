// https://programmers.co.kr/learn/courses/30/lessons/42587

class Queue {
  constructor() {
    this.queue = [];
    this.front = 0;
    this.rear = 0;
  }

  enqueue(value) {
    this.queue[this.rear++] = value;
  }

  dequeue() {
    const value = this.queue[this.front];
    delete this.queue[this.front];
    this.front += 1;
    return value;
  }

  peek() {
    return this.queue[this.front];
  }

  size() {
    return this.rear - this.front;
  }
}

function solution(priorities, location) {
  let count = 0;
  const queue = new Queue();
  priorities.forEach((priority) => queue.enqueue(priority));

  while (queue.size() > 0) {
    const current = queue.dequeue();
    const max = Math.max(...queue.queue.slice(queue.front));
    if (current < max) {
      queue.enqueue(current);
    } else {
      count++;
      const currentIndex = (queue.front - 1) % priorities.length; // 이게 정확하지가 않음
      if (location === currentIndex) {
        return count;
      }
    }
  }
  return 0;
}

// 이렇게 할 경우 큐에 들어가는 요소들의 원래 위치가 제대로 파악되기가 힘들다. 큐의 front 값은 계속 변하며, 맨 앞에서 enqueue될 경우 그 순서가 무너지기 때문이다.
// 따라서 배열 안에 원래의 위치가 함께 pair로 들어가도록 자료구조를 바꿔보았다.

function solution2(priorities, location) {
  const queue = new Queue();
  for (let i = 0; i < priorities.length; i++) {
    queue.enqueue([priorities[i], i]); // queue에 값과 인덱스를 넣어준다.
  }

  priorities.sort((a, b) => b - a); // 우선순위가 높은 것부터 내림차순으로 정렬

  let count = 0;
  while (queue.size() > 0) {
    const currentValue = queue.peek();
    if (currentValue[0] < priorities[count]) {
      queue.enqueue(queue.dequeue());
    } else {
      const value = queue.dequeue();
      count++;
      if (location === value[1]) {
        return count;
      }
    }
  }
}
const result = solution2([1, 1, 9, 1, 1, 1], 0);
console.log(result);
