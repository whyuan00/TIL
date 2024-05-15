<template>
  <div>
  <h1>DetailView</h1>
  <div v-if="article">
  <!-- 비동기상태라서 axios 될떄까지 기다려주지 않음 
  따라서 페이지 렌더링은 article 존재할때만 되도록
  순서 설정해줘야함-->
    <p>작성번호: {{ article.id }}</p>
    <p>제목: {{ article.title }}</p>
    <p>내용: {{ article.content }}</p>
    <p>작성시간: {{ article.created_at }}</p>
    <p>업데이트 시간: {{ article.updated_at }}</p>
  
  </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter';
import { useRoute } from 'vue-router'

const store = useCounterStore()
const route = useRoute()
const article = ref(null)

// 단일 데이터 컴포넌트가 페이지 렌더링과 동시에 세팅되어있어야함

onMounted(()=>{
  axios({
    method:'get',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}`
  })
  .then ((response)=>{
    console.log(response.data)
    article.value = response.data 
  })
  .catch((error)=>{
    console.log(error)
  })
})

</script>

<style>

</style>
