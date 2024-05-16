<template>
  <div>
  <h1>Article Page</h1>
  <RouterLink :to="{name:'CreateView'}">
  [CREATE]
  </RouterLink>
  <ArticleList/>
  </div>
</template>

<script setup>
import {onMounted} from 'vue'
import { useCounterStore } from '@/stores/counter';
import { RouterLink} from 'vue-router'
import ArticleList from '@/components/ArticleList.vue';

const store = useCounterStore()

onMounted(() =>{
  // 마운트 즉시 url로 리스트 불러오기 
  store.getArticles()
})

</script>

<style>

</style>
