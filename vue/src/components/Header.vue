<template>
  <div class="header">
    <div class="title">后台管理</div>
    <div class="blank"></div>
    <div class="list">
        <el-dropdown>
            <span class="el-dropdown-link">
            张三
            <el-icon class="el-icon--right">
                <arrow-down />
            </el-icon>
            </span>
            <template #dropdown>
            <el-dropdown-menu>
                <el-dropdown-item>个人信息</el-dropdown-item>
                <el-dropdown-item @click="this.$router.push('/login')">退出系统</el-dropdown-item>
            </el-dropdown-menu>
            </template>
        </el-dropdown>
    </div>
  </div>
</template>

<script>
import { ArrowDown } from '@element-plus/icons-vue'

export default {
    name: 'Header',
    components: {
        ArrowDown
    }
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
    padding-left: 30px;
    font-weight: bold;
    color: var(--green);
}
.header .blank {
    flex: 1;
}
.header .list {
    width: 100px;
    display: flex;
    align-items: center;
}
el-dropdown {
    border: none;
}
</style>