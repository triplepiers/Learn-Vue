<template>
  <div id="aside">
    <el-menu
        style="min-height: calc(100vh - 50px);"
        default-active="2"
        class="el-menu-vertical-demo"
    >
      <el-sub-menu index="1">
        <template #title>
          <el-icon><location /></el-icon>
          <span>Navigator One</span>
        </template>
          <el-menu-item index="1-1">item one</el-menu-item>
          <el-menu-item index="1-2">item two</el-menu-item>
          <el-menu-item index="1-3">item three</el-menu-item>
          <el-menu-item index="1-4">item four</el-menu-item>
      </el-sub-menu>
    </el-menu>
  </div>
</template>

<script>

export default {
    name: 'Aside'
}
</script>

<style scoped>
el-menu {
  width: 200px;
}
</style>