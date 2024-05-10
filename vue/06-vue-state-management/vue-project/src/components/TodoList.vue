<template>
<<<<<<< HEAD
    <div>
        <TodoListItem 
        v-for="todo in store.todos"
        :key="todo.id"
        :todo="todo"
        />
    </div>
</template>

<script setup>

import TodoListItem from '@/components/TodoListItem.vue';
import { useCounterStore } from '@/stores/counter';
=======
  <div>
    <TodoListItem 
      v-for="todo in store.todos"
      :key="todo.id"
      :todo="todo"
    />
  </div>
</template>

<script setup>
import TodoListItem from '@/components/TodoListItem.vue'
import { useCounterStore } from '@/stores/counter'
>>>>>>> 0db8f7e851a046df1112dd11b4859c48df8d7aac

const store = useCounterStore()

</script>

<<<<<<< HEAD
<style  scoped>

</style>
=======
<style scoped>

</style>
>>>>>>> 0db8f7e851a046df1112dd11b4859c48df8d7aac
