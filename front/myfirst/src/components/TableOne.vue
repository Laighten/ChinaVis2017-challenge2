<template>
   <div>
    <el-table :data="wangba" height="580" border style="width: 100%" >
    <el-table-column 
      prop="SITEID"
      label="网吧编号"
      width="140"
      >
    </el-table-column>

    <el-table-column 
      prop="TITLE"
      label="网吧名称"
      width="120"
      >
    </el-table-column>
    
    <el-table-column 
      prop="Juv_count"
      label="违法次数"
      width="100"
      >
    </el-table-column>
    </el-table>
    
   </div>
</template>

<script>
import axios from 'axios';

export default {
    data(){
        return {
            wangba:[{
              "SITEID":null,
              "TITLE":null,
              "Juv_count":null
            }]
        }
    },
    methods:{
       getdata(){
           return axios.get("/data/api/JuvCount").then(result=>{
             this.wangba=result.data
           }).catch(error=>{
               console.log(error)
        })
       },
      //  tableRowClassName({row, rowIndex}) {
      //     if (rowIndex <= 5) {
      //       return 'warning-row1';
      //     } else if (rowIndex>=5 & rowIndex<=10) {
      //       return 'warning-row2';
      //     }else if(rowIndex>=10 & rowIndex<=21){
      //       return 'warning-row3';
      //     }
      //     return '';
      // }
    },
    beforeMount(){
        this.getdata();
        // this.tableRowClassName();
    }
}
</script>

<style>
    .el-table .warning-row1 {
    background: #01E6FB;
  }

  .el-table .warning-row2 {
    background: #f0cd06;
  }
  .el-table .warning-row3 {
    background: #60db0e;
  }

</style>