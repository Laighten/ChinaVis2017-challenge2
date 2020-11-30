<template>
    <div id=page2>
        <!--右侧栏-->
    <div class="wrap">
      <div class="content container">
        <h3 class="page-title">
          Peak
          <small>Peak surfing analysis</small>
        </h3>
        <div class="row">
          <div class="col-lg-8">
            
            <section class="widget"> <P-time/> </section>
            <section class="widget"> <S-plot/> </section>
          </div>

          <div class="col-lg-4">
         
            <section class="widget"><D-time/></section>
            <section class="widget"><R-age/></section>
            
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script>

import PeakTime from "../components/PeakTime";
import Scatterplot from "../components/Scatterplot";
import AreaChart from "../components/AreaChart";
import Daytime from "../components/Daytime";
import RatioAge from "../components/RatioAge";

export default {
    components: {
    
    "P-time": PeakTime,
    "S-plot": Scatterplot,
    "D-time": Daytime,
    "A-chart":AreaChart,
    "R-age":RatioAge
  },
    data(){
        return {}
    }
}
</script>


<style>
.page2 {
  height: 100%;
  position: relative;
}
</style>