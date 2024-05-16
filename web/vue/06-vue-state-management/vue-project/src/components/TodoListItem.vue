<template>
<<<<<<< HEAD
    <div>
        <span
        
        :class="{'is-done': todo.isDone}"
        
         @click="store.updateTodo(todo.id)" >{{ todo.text }}</span>
        <button @click="store.deleteTodo(todo.id)">삭제</button>
    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';

defineProps({
    todo: Object
})

const store = useCounterStore()


</script>

<style  scoped>

.is-done {
    text-decoration: line-through;
}
</style>
=======
  <div>
    <span 
      @click="store.updateTodo(todo.id)"
      :class="{ 'is-done': todo.isDone }"
    >
      {{ todo.text }}
    </span>
    <button @click="store.deleteTodo(todo.id)">삭제</button>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

defineProps({
  todo: Object
})

</script>

<style scoped>
.is-done {
  text-decoration: line-through;
}
</style>
>>>>>>> 0db8f7e851a046df1112dd11b4859c48df8d7aac
