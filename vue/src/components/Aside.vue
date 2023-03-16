<template>
  <div id="aside">
    <el-menu
        style="min-height: calc(100vh - 50px);"
        default-active="user"
        class="el-menu-vertical-demo"
        default-openeds="1"
    >
      <el-sub-menu index="1">
        <template #title>
          <el-icon><setting /></el-icon>
          <span>系统管理</span>
        </template>
          <el-menu-item index="user">用户管理</el-menu-item>
      </el-sub-menu>
      <el-menu-item index="data">
        <el-icon><icon-menu /></el-icon>
        数据管理
      </el-menu-item>
    </el-menu>
  </div>
</template>

<script>
import { Setting, Menu as IconMenu } from '@element-plus/icons-vue'

export default {
    name: 'Aside',
    components: {
      Setting,
      IconMenu
    }
}
</script>

<style scoped>
el-menu {
  width: 200px;
}
</style>