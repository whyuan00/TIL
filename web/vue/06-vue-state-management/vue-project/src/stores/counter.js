import { ref,computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  
  let id =0;
  const todos = ref([

  ])

  const addTodo = function(todoText){
    todos.value.push({
      id:id++,
      text: todoText,
      isDone: false,
    })
  }
// click=store.deleteTodo(todo.id)
const deleteTodo = function(todoId){
  // console.log('delete')
  // console.log(todoId)
  //todos 배열에서 todo id로 찾기 
  const index = todos.value.findIndex((todo)=> todo.id===todoId)
  // console.log(index)

  //찾은 인덱스 활용하여 todos에서 삭제 후 새로운 todos로 교체
  todos.value.splice(index,1) // js mdn에서 삭제 메서드 검색
}

const updateTodo = function(todoId){
  // console.log('update')
  //전달받은 id로 배열중에 확인, 
  // id 일치하면 isdone 반대로 바꾸고 
  // 새로운 배열 반환
  todos.value = todos.value.map((todo)=>{
    if (todo.id === todoId) {
      todo.isDone = !todo.isDone
    }
    return todo
  } )

}


const doneTodosCount = computed(()=>{
  const doneTodos = todos.value.filter((todo)=> todo.isDone == true)
  return doneTodos.length 
})


  return { todos, addTodo, deleteTodo, updateTodo, doneTodosCount }
},
{persist:true})
//state, getters, actions 
//=> ref, computed, function
