<template>
<!-- https://www.wangeditor.com/ -->
  <div id="rich-text">
    <div class="search" style="margin-bottom:10px;">
        <el-button type="primary" @click="showAdd" style="margin-right:5px;">新增</el-button>
      <el-input v-model="search" placeholder="请输入内容" style="width:20%;" clearable></el-input>
      <el-button type="primary" style="margin-left:5px;" @click="loadData">查询</el-button>
    </div>
    <el-table :data="tableData" stripe style="width: 100%;">
      <el-table-column prop="id" label="ID" sortable/>
      <el-table-column prop="title" label="标题" />
      <el-table-column prop="author" label="作者" />
      <el-table-column prop="create_time" label="创建时间" sortable/>
      <el-table-column fixed="right" label="操作" width="120">
      <template #default="scope">
        <el-button link type="primary" size="small" @click="handleEdit(scope.row)">编辑</el-button>
        <el-popconfirm title="确认要删除吗?" @confirm="handleDelete(scope.row.id)">
          <template #reference>
            <el-button link type="primary" size="small">删除</el-button>
          </template>
        </el-popconfirm>
      </template>
    </el-table-column>
    </el-table>
    <div class="pages">
      <el-pagination
        v-model:current-page="currentPage"
        v-model:page-size="psize"
        :page-sizes="[5, 10, 20]"
        :page-size="5"
        :small="small"
        :disabled="disabled"
        :background="background"
        layout="total, sizes, prev, pager, next, jumper"
        :total="total"
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
      />
    </div>
    <!-- 新增用户弹窗 -->
    <el-dialog
      v-model="dialogVisible"
      title="新增用户"
      width="500px"
      :before-close="handleClose"
    >
      <el-form v-model="form" label-width="120px" >
        <el-form-item label="书名" required>
          <el-input v-model="form.name" style="width:80%"/>
        </el-form-item>
        <el-form-item label="价格">
          <el-input-number v-model="form.price" :precision="2" :step="0.01" :max="1000" />
        </el-form-item>
        <el-form-item label="作者">
          <el-input v-model="form.author" style="width:80%"/>
        </el-form-item>
        <el-form-item label="创建时间">
          <el-date-picker v-model="form.create_time" style="width:80%"
           value-format="YYYY-MM-DD"
          >
          </el-date-picker>
        </el-form-item>
        <el-form-item label="封面">
          <el-upload
            action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
            :on-preview="handlePreview"
            :on-remove="handleRemove"
            :before-remove="beforeRemove"
            :limit="1"
            :on-exceed="handleExceed"
            :http-request="handleUpload"
            ref="myUpload"
          >
            <el-button type="primary" style="width:100%;">点击上传</el-button>
          </el-upload>
        </el-form-item>
      </el-form>
        
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="dialogVisible = false">取消</el-button>
          <el-button type="primary" @click="save">
            确认
          </el-button>
        </span>
      </template>
    </el-dialog>
    <!-- <div id="editor"></div> -->
  </div>
</template>

<script>
import E from 'wangeditor'

export default {
    name: 'RichTextView',
    data() {
        return {
        search: "",
        psize: 5,
        currentPage: 1,
        tableData: [],
        total: 0,
        dialogVisible: false,
        form: {}
        }
    },
    mounted() {
        // const editor = new E('#editor')
        // editor.create()
    }
}
</script>

<style scoped>
#rich-text {
    flex: 1;
    padding: 10px;
}
#editor {
    width: 100%;
    box-shadow: 0 0 15px rgba(0,0,0,.3);
    border-radius: 10px;
    overflow: hidden;
}
</style>