<template>
<<<<<<< HEAD
    <div>
        <form @submit.prevent="createTodo(todoText)" ref="formElem">
        <input type="text" v-model="todoText">
        <input type="submit" value="작성">
        </form>
    </div>
</template>

<script setup>
import {ref} from 'vue'
import { useCounterStore} from '@/stores/counter'

const store = useCounterStore()
const todoText = ref('')

// ref 속성으로 input 선택 -
const formElem = ref(null)
// console.log(formElem.value) : 쿼리선택자의 역할 


const createTodo = function(todoText){
    store.addTodo(todoText)
    formElem.value.reset() // input창 리셋됨    
}

</script>

<style  scoped>

</style>
=======
  <div>
    <form @submit.prevent="createTodo(todoText)" ref="formElem">
      <input type="text" v-model="todoText">
      <input type="submit" value="작성">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const todoText = ref('')
const formElem = ref(null)
// console.log(formElem)

const createTodo = function (todoText) {
  store.addTodo(todoText)
  formElem.value.reset()
}
</script>

<style scoped>

</style>
>>>>>>> 0db8f7e851a046df1112dd11b4859c48df8d7aac
