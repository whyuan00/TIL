<template>
    <div>
        <!-- 자식 컴포넌트 전달시 케밥케이스로 표기 -->
        <!-- parentchild로 내려주기 -->
        <Parentchild my-msg="message"
        :dynamic-props="name"

        @some-event="someCallback"

        @my-focus="someCallback2"
        @emit-args="getnumbers"

        @update-name="updateName"

        />
        <!-- parentchild에서 이벤트 수신, -->


        <Parentitem
        v-for="item in items"
        :key="item.id"
        :my-prop="item"
        />

      </div>
</template>

<script setup>
import Parentchild from '@/components/Parentchild.vue';
import Parentitem from '@/components/Parentitem.vue';
import {ref} from 'vue'
const name = ref('Alice')

const items = ref([

    {id:1, name:'사과'},
    {id:2, name:'바나나'},
    {id:3, name:'딸기'},
]
)

const someCallback = function(){
    console.log('parentchild가 만든 정보를 수신했다')
}

const someCallback2 = function() {
    console.log('defineemit정보 수신')
}


const getnumbers = function(...args){
    console.log(args)
}
const updateName = function(){
    name.value='Bella'
}
</script>

<style scoped>

</style>