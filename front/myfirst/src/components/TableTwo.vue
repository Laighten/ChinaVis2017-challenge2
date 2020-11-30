<template>
    <div>
        <el-table :data="wangbadetail" height="580" border style="width: 100%" >
        <el-table-column 
        prop="SITEID"
        label="网吧编号"
        width="80"
        >
        </el-table-column>

        <el-table-column 
        prop="XB"
        label="性别"
        width="50"
        >
        </el-table-column>

        <el-table-column 
        prop="CUSTOMERNAME"
        label="姓名"
        width="120"
        >
        </el-table-column>

        <el-table-column 
        prop="ONLINETIME"
        label="上线时间"
        width="80"
        >
        </el-table-column>

        <el-table-column 
        prop="OFFLINETIME"
        label="下线时间"
        width="80"
        >
        </el-table-column>

        <el-table-column 
        prop="AREAID"
        label="地域代码"
        width="80"
        >
        </el-table-column>

         <el-table-column 
        prop="BIRTHDAY"
        label="生日"
        width="60"
        >
        </el-table-column>
        
        <el-table-column 
        prop="timestamp"
        label="连续上网天数"
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
             wangbadetail:[{
              "SITEID":null,
              "XB":null,
              "CUSTOMERNAME":null,
              "ONLINETIME":null,
              "OFFLINETIME":null,
              "AREAID":null,
              "BIRTHDAY":null,
              "timestamp":null

            }]
        }
    },
    methods:{
       getdata(){
           return axios.get("/data/api/Juvdetail").then(result=>{
             this.wangbadetail=result.data
           }).catch(error=>{
               console.log(error)
        })
       },
    //    tableRowClassName({row, rowIndex}) {
    //       if (rowIndex <= 5) {
    //         return 'warning-row1';
    //       } else if (rowIndex>=5 & rowIndex<=10) {
    //         return 'warning-row2';
    //       }else if(rowIndex>=10 & rowIndex<=21){
    //         return 'warning-row3';
    //       }
    //       return '';
    //   }
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