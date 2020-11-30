<template>
  <div>
   <div class="wrap">
  
    <h3 class="page-title">
      Signature
      <small>Dimension analysis</small>
    </h3>
    
     <!-- <div class="row">  -->
    
     <div class="col-lg-8 map">
         <section class="widget" style="height: 100%">
            <div style="position: relative; padding: 0;height:100%">
              <echarts :option="scatterOption" ref="map"/>
              <echarts :option="refChart" ref="refChart" class="ref-chart"/> 
            </div>
          </section>
     </div>

     <div class="col-lg-4">
        <section class="widget">
         
              <div class="form-inline btn-group-sm">
                <label for="sample-precision" class="form-check-input">采样精度</label>
                  <select v-model="measureAccuracy" style="color:black" class="custom-select form-check-input custom-select-sm" id="sample-precision">
                  <option disabled value style="color:black">请选择</option>
                  <option value="20" style="color:black">粗略</option>
                  <option value="10" style="color:black">中等</option>
                  <option value="5" style="color:black">精确</option>
                </select>
                <button class="btn btn-primary" @click="referenceLine">绘线</button>
                <button class="btn btn-primary" @click="resetChart">重置</button>
                <button class="btn btn-primary" @click="startSample">采样</button>
                <button class="btn btn-primary" @click="samplePositions">采样位置</button>
                
                <label for="sort" class="form-check-input">排序基准</label>
                <select v-model="baseDataIndex" style="color:black" class="custom-select form-check-input custom-select-sm" id="sort">
                  <option disabled value style="color:black">请选择</option>
                  <option style="color:black" v-for="(item, index) in dataTitle" :value="index" :key="index">{{ item }}</option>
                </select>
                <button class="btn btn-primary" @click="dataNormalization">排序</button>
                <!-- <button class="btn btn-primary" @click="constantBaseLine">基线</button> -->
              </div>
        </section>
        <section class="widget" style="height:485px">
                <div  style="height:100%">
                  <div class="row" style="height:100%" id="multiple-chart">
                    <div v-for="i in 9" :key="i" :id="i-1" class="col-md-4 line">
                      <echarts :option="smallMult" :ref="'chart'+i"/>
                       </div>
                  </div>
                </div>
        </section>
      
    </div>
       
   
   <!-- </div> -->
  </div> 
 </div>
</template>
<script>

import echarts from "../components/echarts";
import axios from "axios";
import _ from "lodash";

let scatterOption = {
  title: {
    text: "重庆市网吧分布",
    left: "center"
  },
  tooltip: {
    trigger: "item",
    show: false
  },
  toolbox: {
    show: false,
    feature: {
      dataView: {
        show: true
      }
    }
  },
  animation: false,
  bmap: {
    center: [107.557862, 30.068242],
    zoom: 8,
    roam: false,
    mapStyle: {
      styleJson: [
        {
          featureType: "water",
          elementType: "all",
          stylers: {
            color: "#d1d1d1"
          }
        },
        {
          featureType: "land",
          elementType: "all",
          stylers: {
            color: "#f3f3f3"
          }
        },
        {
          featureType: "railway",
          elementType: "all",
          stylers: {
            visibility: "off"
          }
        },
        {
          featureType: "highway",
          elementType: "all",
          stylers: {
            color: "#fdfdfd"
          }
        },
        {
          featureType: "highway",
          elementType: "labels",
          stylers: {
            visibility: "off"
          }
        },
        {
          featureType: "arterial",
          elementType: "geometry",
          stylers: {
            color: "#fefefe"
          }
        },
        {
          featureType: "arterial",
          elementType: "geometry.fill",
          stylers: {
            color: "#fefefe"
          }
        },
        {
          featureType: "poi",
          elementType: "all",
          stylers: {
            visibility: "off"
          }
        },
        {
          featureType: "green",
          elementType: "all",
          stylers: {
            visibility: "off"
          }
        },
        {
          featureType: "subway",
          elementType: "all",
          stylers: {
            visibility: "off"
          }
        },
        {
          featureType: "manmade",
          elementType: "all",
          stylers: {
            color: "#d1d1d1"
          }
        },
        {
          featureType: "local",
          elementType: "all",
          stylers: {
            color: "#d1d1d1"
          }
        },
        {
          featureType: "arterial",
          elementType: "labels",
          stylers: {
            visibility: "off"
          }
        },
        {
          featureType: "boundary",
          elementType: "all",
          stylers: {
            color: "#fefefe"
          }
        },
        {
          featureType: "building",
          elementType: "all",
          stylers: {
            color: "#d1d1d1"
          }
        },
        {
          featureType: "label",
          elementType: "labels.text.fill",
          stylers: {
            color: "#999999"
          }
        }
      ]
    }
  },
  brush: {
    toolbox: ["clear"],
    brushMode: "single",
    outOfBrush: {
      color: "purple",
      colorAlpha: 1
    },
    brushStyle: {
      borderWidth: 0,
      color: "rgba(120,140,180,0)"
    },
    throttleDelay: 0,
    transformable: false
  },
  series: [
    {
      id: "data1",
      name: "netbar",
      type: "scatter",
      coordinateSystem: "bmap",
      data: [],
      symbolSize: 5,
      tooltip: {
        formatter: params => {
          let str = "上机人数: ";
          str += params.value[2];
          return str;
        }
      },
      label: {
        normal: {
          formatter: "{b}",
          position: "right",
          show: false
        },
        emphasis: {
          show: true
        }
      },
      itemStyle: {
        normal: {
          color: "purple"
        }
      }
    },
    {
      id: "data2",
      name: "netbar",
      type: "scatter",
      coordinateSystem: "bmap",
      data: [],
      symbolSize: 5,
      tooltip: {
        formatter: params => {
          let str = "上机人数: ";
          str += params.value[2];
          return str;
        }
      },
      label: {
        normal: {
          formatter: "{b}",
          position: "right",
          show: false
        },
        emphasis: {
          show: true
        }
      },
      itemStyle: {
        normal: {
          color: "purple"
        }
      }
    }
  ]
};

