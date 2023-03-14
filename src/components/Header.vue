<template>
  <div class="header">
    <div class="title">后台管理</div>
    <div class="blank"></div>
    <div class="list">下拉框</div>
  </div>
</template>

<script>
export default {
    name: 'Header'
}
</script>

<style scoped>
.header {
    height: 50px;
    line-height: 50px;
    border-bottom: 1px solid #ccc;
    display: flex;
}
.header .title {
    width: 200px;
}
.header .blank {
    flex: 1;
}
.header .list {
    width: 100px;
}
</style>