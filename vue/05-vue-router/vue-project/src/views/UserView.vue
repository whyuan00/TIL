<template>
    <div>
    <RouterLink :to="{name:'user-profile'}" > profile</RouterLink>
    <RouterLink :to="{name:'user-posts'}"> post </RouterLink>
        <h1>
        UserView
        </h1>
        <!-- props형태로 전달됨 -->
        <h2>
        {{  $route.params.id }}번 user 페이지
        <br>
        {{  userid }}번 user 페이지
        </h2>

        <button @click="gohome">홈으로!</button>
        <button @click="routeupdate">100번유저페이지!</button>
        <hr>
        <RouterView/>
    </div>
</template>

<script setup>
import { useRoute, useRouter, onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router'
import {ref} from 'vue'

// 라우트 객체를 자바스크립트에서 불러오기위해
const route = useRoute()
const userid = ref(route.params.id)


const router = useRouter() 
const gohome = function(){
    // router.push라는 코드로 페이지 이동가능함 
    // router.push({name:'home'}) 히스토리에 추가
    // 현재위치바꾸기임,스택에없어서 뒤로가기 안됨
    router.replace({name:'home'})
    // router.replace({name:'home', params:{username: 'alice'}})
    // router.replace({name:'home', query:{ name: 'bella'}})
// <RouterLink :to="" replace> <>
}

onBeforeRouteLeave((to,from)=>{
    const answer = window.confirm('정말 떠ㅏ\ㅏㄴ?')
    if (answer ===false){
        return false; // false는 네비게이션 취소
    }
    return //생략되면 자동르로 to 
})

const routeupdate = function(){
    router.push({ name:'user', params: {id: 100}})
}


onBeforeRouteUpdate((to,from)=> {
    userid.value = to.params.id
})

</script>

<style  scoped>

</style>