let refChart = {
  graphic: [
    {
      id: "handle",
      type: "rect",
      $action: "replace",
      draggable: true,
      z: 1000,
      position: [0, 0],
      shape: {
        width: 50,
        height: 50
      },
      style: {
        fill: "rgba(255,0,0,0.3)"
      },
      cursor: "move"
    },
    {
      id: "referenceLine",
      type: "polyline",
      shape: {},
      style: {
        stroke: "#000",
        lineWidth: 2
      },
      cursor: "default"
    },
    {
      id: "rect",
      type: "rect",
      $action: "merge",
      z: 900,
      style: {
        fill: "rgba(0,0,255,0.3)"
      },
      position: [-50, -50],
      shape: {
        width: 50,
        height: 50
      },
      cursor: "default"
    }
  ]
};

let smallMult = {
  title: {
    left: "left",
    textStyle: {
      fontWeight: "normal",
      fontSize: 12
    }
  },
  tooltip: { show: false },
  toolbox: {
    feature: {
      magicType: {
        type: ["line", "bar"]
      }
    }
  },
  xAxis: {
    type: "category"
  },
  yAxis: {},
  grid: {
    left: 5,
    right: 5,
    top: 25,
    bottom: 2,
    containLabel: true
  },
  series: {
    type: "line",
    id: "linechart"
  }
};

//所有数据项名称
const dataTitle = [
  "Under_age",
  "UnnormalAge",
  "OvertimeOnNet",
  "ExternalPeople",
  "MidnightOnNet",
  "Online17_18",
  "age18_44",
  "age45_52",
  "age53_68"
];

window.dataTitle = dataTitle;

