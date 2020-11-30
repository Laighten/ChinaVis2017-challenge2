<template>
    <div id=conRA></div>
</template>

<script>
let echarts = require("echarts");

let option = {
    title:{
       text: '上网人员年龄比例图',
        textStyle: {
            color: '#F3F3F3'
        },
        left:'center'
    },

    tooltip: {
        
        trigger: 'item',
        formatter: "{a} <br/>{b}: {c} ({d}%)"
    },
    legend: {
        top:30,
        orient: 'horizontal',
        x: 'left',
        data:['本市','外来','小于18','18-30岁','30-40岁','40-60岁','大于60']
    },
    series: [
        {   
            center:['53%','65%'],
            name:'人数',
            type:'pie',
            selectedMode: 'single',
            radius: [0, '30%'],

            label: {
                normal: {
                    position: 'inner'
                }
            },
            labelLine: {
                normal: {
                    show: true
                }
            },
            data:[
                {value:1900368, name:'本市'},
                {value:13761761, name:'外来'}
            ]
        },
        {
            center:['53%','65%'],
            name:'人数',
            type:'pie',
            radius: ['40%', '55%'],
            label: {
                normal: {
                    //formatter: '{a|{a}}{abg|}\n{hr|}\n  {b|{b}：}{c}  {per|{d}%}  ',
                    //backgroundColor: '#eee',
                    textStyle: {
                        color: '#F3F3F3'
                    },
                    borderColor: '#aaa',
                    borderWidth: 1,
                    borderRadius: 4,
                    shadowBlur:3,
                    shadowOffsetX: 2,
                    shadowOffsetY: 2,
                    shadowColor: '#999',
                    padding: [0, 7],
                    rich: {
                        a: {
                            color: 'black',
                            lineHeight: 22,
                            align: 'center'
                        },
                        abg: {
                            backgroundColor: 'black',
                            width: '100%',
                            align: 'right',
                            height: 22,
                            borderRadius: [4, 4, 0, 0]
                        },
                        hr: {
                            borderColor: 'black',
                            width: '100%',
                            borderWidth: 0.5,
                            height: 0
                        },
                        b: {
                            fontSize: 16,
                            lineHeight: 33
                        },
                        per: {
                            color: 'black',
                            backgroundColor: 'black',
                            padding: [2, 4],
                            borderRadius: 2
                        }
                    }
                }
            },
            data:[
                {value:903692, name:'小于18'},
                {value:10562535, name:'18-30岁'},
                {value:2835681, name:'30-40岁'},
                {value:1289455, name:'40-60岁'},
                {value:70766, name:'大于60'}
            ]
        }
    ]
};
export default {
    data(){
        return {
            data:null
        }
    },
    mounted(){
        this.myChart = echarts.init(document.getElementById("conRA"));
        this.myChart.setOption(option);

    }
}
</script>

<style>
    #conRA{
        width: 250x;
	    height: 300px
    }
</style>