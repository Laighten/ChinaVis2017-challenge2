<template>
    <div id=conDA></div>
</template>

<script>
import axios from 'axios';
let echarts = require("echarts");

// function getVirtulData(year) {
//             year = year || '2017';
//             var date = +echarts.number.parseDate(year + '-01-01');
//             var end = +echarts.number.parseDate((+year + 1) + '-01-01');
//             var dayTime = 3600 * 24 * 1000;
//             var data = [];
//             for (var time = date; time < end; time += dayTime) {
//                 data.push([
//                     echarts.format.formatTime('yyyy-MM-dd', time),
//                     Math.floor(Math.random() * 10000)
//                 ]);
//             }
//             return data;
// }

var data = [

    ['2016-11-05',255363],
    ['2016-11-19',253536],
    ['2016-11-26',242740],
    ['2016-11-20',242682],
    ['2016-11-13',229502],
    ['2016-11-06',230169],
    ['2016-11-27',226428],
    ['2016-11-12',227575],
    ['2016-11-04',216747],
    ['2016-11-18',217307]
];

let option = {
    //backgroundColor: '#404a59',

    title: {
        top: 0,
        text: '上网记录日历图',
        left: 'center',
        textStyle: {
            color: '#fff'
        }
    },
    tooltip : {
        trigger: 'item'
    },
    legend: {
        top: '30',
        left: '100',
        data:['人数', 'Top 10'],
        textStyle: {
            color: '#fff'
        }
    },
    calendar: [{
        top: 80,
        left: 'center',
        range: ['2016-10-01', '2016-12-31'],
        splitLine: {
            show: true,
            lineStyle: {
                color: '#000',
                width: 4,
                type: 'solid'
            }
        },
        // yearLabel: {
        //     formatter: '{start} 10-12月',
        //     textStyle: {
        //         color: '#fff',
        //     }
        // },
        itemStyle: {
            normal: {
                color: '#323c48',
                borderWidth: 1,
                borderColor: '#111'
            }
        }
    }],
    series : [
        {
            id:'1',
            name: '人数',
            type: 'scatter',
            coordinateSystem: 'calendar',
            symbolSize: function (val) {
                return val[1] / 12000;
            },
            itemStyle: {
                normal: {
                    color: '#ddb926'
                }
            }
        },
        {
            id:'2',
            name: 'Top 10',
            type: 'effectScatter',
            coordinateSystem: 'calendar',
            data: data.sort(function (a, b) {
                return b[1] - a[1];
            }).slice(0, 10),
            symbolSize: function (val) {
                return val[1] / 12000;
            },
            showEffectOn: 'render',
            rippleEffect: {
                brushType: 'stroke'
            },
            hoverAnimation: true,
            itemStyle: {
                normal: {
                    color: '#f4e925',
                    shadowBlur: 10,
                    shadowColor: '#333'
                }
            },
            zlevel: 1
        }
    ]
};
export default {
    data(){
        return {
            AVdata:[]
        }
    },
    methods:{
        getdata(){
            return axios.get("/data/api/AvgDayTime").then(result=>{
                //console.log(result.data)
                this.AVdata = result.data  
            }).catch(error=>{
                console.log(error)
            })
        }
    },
    mounted() {
        this.myChart = echarts.init(document.getElementById("conDA"));
        this.myChart.setOption(option);
       
       
        this.getdata().then(()=>{
            this.myChart.setOption({
                series: [
                    {
                        id:"1",
                        data: this.AVdata
                        
                    }]
            })
        })
        
    }
}
</script>

<style>
    #conDA{
        width: 250x;
	    height: 240px
    }
</style>