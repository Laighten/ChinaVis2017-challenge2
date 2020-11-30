<template>
    <div id=cloumn></div>
</template>

<script>
let echarts = require("echarts");
let option = {
    title: {
			text: '外来上网省份比例图',
			left: '30px',
			textStyle: {
                color: "#F4F3EF",
                fontSize:"18",
				}
		},
    tooltip : {
        
        trigger: 'axis',
        axisPointer : {            // 坐标轴指示器，坐标轴触发有效
            type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
        }
    },
    legend: {
        right:'0px',
        data:['男','女']
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
            data : ['四川省','贵州省','湖北省','湖南省','河南省','江西省','云南省','安徽省','陕西省','江苏省','甘肃省'],
            axisLabel:{
                rotate:45,
                color:'white'
            }
        }
    ],
    yAxis : [
        {
            type : 'value',
            axisLabel:{
                color:'white'
            }
        }
    ],
    series : [
      
        {
            name:'男',
            type:'bar',
            stack: '广告',
            barWidth : 12,
            data:[3995455,953112,548405,385001,361736,246430,322744,229372,211420,189810,184536],
            color:'#335365'
        },
        {
            name:'女',
            type:'bar',
            stack: '广告',
            barWidth : 12,
            data:[883186,123810,55008,37078,34864,15304,45377,15275,19165,13428,15428],
    
        }
    ]
};
export default {
    data(){
        return {
            Mydata:null
        }
    },
    methods:{

    },
    mounted(){
        this.myChart = echarts.init(document.getElementById("cloumn"));
        this.myChart.setOption(option);
    }
}
</script>

<style>
    #cloumn{
        width: 250x;
	    height: 240px
    }
</style>