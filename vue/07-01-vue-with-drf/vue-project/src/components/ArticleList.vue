<template>
  <div>
    <h3>Article List</h3>
    <ArticleListItem 
    v-for="article in store.articles"
    :key="article.id"
    :article="article"
    />
      
  </div>
</template>

<script setup>

import { useCounterStore } from '@/stores/counter';
const store = useCounterStore()

import ArticleListItem from '@/components/ArticleListItem.vue'
</script>
