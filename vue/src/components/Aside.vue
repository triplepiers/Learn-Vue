<template>
  <div id="aside">
    <el-menu
        style="min-height: calc(100vh - 50px);"
        default-active="$route.path"
        router
        class="el-menu-vertical-demo"
    >
      <el-sub-menu index="1">
        <template #title>
          <el-icon><Tools /></el-icon>
          <span>系统管理</span>
        </template>
          <el-menu-item index="user">
            <el-icon><User /></el-icon>
            用户管理
          </el-menu-item>
      </el-sub-menu>
      <el-menu-item index="book">
        <el-icon><icon-menu /></el-icon>
        书籍管理
      </el-menu-item>
      <el-menu-item index="upload">
        <el-icon><UploadFilled /></el-icon>
        文件上传
      </el-menu-item>
    </el-menu>
  </div>
</template>

<script>
import { Tools, User, Menu as IconMenu, UploadFilled } from '@element-plus/icons-vue'

export default {
    name: 'Aside',
    components: {
      Tools,
      User,
      IconMenu,
      UploadFilled
    }
}
</script>

<style scoped>
el-menu {
  width: 200px;
}
</style>