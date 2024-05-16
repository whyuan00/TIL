<!-- vbase-3-setup -->
<!-- 템플릿태그는 안나옴, 언어블록 template, script, style 순서는 노상관  -->
<!-- vue파일하나당 템플릿과 setup은 하나만 가질수있음 -->
<template>
    <div>
        <p class="greeting" > {{ msg }}  </p>
    </div>
</template>

<script setup>
// 우리가 쓰던 setup함수임
import {ref} from 'Vue' // 주의: 문자열로 작성

const msg = ref('Hello') // return 없어도 템플릿에서 쓸수있음


</script>

<!-- <style lang="scss" scoped> -->
<style scoped>
.greeting {
    color:darkblue;
}

</style>