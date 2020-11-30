<template>
  <div id=conP></div>
</template>

<script>
import axios from 'axios';
let echarts = require("echarts");

let option = {
    title: {
        text: '上网高峰时段分析折线图',
        left:"center",
        textStyle: {
                color: "#F3F3F3"
              }
    },
    tooltip : {
        trigger: 'axis',
        axisPointer: {
            type: 'cross',
            label: {
                backgroundColor: '#6a7985'
            }
        }
    },
    legend: {
        data:['上网人数'],
        right:'5%',
        textStyle: {
                color: "#D53A35"
              }
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis : [
        {
            type : 'category',
            boundaryGap : false,
            data: [
               "0","1","2","3","4","5","6","7","8","9","10","11","12",
               "13","14","15","16","17","18","19","20","21","22","23" ],
            axisLabel: {
              textStyle: {
                color: "#F4F3EF",
                fontSize: "10",
                fontStyle: "normal"
              }
            }
        }
    ],
    yAxis : [
        {
            type : 'value',
            axisLabel: {
              textStyle: {
                color: "#F4F3EF",
                fontSize: "10",
                fontStyle: "normal"
              }
            }
        }
    ],
    series : [
        {
            id:'1',
            name:'上网人数',
            type:'line',
            stack: '总量',
            areaStyle: {
                color:'#D53A35'//更改折线背景的颜色
            },
            itemStyle : {  
                normal : {  
                    color:"#D53A35", //更改折线点的颜色
                    lineStyle:{  
                        color:'#D53A35'  //更改折线的颜色
                    }  
                }  
            },  
            // data:[120, 132, 101, 134, 90, 230, 210,234,343,231,344,341,123,123,344,34,454,343,123,333,231,234,123,123],
            
        }
       
    ]
};

export default {
    data(){
      return {
        Pdata:[]
      }
    },
    methods:{
       getdata(){
          return axios.get("data/api/AvgTime").then(result=>{
             
              this.Pdata = result.data 
          }).catch(error=>{
              console.log(error)
          })
       }

    },
    mounted() {
        this.myChart = echarts.init(document.getElementById("conP"));
        this.myChart.setOption(option);
        this.getdata().then(()=>{
             this.myChart.setOption({
				series: [
				{
				    id:"1",
					data: this.Pdata
				}]
			})
        })
    }
}
</script>

<style>
  #conP{
     width: 680px;
     height: 260px;
  }
</style>