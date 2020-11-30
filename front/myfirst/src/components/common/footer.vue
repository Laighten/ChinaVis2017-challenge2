<template>
    <div class="footer">
        
        <p class="text-center color" >©{{ year }} 赖腾的毕业设计,All rights reserved. </p>
       
    </div>
</template>
<script>
    export default {
        data() {
            return {
                year: undefined
            }
        },
        mounted() {
            this.year = this.getYear();
        },
        methods: {
            getYear() {
                let date = new Date();
                return date.getFullYear();
            }
        }
    }
</script>
<style>
    .text-center {
        margin: 0px 0 0 0
    }
    .color{
        color:#F2F2F2
    }
</style>