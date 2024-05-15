<template>
    <div>
        <p>
            {{ myProp.id }}
            {{ myProp.name }}
        </p>
    </div>
</template>

<script setup>
//내려받기
defineProps({
    myProp: Object
})

</script>

<style  scoped>


</style>