export default {
  name: "dataSet1",
  components: {
    echarts
  },
  data() {
    return {
      measureAccuracy: 20, //选择刷采样的精度
      scatterOption, //地图配置项
      refChart, //参考线配置项
      netbar1: [], //原始数据
      netbar2: [],
      mapComponent: {}, //地图组件实例
      selectedNetbar: [], //被选中的所有网吧集
      selectedData: [], //所有被选中网吧数据集（ajax从后端请求）
      selectedPosition: [], //刷选位置的坐标集
      //beforeSelected: [], //上一次被选中的数据
      //currentSelected: [], //当前被选择刷选中的数据
      smallMult,
      allData: [], //处理后的数据集（本系统对每一个采样求平均值）
      refLinePoints: [], //参考线
      dataTitle, //所有数据项名称
      baseDataIndex: 0 //排序基准数据项的索引
    };
  },
  created() {
    const _this = this;
    this.getScatterData().then(() => {
      _this.scatterOption.series[0].data = _this.netbar1;
      _this.scatterOption.series[1].data = _this.netbar2;
    });
    //
  },
  mounted() {
    this.mapComponent = this.$refs.map; //map组件
    const _this = this;
    let bmap = this.mapComponent.chart
      .getModel()
      .getComponent("bmap")
      .getBMap();
    //console.log(bmap)

    this.mapComponent.chart.setOption({
      series: {
        data: _this.netbar
      }
    });
    window.refSmallChart = []; //所有邮贴图的vue实例
    for (let item in this.$refs) {
      if (item.search(/chart{1}[1-9]+/) != -1) {
        window.refSmallChart.push({
          ref: item,
          instance: this.$refs[item][0]
        });
      }
    }
    //console.log(window.refSmallChart)

    window.refChart = this.$refs.refChart.chart; //参考线图表的echarts实例
    window.refLine = []; //参考线的point
    //console.log(window.mapChart);

    this.getBrushData();
    this.smallChartClick();
  },
  methods: {
    //ajax请求原始数据
    getScatterData: function() {
      const _this = this;
      return new Promise(function(resolve, reject) {
        axios
          .get("/data/api/ApiAll")
          .then(response => {
            let data = response.data;
            data = data.map(obj => {
              let arr = _.values(obj);
              let siteid = arr.shift();
              arr.push(siteid);
              return arr;
            });
            //单个series的data的临界值是2999，超过后渲染会卡顿，因此设置每2000个点为一个series
            _this.netbar1 = data.splice(0, 2000);
            _this.netbar2 = data;
            resolve();
          })
          .catch(error => {
            reject(error);
          });
      });
    },
    //选择刷刷选数据处理
    getBrushData: function() {
      const _this = this;
      this.mapComponent.chart.on("brushselected", params => {
        if (
          params.batch[0].selected[0].dataIndex.toString() === "" &&
          params.batch[0].selected[1].dataIndex.toString() === ""
        ) {
          //console.log('brush')
          return;
        }
        let position = params.batch[0].areas[0].range;
        _this.selectedPosition.push([position[0][0] + 25, position[1][0] + 25]);
        // console.log(_this.selectedPosition);

        let dataIndex1 = params.batch[0].selected[0].dataIndex;
        let dataIndex2 = params.batch[0].selected[1].dataIndex;
        let netbarId = [];
        //此处可能导致刷选速度慢
        _this.netbar1.forEach((curVal, index) => {
          dataIndex1.forEach(item => {
            if (item === index) netbarId.push(curVal[2]);
          });
        });
        _this.netbar2.forEach((curVal, index) => {
          dataIndex2.forEach(item => {
            if (item === index) netbarId.push(curVal[2]);
          });
        });
        _this.selectedNetbar.push(netbarId);
        //console.log(_this.selectedNetbar)
      });
    },
    //邮贴图click事件显示单个数据采样位置(已改为监听mouseover)
    smallChartClick: function() {
      const _this = this;
      window.refSmallChart.forEach(item => {
        item.instance.chart.on("mouseover", params => {
          let dataIndex = params.dataIndex;
          window.refChart.setOption({
            graphic: {
              id: "rect",
              position: [
                _this.selectedPosition[dataIndex][0] - 25,
                _this.selectedPosition[dataIndex][1] - 25
              ]
            }
          });
        });
      });
    },
    //所有数据采样的位置
    samplePositions: function() {
      const _this = this;
      this.selectedPosition.forEach((item, index) => {
        window.refChart.setOption({
          graphic: {
            id: "rects" + index,
            position: [item[0] - 25, item[1] - 25],
            type: "rect",
            z: 800,
            style: {
              fill: "rgba(0,255,0,0.3)"
            },
            shape: {
              width: 50,
              height: 50
            },
            cursor: "default"
          }
        });
      });
    },
    //邮贴图click事件处理（事件改为mouseover）
    smallChartClick: function() {
      const _this = this;
      window.refSmallChart.forEach(item => {
        item.instance.chart.on("mouseover", params => {
          let dataIndex = params.dataIndex;
          window.refChart.setOption({
            graphic: {
              id: "rect",
              position: [
                _this.selectedPosition[dataIndex][0] - 25,
                _this.selectedPosition[dataIndex][1] - 25
              ]
            }
          });
          //console.log(params)
        });
      });
    },
    //初始化选择刷
    initBrush: function(x, y) {
      this.mapComponent.chart.dispatchAction({
        type: "brush",
        areas: [
          {
            brushType: "rect",
            range: [[x - 25, x + 25], [y - 25, y + 25]]
          }
        ]
      });
    },
   
    //监听参考线把手的拖拽事件和绘制参考线
    referenceLine: function() {
      const _this = this;
      window.refChart.setOption({
        graphic: {
          id: "handle",
          ondrag: function() {
            const _position = this.position;
            _this.refLinePoints.push([_position[0] + 25, _position[1] + 25]);
          }
        }
      });
    },
    //取消把手绘制参考线
    deleteRefline: function() {
      window.refChart.setOption({
        graphic: {
          id: "handle",
          ondrag: null
        }
      });
    },
    //重置所有
    resetChart: function() {
      this.selectedData = [];
      this.refLinePoints = [];
      this.initChart();
      this.deleteRefline();
      this.selectedNetbar = [];
      this.allData = [];

      this.selectedPosition.forEach((item, index) => {
        window.refChart.setOption({
          graphic: {
            id: "rects" + index,
            $action: "remove"
          }
        });
      });
      this.selectedPosition = [];

      window.refChart.setOption({
        graphic: {
          id: "rect",
          position: [-50, -50]
        }
      });

      this.resetDOMNode();
    },
    //栅格图DOM节点复原
    resetDOMNode: function() {
      let parent = document.getElementById("multiple-chart");
      let children = parent.children;
      let temp = [];
      for (let i in children) {
        if (children[i].nodeType == 1) {
          temp[i] = children[i];
        }
      }
      temp.sort((a, b) => {
        return a.id > b.id ? 1 : -1;
      });
      temp.forEach(item => {
        parent.appendChild(item);
      });
    },
    //绘制邮贴图
    drawChart: function() {
      const _this = this;
      let average = [];
      //选中为空不请求
      if (!_this.selectedNetbar.length) {
        window.refChart.hideLoading();
        return;
      }
      let promise = new Promise(function(resolve, reject) {
        axios({
          method: "post",
          url: "/data/api/detail",
          data: _this.selectedNetbar
        })
          .then(response => {
            //console.log(response.data)
            let data = response.data;
            _this.selectedData = data.map(item => {
              return item.map(obj => {
                return _.values(obj);
              });
            });
            //console.log(_this.selectedData)
            resolve();
          })
          .catch(error => {
            console.error(error);
            reject(error);
          });
      });
      promise.then(() => {
        //console.log(_this.selectedData)
        _this.selectedData.forEach(item => {
          let ave = new Array(9);
          ave.fill(0);
          item.forEach(arr => {
            for (let i = 3; i < arr.length; i++) {
              ave[i - 3] = ave[i - 3] + arr[i] / item.length;
            }
          });
          average.push(ave);
        });
        for (let i = 0; i < average.length; i++) {
          average[i] = average[i].map(item => {
            return Math.round(item);
          });
        }
        //转置
        average = average[0].map((col, i) => {
          return average.map(row => {
            return row[i];
          });
        });
        _this.allData = average;
        //console.log(average)
        window.refSmallChart.forEach((item, index) => {
          item.instance.chart.setOption({
            title: {
              text: window.dataTitle[index]
            },
            series: {
              id: "linechart",
              data: average[index]
            }
          });
        });
        window.refChart.hideLoading();
      });
    },
    //邮贴图初始化(重置)
    initChart: function() {
      window.refSmallChart.forEach(item => {
        item.instance.chart.setOption({
          title: {
            text: ""
          },
          series: {
            id: "linechart",
            data: []
          }
        });
      });
    },
    //按参考线采样
    startSample: function() {
      const _this = this;
      this.deleteRefline();
      //邮贴图绘完再hide
      window.refChart.showLoading("default", {
        text: "正在采样，请稍候",
        color: "#c23531",
        textColor: "#000",
        maskColor: "rgba(255, 255, 255, 0.8)",
        zlevel: 1
      });
      //不延时showLoading不能显示
      window.setTimeout(() => {
        let samplePoint = this.refLinePoints[0];
        let distance = 0;
        let i = 0;
        while (i < this.refLinePoints.length) {
          let j = i + 1;
          while (j < this.refLinePoints.length) {
            distance = Math.round(
              Math.sqrt(
                Math.pow(
                  this.refLinePoints[i][0] - this.refLinePoints[j][0],
                  2
                ) +
                  Math.pow(
                    this.refLinePoints[i][1] - this.refLinePoints[j][1],
                    2
                  )
              )
            );
            if (distance >= _this.measureAccuracy) {
              i = j;
              samplePoint = this.refLinePoints[i];
              break;
            }
            j++;
          }
          let endCondition = Math.round(
            Math.sqrt(
              Math.pow(
                this.refLinePoints[i][0] -
                  this.refLinePoints[this.refLinePoints.length - 1][0],
                2
              ) +
                Math.pow(
                  this.refLinePoints[i][1] -
                    this.refLinePoints[this.refLinePoints.length - 1][1],
                  2
                )
            )
          );
          //当前点到终点的距离小于采样精度时结束采样，以减少时间
          if (endCondition < _this.measureAccuracy) {
            break;
          }
          _this.initBrush(samplePoint[0], samplePoint[1]);
        }
        _this.drawChart();
      }, 100);
    },
    //归一化处理
    dataNormalization: function() {
      let normal = this.allData.map(item => {
        if (_.max(item) === _.min(item) && _.max(item) <= 1)
          return item.fill(0);
        else
          return item.map(val => {
            return _.round(
              _.divide(
                _.subtract(val, _.min(item)),
                _.subtract(_.max(item), _.min(item))
              ),
              5
            );
          });
      });
      this.euclideanDistance(normal);
    },
    //计算欧式距离和图表排序
    euclideanDistance: function(normal) {
      const _this = this;
      let parentNode = document.getElementById("multiple-chart");
      let childrenNode = parentNode.children;
      let baseData = normal[this.baseDataIndex];
      normal.forEach((item, index) => {
        let d = 0;
        item.forEach((val, i) => {
          d += Math.pow(_.subtract(val, baseData[i]), 2);
        });
        d = _.round(Math.sqrt(d), 5);

        for (let i in childrenNode) {
          if (childrenNode[i].id == index) {
            childrenNode[i].distance = d;
          }
        }
      });
      let tempNode = [];
      for (let i in childrenNode) {
        if (childrenNode[i].nodeType == 1) tempNode.push(childrenNode[i]);
      }
      tempNode.sort((a, b) => {
        return _.subtract(a.distance, b.distance);
      });
      if (this.baseDataIndex != tempNode[0].id) {
        let tempIndex = tempNode.findIndex(item => {
          return this.baseDataIndex == item.id;
        });
        let temp = tempNode[0];
        tempNode[0] = tempNode[tempIndex];
        tempNode[tempIndex] = temp;
      }
      for (let i = 0; i < childrenNode.length; i++) {
        parentNode.appendChild(tempNode[i]);
      }
    },
    //绘制固定基线（baseline）
    constantBaseLine: function() {
      const _this = this;
      let avg;
      let promise = new Promise(function(resolve, reject) {
        axios
          .get("data/api/avg")
          .then(response => {
            avg = response.data[0];
            //console.log(avg)
            avg = avg.map(value => {
              return Math.round(value*100)/100
            })
            resolve();
          })
          .catch(error => {
            reject();
          });
      });
      promise.then(() => {
        window.refSmallChart.forEach((item, index) => {
          avg.forEach((val, i) => {
            if (item.ref.search(String(i + 1)) != -1) {
              item.instance.chart.setOption({
                series: {
                  id: "linechart",
                  markLine: {
                    symbol: "none",
                    label: {
                      position: "start"
                    },
                    lineStyle: {
                      color: "#157ac6",
                      type: "solid",
                      opacity: 1
                    },
                    data: [
                      {
                        name: "baseline",
                        yAxis: val
                      }
                    ]
                  }
                }
              });
            }
          });
        });
      });
    }
  },
  watch: {
    //监听参考线
    refLinePoints: function(newVal) {
      window.refChart.setOption({
        graphic: {
          id: "referenceLine",
          shape: {
            points: newVal
          }
        }
      });
    }
  }
};
</script>
<style>
.map {
  
  height: 580px;
}
.lines {
  height: 100%;
}
.widget div.line {
  height: 30%;
  padding: 0;
}
.reset-button {
  position: absolute;
  top: 0;
  right: 0;
  z-index: 10;
}
.ref-chart {
  position: absolute;
  top: 0;
  left: 0;
}
</style>