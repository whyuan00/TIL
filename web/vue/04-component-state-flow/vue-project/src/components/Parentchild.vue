<template>
    <div>
    <p>
        {{ myMsg }}
    </p>
    <p>
        {{ dynamicProps }}
    </p>
    <Parentgrandchild 
    :my-msg="myMsg"
    @update-name="updateName"

     />
<!-- :num=""은 동적 프롭스, num=""은 정적프롭스 -->

    <!-- 소리 보냄 -->
    <button @click="$emit('someEvent')" > 버튼 </button>
    <button @click="buttonclick">버튼2</button>
    <button @click="emitArgs">추가인자전달</button>
    
    </div>
</template>

<script setup>
import Parentgrandchild from '@/components/Parentgrandchild.vue';


//내려받은 props 선언해줘야 쓸수있음 
//1, 배열 상태로 선언
//js문법: 하이픈기준 대문자로 변경 (카멜케이스)

// defineProps(['myMsg'])

//2, 객체상태로 선언(권장)  -> 객체 선언문법은 유효성검사로 활용가능하기때문에 권장 
// defineProps({
//     myMsg: String
// })

const props = defineProps({
    myMsg: String,
    dynamicProps: String
})
console.log(props) // {myMsg: message}
console.log(props.myMsg) // message 


// 자바스크립트에서 호출, emit 정의안해도 작동은 함
const emit = defineEmits(['myFocus', 'emitArgs', 'updateName'])
const buttonclick = function() {
    emit('myFocus')
}

const emitArgs = function(){
    emit('emitArgs', 1,2,3)
}

const updateName = function(){
    emit('updateName')
}
</script>

<style  scoped>

</style>