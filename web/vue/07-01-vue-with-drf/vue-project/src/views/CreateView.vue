<template>
  <div>
  <h1>게시글 작성</h1>
  <form @submit.prevent="createArticle" >
  <!-- trim:공백일떄 요청방지 -->
  <input v-model.trim="title" type="text">
  <textarea v-model="content" name="" id="" cols="30" rows="10"></textarea>
  <input type="submit">
  </form>
  </div>
</template>

<script setup>
import {ref} from 'vue'
import { useCounterStore } from '@/stores/counter';
import axios from 'axios'
import { useRouter} from 'vue-router'

const store = useCounterStore()
const router = useRouter()
const title = ref(null)
const content = ref(null)


const createArticle = function(){
  axios({
    method:'POST',
    url:`${store.API_URL}/api/v1/articles/`,
    data:{
      title:title.value,
      content:content.value,

    }
  })
  .then((response)=>{
    console.log(response.data)
    router.push({name:'ArticleView'})
  })
  .catch((error)=>{
    console.log(error)
  })
}
</script>

<style>

</style>
