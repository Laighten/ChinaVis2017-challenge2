<template>
<div v-show="peakData.length" class="aabb">
      <i class="fa fa-times" id="close-button" style="color: black; font-size: 1.5em; cursor: pointer" aria-hidden="true" @click="closeButton"></i>
      <div  id="conZ"></div>
</div>
</template>

<script>
let echarts = require("echarts");

let option = {
  title: {
    text: "上网人数接纳图",
    left: "5%"
  },
  tooltip: {
    trigger: "axis",
    axisPointer: {
      type: "cross",
      label: {
        backgroundColor: "#6a7985"
      }
    }
  },
  legend: {
    data: ["未成人上网人数","成年人上网人数"],
    right: "4%"
  },
  // toolbox: {
  //     feature: {
  //         saveAsImage: {}
  //     }
  // },
  grid: {
    left: "3%",
    right: "4%",
    bottom: "3%",
    containLabel: true
  },
  xAxis: [
    {
      type: "category",
      boundaryGap: false,
      data: [
        "0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23"
      ],
      axisLabel: {
        textStyle: {
          color: "black",
          fontSize: "10",
          fontStyle: "normal"
        }
      }
    }
  ],
  yAxis: [
    {
      type: "value"
    }
  ],
  series: [
    {
      id: "Below18",
      name: "未成人上网人数",
      type: "line",
      stack: "总量",
      areaStyle: {},
      label: {
        normal: {
          show: false,
          position: "top"
        }
      }
     
    },
    {
      id: "Above18",
      name: "成年人上网人数",
      type: "line",
      stack: "总量",
      areaStyle: {},
      label: {
        normal: {
          show: false,
          position: "top"
        }
      }
    }
  ]
};
export default {
  data() {
    return {
      peakData: []
    };
  },
  mounted() {
    this.myChart = echarts.init(document.getElementById("conZ"));
    this.myChart.setOption(option);

    this.$root.Bus.$on("peakData", params => {
      //console.log(this.peakData)
      this.peakData = params;
    });
  },
  methods:{
    closeButton() {
      console.log('close')
      this.peakData = []
      this.$root.Bus.$emit('lightOFF', false)
    }
  },
  watch: {
    peakData(newValue) {
      this.myChart.setOption({
        series: [
          {
            id: "Below18",
            data: newValue[0][0]
          },
          {
            id: "Above18",
            data: newValue[0][1]
          }
        ]
      });
    }
  }
};
</script>


<style>
.aabb {
  background-color: rgba(255,255,255,0.7);
  position: absolute;
  padding: 0;
  margin: 0;
  width: 450px;
  height: 280px;
  top:30%;
  left: 46%;
  margin-top: 20px;
  margin-left: -260px;
  z-index: 1001
}
#conZ {
  width: 450px;
  height: 280px;
}
#close-button {
  position: absolute;
  left: 5px;
  top: 5px;
  z-index: 1000
}
</style>