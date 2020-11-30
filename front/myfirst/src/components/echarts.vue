<template>
<div class="echarts"/>
</template>

<script>
let echarts = require("echarts");
require("echarts/extension/bmap/bmap");
const EVENTS = ["datazoom", "restore", 'brush', 'brushselected'];
export default {
  name: "echarts",
  props: {
    option: Object
  },
  methods: {
    init() {
      if (this.chart) return;
      //console.log(this.option);
      let chart = echarts.init(this.$el);

      this.chart = chart;    //将echarts实例绑定到vue组件
    }
  },
  created() {},
  mounted() {
    if (this.option) this.init();
    this.chart.setOption(this.option);
    window.onresize = this.chart.resize;
  },
  watch: {
    option: {
      deep: true,
      handler: function(newVal) {
        this.chart.setOption(newVal, true);
      }
    }
  }
};
</script>
<style>
.echarts {
  
  width: 100%;
  height: 100%;
  overflow: hidden;
  position: absolute; 
}
</style>