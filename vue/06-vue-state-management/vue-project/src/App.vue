<template>
<<<<<<< HEAD
<div>
<h1>Todo Project</h1>
<h2> 완료된 Todo: {{ store.doneTodosCount }} </h2>
<TodoList />
<TodoForm />

</div>
 <!-- <p>{{ nuwNumber }}</p>
 <p>{{ store.count }}</p>
 <p>{{ store.doubleCount }}</p> -->
<!-- <button @click="store.increment()">++</button> -->
</template>

<script setup>
import TodoForm from './components/TodoForm.vue';
import TodoList from './components/TodoList.vue';

import { useCounterStore } from './stores/counter';
const store = useCounterStore()







// import { useCounterStore } from '@/stores/counter';
// const store = useCounterStore() // 중앙저장소 접근가능한 인스턴스변수
// console.log(store.count) // count 가 저장되어있기때문
// const nuwNumber = store.count +1


// //getters

// console.log(store.doubleCount)
// </script>
<style scoped>

=======
  <div>
    <h1>Todo Project</h1>
    <h2>완료된 Todo : {{ store.doneTodoCount }}</h2>
    <TodoList />
    <TodoForm />
  </div>
</template>

<script setup>
import TodoForm from '@/components/TodoForm.vue'
import TodoList from '@/components/TodoList.vue'
import { useCounterStore } from './stores/counter'

const store = useCounterStore()
</script>

<style scoped>
>>>>>>> 0db8f7e851a046df1112dd11b4859c48df8d7aac
</style>
