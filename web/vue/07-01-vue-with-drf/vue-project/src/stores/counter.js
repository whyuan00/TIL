import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
// drf서버에 ajax요청윟 axios 불러오기(install+)
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {


  const articles = ref([
  ])

  const API_URL = 'http://127.0.0.1:8000'
  const getArticles = function(){
    axios({
      method:'get',
      url: `${API_URL}/api/v1/articles/`,
    })
    .then((response)=> {
      console.log(response)
      console.log(response.data)
      articles.value = response.data
    })
    .catch(error=>{
      console.log(error)
    })
  }

  return {articles,API_URL,getArticles }
}, { persist: true })
