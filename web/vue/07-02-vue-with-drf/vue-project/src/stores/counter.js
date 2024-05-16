import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const Token = ref(null)
  const isLogin = computed(()=>{

    if (Token.value === null){
      return false 
    } else {
      return true
    }
  })
const router = useRouter()

  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      headers:{
        Authorization: `Token ${Token.value}`
      }
    })
      .then(response => {
        articles.value = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }

  const signUp = function (payload) {
    const {username, password1, password2} = payload 
    console.log(payload)
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data:{
        username,password1,password2
      }
    })
      .then(response => {
        console.log('회원가입 성공')
        const password = password1
        logIn({username, password})
      })
      .catch((error) => {
        console.log(error)
      })
  }

  const logIn= function (payload) {
    const {username, password} = payload 
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data:{
        username,password
      }
    })
      .then(response => {
        console.log('로그인 성공')
        // 응답받은 토큰 저장 
        // console.log(response.data.key)
        Token.value = response.data.key
        // 로그인 후 메인으로 이동
        router.push({name:'ArticleView'})
      })
      .catch(error => {
        console.log(error)
      })
  }



  return { articles, API_URL, getArticles, signUp, logIn, Token, isLogin}
}, { persist: true })
