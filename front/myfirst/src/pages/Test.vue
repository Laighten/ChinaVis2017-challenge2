<template>
  <div id="test">

    <J-time/>
    <!--右侧栏-->
    <div class="wrap">
     
      <div class="content container">
        <h3 class="page-title">
          Map
          <small>重庆市违法网吧地图分布</small>
        </h3>
        <div class="row">
          <div class="col-lg-8">
            <section class="widget"><M-chart/></section>
           
          </div>

          <div class="col-lg-4">
              <!-- <section class="widget large">
                <div class="body">
                  <div id="feed" class="feed">
                      <div class="wrapper">
                          <div class="vertical-line"></div>
                          <section class="feed-item"><R-age/></section>
                      </div>
                  </div>
                </div>
              </section> -->

            <!-- <section class="widget widget-tabs">   </section> -->
          
            <section class="widget"><A-chart/></section>
            <section class="widget"><C-chart/></section>
            
          </div>
        </div>

      </div>
      <div class="loader-wrap hiding hide">
          <i class="fa fa-circle-o-notch fa-spin"> </i>
      </div>
    </div>
  </div>
</template>

<script>
import MapChart from "../components/MapChart";
import JuvTime from "../components/JuvTime";
import Daytime from "../components/Daytime";
import RatioAge from "../components/RatioAge";
import AreaChart from '../components/AreaChart';
import ColumnChart from '../components/ColumnChart';


export default {
  components: {
    "M-chart": MapChart,
    "J-time": JuvTime,
    "D-time": Daytime,
    "R-age": RatioAge,
    "A-chart":AreaChart,
    "C-chart":ColumnChart
  },
  data() {
    return {};
  },
  methods: {}
};
</script>

<style>
.test {
  height: 100%;
  position: relative;
}
</style>