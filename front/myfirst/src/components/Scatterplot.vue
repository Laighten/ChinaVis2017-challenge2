<template>
    <div id=conSP></div>
</template>

<script>
import axios from 'axios';
let echarts = require("echarts");

var itemStyle = {
    normal: {
        opacity: 0.8,
        shadowBlur: 10,
        shadowOffsetX: 0,
        shadowOffsetY: 0,
        shadowColor: 'rgba(0, 0, 0, 0.5)'
    }
};
//var countries = ['奥地利', '比利时', '加拿大'];

var years = ['12','16','20','24','28','32','36','40','44','48','52','56','60'];

var sizeFunction = function (x) {
    var y = Math.sqrt(x / 5e8) + 0.1;
    return y * 100;
};
// Schema:
var schema = [
    {name: 'Age', index: 0, text: '年龄', unit: '岁'},
    {name: 'Num', index: 1, text: '该年龄的上网人数', unit: '个'},
    {name: 'Time', index: 2, text: '平均上网时长', unit: '分钟'}
];

    
let option = {
    baseOption: {
        timeline: {
            axisType: 'category',
            orient: 'vertical',
            autoPlay: true,
            inverse: true,
            playInterval: 1000,
            left: null,
            right: 0,
            top: 10,
            bottom: 10,
            width: 35,
            height: null,
            label: {
                normal: {
                    textStyle: {
                        color: '#F4F3EF'
                    }
                },
                emphasis: {
                    textStyle: {
                        color: '#F4F3EF'
                    }
                }
            },

            symbol: 'none',
            lineStyle: {
                color: '#F4F3EF'
            },
            checkpointStyle: {
                color: '#F4F3EF',
                borderColor: '#777',
                borderWidth: 2
            },
            controlStyle: {
                showNextBtn: false,
                showPrevBtn: false,
                normal: {
                    color: '#666',
                    borderColor: '#666'
                },
                emphasis: {
                    color: '#F4F3EF',
                    borderColor: '#aaa'
                }
            },
            data:years
        },
        //backgroundColor: '#404a59',
        title: [{
            text: '',
            textAlign: 'center',
            left: '63%',
            top: '55%',
            textStyle: {
                fontSize: 50,
                color: 'rgba(255, 255, 255, 0.7)'
            }
        }, {
            text: '上网时间与年龄关系的演变',
            left: 'center',
            top: 5,
            textStyle: {
                color: '#F3F3F3',
                fontWeight: 'normal',
                fontSize: 18
            }
        }],
        tooltip: {
            padding: 5,
            backgroundColor: '#222',
            borderColor: '#777',
            borderWidth: 1,
            formatter: function (obj) {
                    var value = obj.value;
                    return  schema[0].text + '：' + value[2] + schema[0].unit + '<br>'
                            + schema[1].text + '：' + value[1] + schema[1].unit + '<br>'
                            + schema[2].text + '：' + value[0] + schema[2].unit+'<br>';
                }
            
        },
        grid: {
            top: 40,
            containLabel: true,
            left: 10,
            right: '60'
        },
        xAxis: {
            type: 'value',
            name: '上网时长',
            max: 280,
            min: 180,

            nameGap: 30,
            nameLocation: 'middle',
            nameTextStyle: {
                fontSize: 13,
                color: '#F3F3F3',
            },
            splitLine: {
                show: false,
               
            },
            axisLine: {
                lineStyle: {
                    color:"#F4F3EF"
                }
            },
            axisLabel: {
               
                formatter: '{value}分钟',
                textStyle: {
                color: "#F4F3EF",
                fontStyle: "normal"
              }
            }
        },
        yAxis: {
            type: 'value',
            name: '上网人数',
            max: 160000,
            nameTextStyle: {
                color: '#F3F3F3',
                fontSize: 13
            },
            axisLine: {
                lineStyle: {
                    color: "#F3F3F3"
                }
            },
            splitLine: {
                show: false
            },
            axisLabel: {
                /* formatter: '{value}人' */
            }
        },
        visualMap: [
            {
                show: false,
                dimension: 3,
                //categories:countries,
                calculable: true,
                precision: 0.1,
                textGap: 30,
                textStyle: {
                    color: 'black'
                },
                inRange: {
                    color: (function () {
                        var colors = ['#16E9E9'];
                        return colors.concat(colors);
                    })()
                }
            }
        ],
        series: [
            {
                id:"dat",
                type: 'scatter',
                itemStyle: itemStyle,
                symbolSize: function(val) {
                        return sizeFunction(val[2]);
                    }
            }
        ],
        //animationDurationUpdate: 10,
        animationEasingUpdate: 'quinticInOut'
    }
    
};


export default {
    data(){
      return {
        SPdata:null
      }
    },
    methods:{
       getdata(){
          return axios.get("data/api/AgeTimeNum").then(result=>{  
              this.SPdata = result.data 
            
          }).catch(error=>{
              console.log(error)
          })
       }

    },
    mounted() {
        this.myChart = echarts.init(document.getElementById("conSP"));
        this.myChart.setOption(option);
        this.getdata().then(()=>{

            let options = []
            this.SPdata.forEach((item, index) => {
                console.log(item[2]),
                options.push({
                    title: {
                        text: years[index]
                    },
                    series: {
                        name: years[index],
                        type: 'scatter',
                        data: [item],
                        symbolSize: 20
                    }
                })
            })
            this.myChart.setOption({
                options     
            })

        });
     
    }
    
}
</script>

<style>
   #conSP{
     width: 680px;
     height: 280px;
   } 
</style>